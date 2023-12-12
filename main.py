import kivy
kivy.require('2.1.0')  # Substitua pela versão mais recente do Kivy

from kivy.app import App
from kivy.uix.label import Label

class OlaMundoApp(App):
    def build(self):
        return Label(text='Olá, mundo!')

if __name__ == '__main__':
    OlaMundoApp().run()
