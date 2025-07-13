"""
My first application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER


class Strong(toga.App):
    def startup(self):
        self.input = toga.TextInput(placeholder="Введите имя")
        self.button = toga.Button("Привет!", on_press=self.say_hello)
        self.label = toga.Label("")

        box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=20))
        box.add(self.input)
        box.add(self.button)
        box.add(self.label)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = box
        self.main_window.show()

    def say_hello(self, widget):
        self.label.text = f"Привет, {self.input.value}!"


def main():
    return Strong()
