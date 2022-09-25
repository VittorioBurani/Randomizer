from kivy.app import  App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from random import randint
from kivy.config import Config

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'height', 200)
Config.set('graphics', 'width', 150)

class Tool(RelativeLayout):
    def __init__(self, **kwargs):
        super(Tool, self).__init__(**kwargs)
        self.txtin = TextInput(size_hint=(0.8, None), height='30px', pos_hint={'x': 0.1, 'top': 1})
        self.add_widget(self.txtin)
        self.lbl = Label(text="", markup=True, font_size=70, color=(1, 0.6, 0.4, 1), size_hint=(1, None), height='100px', pos_hint={'x': 0, 'top': 0.8})
        self.add_widget(self.lbl)
        self.actbtn = Button(text="[b][size=40]Genera![/size][/b]", markup=True, color=(1, 0.6, 0.4, 1), background_color=(1, 1, 1, 0.5), size_hint=(1, None), height='70px', pos_hint={'x': 0, 'bottom': 1})
        self.actbtn.bind(on_press=self.click)
        self.add_widget(self.actbtn)
    def click(self, btn):
        if self.txtin.text!="":
            self.lbl.text = str(randint(1, int(self.txtin.text)))


class Randomizer(App):
    def build(self):
        self.tool = Tool()
        return self.tool


if __name__ == '__main__':
    Randomizer().run()
