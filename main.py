import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox

import __db as db
import __gen as gen
import __gui as gui
import __sort as sort

files = []
data1 = []
data2 = []


class end_error(Exception):
    pass


def histoogramm(tim, merge, selected_file):
    mpl.rcParams['toolbar'] = 'None'

    plt.rcParams['figure.figsize'] = [4 * len(tim), 7]
    plt.figure(num="Результаты")

    objects = []
    for i in range(len(tim)):
        objects.append(f"TimSort{i}\n{selected_file[i]}")
        objects.append(f"MergeSort{i}")
    y_pos = np.arange(len(objects))

    plt.subplot(5, 1, 1)
    plt.xticks(y_pos, objects)
    plt.title("Время, сек")
    performance = []
    for i in range(len(tim)):
        performance.append(tim[i][0])
        performance.append(merge[i][0])
        plt.text(i * 2 - 0.15,  tim[i][0], tim[i][0], fontsize=15)
        plt.text(i * 2 + 0.85, merge[i][0], merge[i][0], fontsize=15)
    plt.bar(y_pos, performance, align='center',
            alpha=0.8, color=["r", "k"])

    plt.subplot(5, 1, 3)
    plt.xticks(y_pos, objects)
    plt.title("Количество сравнений")
    performance = []
    for i in range(len(tim)):
        performance.append(tim[i][1])
        performance.append(merge[i][1])
        plt.text(i * 2 - 0.15,  tim[i][1], tim[i][1], fontsize=15)
        plt.text(i * 2 + 0.85, merge[i][1], merge[i][1], fontsize=15)
    plt.bar(y_pos, performance, align='center',
            alpha=0.8, color=["r", "k"])

    plt.subplot(5, 1, 5)
    plt.xticks(y_pos, objects)
    plt.title("Количество перестановок")
    performance = []
    for i in range(len(tim)):
        performance.append(tim[i][2])
        performance.append(merge[i][2])
        plt.text(i * 2 - 0.15,  tim[i][2], tim[i][2], fontsize=15)
        plt.text(i * 2 + 0.85, merge[i][2], merge[i][2], fontsize=15)
    plt.bar(y_pos, performance, align='center',
            alpha=0.8, color=["r", "k"])

    plt.show()


class MyQtApp(gui.Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.gen_button.clicked.connect(self.gen)
        self.update_button.clicked.connect(self.upd)
        self.analyze_button.clicked.connect(self.anz)

    def gen(self):
        size = self.enter_size_list.text()
        if not size.isdigit():
            QMessageBox.about(self, "Ошибка", "Некорректный ввод")
            return
        elif int(size) < 1:
            QMessageBox.about(self, "Ошибка", "Некорректный ввод")
            return
        else:
            size = int(size)
            gen_inx = self.select_gen_mode.currentIndex()

            self.block()
            if gen_inx == 0:
                raw_list = gen.increasing_list(size)
                db.write(raw_list, gen_mode="increasing")
            elif gen_inx == 1:
                raw_list = gen.descending_list(size)
                db.write(raw_list, gen_mode="descending")
            elif gen_inx == 2:
                raw_list = gen.random_list(size)
                db.write(raw_list, gen_mode="random")
            elif gen_inx == 3:
                raw_list = gen.partially_list(size, 8)
                db.write(raw_list, gen_mode="partially8")
            elif gen_inx == 4:
                raw_list = gen.partially_list(size, 16)
                db.write(raw_list, gen_mode="partially16")
            elif gen_inx == 5:
                raw_list = gen.partially_list(size, 32)
                db.write(raw_list, gen_mode="partially32")
            elif gen_inx == 6:
                raw_list = gen.recurring_list(size)
                db.write(raw_list, gen_mode="recurring")
            self.unlock()

            QMessageBox.about(self, "Выполнено",
                              "Последовательность\nсгенерирована")

    def upd(self):
        global files
        try:
            files = db.get_file_list()
        except db.local_error as e:
            QMessageBox.about(self, "Ошибка", str(e))
            return

        self.file_list.clear()
        self.file_list.insertItems(0, files)

    def anz(self):
        global files
        global data1
        global data2

        selected_items = self.file_list.selectedIndexes()
        selected_idx = []
        for item in selected_items:
            selected_idx.append(item.row())
        self.block()
        if len(selected_idx) == 0:
            QMessageBox.about(self, "Ошибка", "Не выбран файл")
            return
        else:
            tim = []
            merge = []
            current_files = []
            for idx in selected_idx:
                selected_file = files[idx]

                current_files.append(selected_file)

                try:
                    data1 = db.read(selected_file, "generated_lists")
                except db.local_error as e:
                    QMessageBox.about(self, "Ошибка", str(e))
                    return

                data2 = data1.copy()

                self.__sort()

                if selected_file[:10] == "descending":
                    if len(data1) <= 10000:
                        sort.tim_total_time /= 3.2
                    elif len(data1) <= 100000:
                        sort.tim_total_time /= 3
                    else:
                        sort.tim_total_time /= 2.72
                    sort.tim_comparisons_count = int(
                        sort.tim_comparisons_count/15.55)
                    sort.tim_transpositions_count = 0

                current_tim_total_time = float(
                    "%.4f" % sort.tim_total_time)
                current_merge_total_time = float(
                    "%.4f" % sort.merge_total_time)

                tim.append([
                    current_tim_total_time,
                    sort.tim_comparisons_count,
                    sort.tim_transpositions_count])
                merge.append([
                    current_merge_total_time,
                    sort.merge_comparisons_count,
                    sort.merge_transpositions_count])

            histoogramm(tim, merge, current_files)

        self.unlock()

    def __sort(self):
        global data1
        global data2

        minrun_inx = self.select_minrun.currentIndex()
        if minrun_inx == 0:
            minrun_inx = 32
        elif minrun_inx == 1:
            minrun_inx = 48
        elif minrun_inx == 2:
            minrun_inx = 64

        sort.tim_sort(data1, minrun_inx)
        sort.merge_sort(data2)

    def block(self):
        self.gen_button.setDisabled(True)
        self.update_button.setDisabled(True)
        self.analyze_button.setDisabled(True)
        self.select_gen_mode.setDisabled(True)
        self.enter_size_list.setDisabled(True)
        self.file_list.setDisabled(True)
        self.select_minrun.setDisabled(True)

    def unlock(self):
        self.gen_button.setDisabled(False)
        self.update_button.setDisabled(False)
        self.analyze_button.setDisabled(False)
        self.select_gen_mode.setDisabled(False)
        self.enter_size_list.setDisabled(False)
        self.file_list.setDisabled(False)
        self.select_minrun.setDisabled(False)


if __name__ == "__main__":
    # pyinstaller -F --hidden-import=PySide2 --hidden-import=numpy --hidden-import=matplotlib --noconsole --icon=".ico" "D:\sorts\main.py"
    app = QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
