from PySide2.QtWidgets import QMainWindow, QComboBox, QApplication, QMessageBox


import db
import gen
import sort
import gui


files = []
data1 = []
data2 = []


# def g_tim_comparisons_count(value):
#     return sort.tim_comparisons_count


# def g_tim_transpositions_count(value):
#     return sort.tim_transpositions_count


# def g_tim_total_time(value):
#     return sort.tim_total_time


# def g_merge_comparisons_count(value):
#     return sort.merge_comparisons_count


# def g_merge_transpositions_count(value):
#     return sort.merge_transpositions_count


# def g_merge_total_time(value):
#     return sort.merge_total_time


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
            self.unlock()

    def __sort(self):
        global data1
        global data2

        data1_sorted = sort.tim_sort(data1)
        sort.merge_sort(data2)

        db.write(data1, sort_mode="")

        print("tim_comparisons_count:", sort.tim_comparisons_count)
        print("tim_transpositions_count:", sort.tim_transpositions_count)
        print("tim_total_time:", sort.tim_total_time)

        print("merge_comparisons_count:", sort.merge_comparisons_count)
        print("merge_transpositions_count:", sort.merge_transpositions_count)
        print("merge_total_time:", sort.merge_total_time)

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
