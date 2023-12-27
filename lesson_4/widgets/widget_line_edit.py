from PyQt6.QtWidgets import QLineEdit, QPlainTextEdit


def line_edit(height=None, placeholder=None):
    """
    line_edit(height: int, placeholder: str)
    """
    le = QLineEdit()
    if height:
        le.setFixedHeight(height)
    if placeholder:
        le.setPlaceholderText(placeholder)
    return le

def plain_text_edit(self, read_only=None, placeholder=None):
    """
    plain_text_edit(read_only: bool, placeholder: str)
    """
    self.pte = QPlainTextEdit()
    if read_only:
        self.pte.setReadOnly(read_only)
    if placeholder:
        self.pte.setPlaceholderText(placeholder)
    return self.pte
