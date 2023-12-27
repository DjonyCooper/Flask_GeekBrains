import asyncio
import sys
import time
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout, QMessageBox
from PyQt6.QtCore import Qt
from widgets.widget_line_edit import line_edit, plain_text_edit
from widgets.widget_button import push_button, radio_button
from widgets.widget_label import label
from widgets.widget_layout import h_box

from functions.request_image import threads_download_img, processes_download_img, async_download_img



class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 400)
        self.setWindowTitle('Многозадачность в Python')
        self.setWindowIcon(QIcon('icons/gb_logo.ico'))
        self.row_counter = 0
        self.grid = QGridLayout()
        self.grid_line_url = QGridLayout()
        self.grid.addWidget(label(text='Добро пожаловать в Многозадачность от GeekBrains!\n'
                                       'для скачивания файлов, укажите URL, выберите подход и нажмите "ОК"',
                                  position=Qt.AlignmentFlag.AlignCenter,
                                  height=35), 0, 0, 1, 3)
        self.grid.addLayout(self.generate_line_url(), 1, 0, 1, 3)
        self.grid.addWidget(radio_button(name='Многопоточный',
                                         checked=True), 2, 0, 1, 1, Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(radio_button(name='Многопроцессорный'), 2, 1, 1, 1, Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(radio_button(name='Асинхронный'), 2, 2, 1, 1, Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(plain_text_edit(self=self,
                                            read_only=True,
                                            placeholder='Здесь будет показан результат выполнения запроса'),
                            self.row_counter + 2, 0, 1, 3)
        self.grid.addWidget(push_button(name='ok!',
                                        color='lightgreen',
                                        img='icons/ok.ico',
                                        do=self.do_task), 4, 0, 1, 2)
        self.grid.addWidget(push_button(color='red',
                                        name='Закрыть',
                                        do=self.close_app), 4, 2, 1, 1)
        self.setLayout(self.grid)

    def generate_line_url(self):
        """Функция динамической генерации строки для ввода URL"""
        self.grid_line_url.addLayout(h_box(line_edit(height=30,
                                                     placeholder='Укажите ссылку на изображение'),
                                           push_button(width=30,
                                                       height=30,
                                                       name='+',
                                                       do=self.generate_line_url)), self.row_counter, 0, 1, 3)
        self.row_counter += 1
        return self.grid_line_url

    def do_task(self):
        """Функция собирает все данные с созданных QLineEdit (*если они есть) и, в зависимости от выбранного подхода,
        выполняет задачу и возвращает результат выполнения"""
        url_box = []
        approach = self.check_radio_button()
        for i in self.children():
            if type(i).__name__ == 'QLineEdit' and i.text() != '':
                url_box.append(i.text())
        if not url_box:
            QMessageBox.warning(self, 'Ошибка', 'Для выполнения задачи, нужно заполнить хотя бы 1 поле')
        else:
            if approach == 'Многопоточный':
                save_img = threads_download_img(url_box)
            elif approach == 'Многопроцессорный':
                save_img = processes_download_img(url_box)
            elif approach == 'Асинхронный':
                start_time = time.time()
                loop = asyncio.get_event_loop()
                loop.run_until_complete(async_download_img(url_box))
                save_img = f'Асинхронный запрос выполнен\nВремя выполнения запроса: {time.time() - start_time}'
            self.pte.setPlainText(save_img)

    def check_radio_button(self):
        """Функция возвращает название выбранной пользователем QRadioButton"""
        for i in self.children():
            if type(i).__name__ == 'QRadioButton':
                if i.isChecked():
                    return i.text()

    def close_app(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Main()
    w.show()
    sys.exit(app.exec())
