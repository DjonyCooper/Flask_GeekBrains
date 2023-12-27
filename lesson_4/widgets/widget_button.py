from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton, QRadioButton


def push_button(width=None, height=None, color=None, name=None, img=None, do=None):
    """
    push_button(width: int, height: int, color: str, name: str, img: str|path, do: func)
    """
    but = QPushButton()
    if width is not None and height is not None:
        but.setFixedSize(width, height)
    if name:
        but.setText(name)
    if img:
        but.setIcon(QIcon(img))
    if color:
        but.setStyleSheet(f'background-color: {color};')
    if do:
        but.clicked.connect(do)
    return but


def radio_button(name, checked=None):
    """
    radio_button(name: str, checked: bool)
    """
    rb = QRadioButton()
    rb.setText(name)
    if checked and checked is True or checked is False:
        rb.setChecked(checked)
    return rb
