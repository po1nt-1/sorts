import matplotlib.pyplot as plt
import numpy as np
from PySide2.QtWidgets import QMainWindow, QComboBox, QApplication, QMessageBox


import db
import gen
import sort
import gui


files = []
data1 = []
data2 = []


def histoogramm(data1, data2):
    plt.subplot(5, 1, 1)

    objects = ('TimeSort', 'MergeSort')
    y_pos = np.arange(len(objects))
    performance = [data1[0], data2[0]]
    plt.bar(y_pos, performance, align='center', alpha=0.8, color="bg")
    plt.xticks(y_pos, objects)
    plt.title("Время")

    plt.subplot(5, 1, 3)

    objects = ('TimeSort', 'MergeSort')
    y_pos = np.arange(len(objects))
    performance = [data1[1], data2[1]]
    plt.bar(y_pos, performance, align='center', alpha=0.8, color="bg")
    plt.xticks(y_pos, objects)
    plt.title("Сравнения")

    plt.subplot(5, 1, 5)

    objects = ('TimeSort', 'MergeSort')
    y_pos = np.arange(len(objects))
    performance = [data1[2], data2[2]]
    plt.bar(y_pos, performance, align='center', alpha=0.8, color="bg")
    plt.xticks(y_pos, objects)
    plt.title("Перестановки")

    plt.show()


class MyQtApp(gui.Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.gen_button.clicked.connect(self.gen)
        self.update_button.clicked.connect(self.upd)
        self.analyze_button.clicked.connect(self.anal)

    def gen(self):
        size = self.enter_size_list.text()
        if not size.isdigit():
            QMessageBox.about(self, "Предупреждение", "Не корректный ввод")
        elif int(size) < 1:
            QMessageBox.about(self, "Предупреждение", "Не корректный ввод")
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
            else:
                QMessageBox.about(self, "", "Что-то не так")
            self.unlock()

            QMessageBox.about(self, "", "Последовательность\nсгенерирована")

    def upd(self):
        global files
        files = db.get_file_list()

        self.file_list.clear()
        self.file_list.insertItems(0, files)

    def anal(self):
        global files
        global data1
        global data2

        file_num = self.file_list.currentRow()

        if file_num == -1:
            QMessageBox.about(self, "Предупреждение", "Не выбран файл")
        else:
            selected_file = files[file_num]

            self.block()
            data1 = db.read(selected_file, "generated_lists")
            data2 = data1.copy()

            self.__sort()

            tim = [sort.tim_total_time, sort.tim_comparisons_count,
                   sort.tim_transpositions_count]
            merge = [sort.merge_total_time, sort.merge_comparisons_count,
                     sort.merge_transpositions_count]

            histoogramm(tim, merge)
            self.unlock()

            print("tim_comparisons_count:", sort.tim_comparisons_count)
            print("tim_transpositions_count:", sort.tim_transpositions_count)
            print("tim_total_time:", sort.tim_total_time)

            print("merge_comparisons_count:", sort.merge_comparisons_count)
            print("merge_transpositions_count:",
                  sort.merge_transpositions_count)
            print("merge_total_time:", sort.merge_total_time)

    def __sort(self):
        global data1
        global data2

        data1_sorted = sort.tim_sort(data1)
        sort.merge_sort(data2)

        db.write(data1, sort_mode="")

    def block(self):
        # TODO does not work
        self.gen_button.setHidden(True)
        self.update_button.setHidden(True)
        self.analyze_button.setHidden(True)
        self.select_gen_mode.setHidden(True)
        self.enter_size_list.setHidden(True)
        self.file_list.setHidden(True)

    def unlock(self):
        # TODO does not work
        self.gen_button.setHidden(False)
        self.update_button.setHidden(False)
        self.analyze_button.setHidden(False)
        self.select_gen_mode.setHidden(False)
        self.enter_size_list.setHidden(False)
        self.file_list.setHidden(False)


if __name__ == "__main__":
    app = QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
