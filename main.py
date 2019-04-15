from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle, Line
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.app import App
from kivy.graphics import Mesh
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from functools import partial
from math import cos, sin, pi, floor


class CellularAutomatonApp(App):

    def change_mode(self, mode, *largs):
        self.mesh.mode = mode

    def build(self):
        Window.size = (600, 650)
        wid = Widget()

        layout = FloatLayout(size=(600, 600))
        layout.add_widget(Label(text='Enter size:', size_hint_x=None, width=100, size_hint=(.2, .1),
                                pos_hint={'x': 0.05, 'y': 0.1}))
        layout.add_widget(TextInput(size_hint_x=None, width=50, multiline=False, size_hint=(.2, .1),
                                    pos_hint={'x': .25, 'y': .1}))
        layout.add_widget(Label(text='Rule:', size_hint_x=None, width=100, size_hint=(.2, .1),
                                pos_hint={'x': .40, 'y': .1}))

        dropdown = DropDown()
        for index in range(1, 4):
            btn = Button(text='Rule %d' % (index * 30), size_hint_y=None, height=35)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        mainbutton = Button(text='Choose rule', width=100, size_hint_x=None, size_hint=(.2, .1),
                            pos_hint={'x': .55, 'y': .1})
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        layout.add_widget(mainbutton)
        layout.add_widget(Button(text='Calculate', size_hint_x=None, width=100, size_hint=(.2, .1),
                                 pos_hint={'x': 0.75, 'y': 0.1}))

        root = BoxLayout(orientation='vertical')
        root.add_widget(wid)
        root.add_widget(layout)

        height = 550
        width = 550

        size = 50
        stepWidth = floor(width / (size+1))
        stepHeight = floor(height / (size+1))
        with wid.canvas:
            Color(1., 1, 1)

            for index in range(0, size+1):
                #poziome
                Line(points=[0.1 * width, index * stepHeight + 0.2 * stepHeight * (size+1),
                             size * stepWidth + 0.1 * width, index * stepHeight + 0.2 * stepHeight * (size+1)],
                     width=1)

                #pionowe
                Line(points=[index * stepWidth + 0.1 * width, 0.2 * stepHeight * (size+1),
                             index * stepWidth + 0.1 * width, size * stepHeight + 0.2 * stepHeight * (size + 1)],
                     width=1)

        return root


if __name__ == '__main__':
    CellularAutomatonApp().run()
