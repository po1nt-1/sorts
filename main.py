import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from PySide2.QtWidgets import QMainWindow, QComboBox, QApplication, QMessageBox


import __db as db
import __gen as gen
import __sort as sort
import __gui as gui


files = []
data1 = []
data2 = []


class end_error(Exception):
    pass


def histoogramm(data1, data2):
    mpl.rcParams['toolbar'] = 'None'
    plt.rcParams['figure.figsize'] = [5, 7]
    plt.figure(num="Результаты")
    objects = ('TimeSort', 'MergeSort')
    y_pos = np.arange(len(objects))

    plt.subplot(5, 1, 1)
    plt.xticks(y_pos, objects)
    plt.title("Время, сек")
    performance = [data1[0], data2[0]]
    plt.bar(y_pos, performance, align='center',
            alpha=0.9, color=["r", "k"])

    plt.subplot(5, 1, 3)
    plt.bar(y_pos, performance, align='center',
            alpha=0.9, color=["r", "k"])
    plt.xticks(y_pos, objects)
    plt.title("Количество сравнений")
    performance = [data1[1], data2[1]]

    plt.subplot(5, 1, 5)
    plt.bar(y_pos, performance, align='center',
            alpha=0.9, color=["r", "k"])
    plt.xticks(y_pos, objects)
    plt.title("Количество перестановок")
    performance = [data1[2], data2[2]]

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

        elif int(size) < 1:
            QMessageBox.about(self, "Ошибка", "Некорректный ввод")
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
                raw_list = gen.partially_list(size)
                db.write(raw_list, gen_mode="partially")
            elif gen_inx == 4:
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

        self.file_list.clear()
        self.file_list.insertItems(0, files)

    def anz(self):
        global files
        global data1
        global data2

        file_num = self.file_list.currentRow()

        if file_num == -1:
            QMessageBox.about(self, "Ошибка", "Не выбран файл")
        else:
            selected_file = files[file_num]

            self.block()
            try:
                data1 = db.read(selected_file, "generated_lists")
            except db.local_error as e:
                QMessageBox.about(self, "Ошибка", str(e))

            data2 = data1.copy()

            self.__sort()

            tim = [sort.tim_total_time, sort.tim_comparisons_count,
                   sort.tim_transpositions_count]
            merge = [sort.merge_total_time, sort.merge_comparisons_count,
                     sort.merge_transpositions_count]

            histoogramm(tim, merge)

            self.unlock()

            # debug
            print("tim_comparisons_count:", sort.tim_comparisons_count)
            print("tim_transpositions_count:", sort.tim_transpositions_count)
            print("tim_total_time:", sort.tim_total_time)

            print("merge_comparisons_count:", sort.merge_comparisons_count)
            print("merge_transpositions_count:",
                  sort.merge_transpositions_count)
            print("merge_total_time:", sort.merge_total_time)
            # debug

    def __sort(self):
        global data1
        global data2

        data1_sorted = sort.tim_sort(data1)
        sort.merge_sort(data2)

        try:
            db.write(data1, sort_mode=True)
        except db.local_error as e:
            QMessageBox.about(self, "Ошибка", str(e))

    def block(self):
        self.gen_button.setDisabled(True)
        self.update_button.setDisabled(True)
        self.analyze_button.setDisabled(True)
        self.select_gen_mode.setDisabled(True)
        self.enter_size_list.setDisabled(True)
        self.file_list.setDisabled(True)

    def unlock(self):
        self.gen_button.setDisabled(False)
        self.update_button.setDisabled(False)
        self.analyze_button.setDisabled(False)
        self.select_gen_mode.setDisabled(False)
        self.enter_size_list.setDisabled(False)
        self.file_list.setDisabled(False)


if __name__ == "__main__":
    app = QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
