from PyQt6.QtWidgets import QLabel


def label(text, position=None, height=None):
    """
    label(text: str, position: QAlignmentFlag, height: int)
    """
    l = QLabel()
    l.setText(text)
    if height:
        l.setFixedHeight(height)
    if position:
        l.setAlignment(position)
    return l