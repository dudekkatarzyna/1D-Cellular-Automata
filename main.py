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

global width
global stepWidth
global stepHeight
global size

def updateMesh(value):
    global width
    global stepWidth
    global stepHeight
    wid.canvas.clear()


    height = 550
    width = 550

    value = int(value)
    stepWidth = floor(width / (value + 1))
    stepHeight = floor(height / (value + 1))
    with wid.canvas:
        Color(1., 1, 1)

        for index in range(0, value + 1):
            # poziome   i
            Line(points=[0.1 * width,
                         stepHeight * (index + 0.2 * (value + 1)),
                         value * stepWidth + 0.1 * width,
                         stepHeight * (index + 0.2 * (value + 1))],
                 width=1)

            # pionowe   j
            Line(points=[index * stepWidth + 0.1 * width,
                         0.2 * stepHeight * (value + 1),
                         index * stepWidth + 0.1 * width,
                         stepHeight * (value + 0.2 * (value + 1))],
                 width=1)


    pass


def drawStartingPoint(value):
    global stepWidth
    global size
    value=int(value)
    size=int(size)
    with wid.canvas:
        Rectangle(pos=(value * stepWidth + 0.1 * width, stepHeight * (size-1 + 0.2 * (size+1))), size=(stepWidth, stepWidth))
    pass


class CellularAutomatonApp(App):

    def on_enter(self, value):
        #  print('The widget', instance, 'have:', value)
        updateMesh(value.text)

    def on_enter_starting_point(self, value):
        #  print('The widget', instance, 'have:', value)
        drawStartingPoint(value.text)

    def calculate(self):
        print()

    def build(self):
        global size
        Window.size = (600, 650)

        layout = FloatLayout(size=(600, 600))

        layout.add_widget(Label(text='Starting point:', size_hint_x=None, width=100, size_hint=(.2, .08),
                                pos_hint={'x': 0.05, 'y': 1.9}))
        self.startingPoint = TextInput(size_hint_x=None, width=30, multiline=False, size_hint=(.09, .08),
                                       pos_hint={'x': .25, 'y': 1.9}, input_filter='int')
        self.startingPoint.bind(on_text_validate=self.on_enter_starting_point)
        layout.add_widget(self.startingPoint)

        layout.add_widget(Label(text='Enter size:', size_hint_x=None, width=100, size_hint=(.2, .1),
                                pos_hint={'x': 0.05, 'y': 0.1}))

        self.size = TextInput(size_hint_x=None, width=50, multiline=False, size_hint=(.2, .1),
                              pos_hint={'x': .25, 'y': .1}, input_filter='int')
        self.size.bind(on_text_validate=self.on_enter)

        layout.add_widget(self.size)
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

        calculateButton=Button(text='Calculate', size_hint_x=None, width=100, size_hint=(.2, .1),
                                 pos_hint={'x': 0.75, 'y': 0.1})
        calculateButton.bind(on_press=self.calculate)
        layout.add_widget(calculateButton)

        root = BoxLayout(orientation='vertical')
        root.add_widget(wid)
        root.add_widget(layout)

        size = 30
        updateMesh(30)

        return root


if __name__ == '__main__':
    wid = Widget()
    CellularAutomatonApp().run()
