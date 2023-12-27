from PyQt6.QtWidgets import QHBoxLayout


def h_box(*args):
    """
    label(args: widgets)
    """
    box = QHBoxLayout()
    if args:
        for widget in args:
            box.addWidget(widget)
    return box
