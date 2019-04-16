from math import floor

from kivy.app import App
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from algorithm import calculate

global width, height, stepHeight, stepWidth, size, rule, surface


def updateMesh(value):
    global width, height
    global stepWidth
    global stepHeight
    global size

    wid.canvas.clear()

    height = 550
    width = 550

    value = int(value)
    size = value
    stepWidth = floor(width / (value + 1))
    stepHeight = floor(height / (value + 1))
    with wid.canvas:
        Color(1., 1, 1)

        for index in range(0, value + 1):
            # poziome
            Line(points=[0.1 * width,
                         stepHeight * (index + 0.2 * (value + 1)),
                         value * stepWidth + 0.1 * width,
                         stepHeight * (index + 0.2 * (value + 1))],
                 width=1)

            # pionowe
            Line(points=[index * stepWidth + 0.1 * width,
                         0.2 * stepHeight * (value + 1),
                         index * stepWidth + 0.1 * width,
                         stepHeight * (value + 0.2 * (value + 1))],
                 width=1)

    pass


def selected(mainbutton):
    global rule
    rule = int(mainbutton[-2:])
    children = layout.children
    setattr(children[1], 'text', 'Rule ' + str(rule))


def drawStartingPoint(value):
    global size
    global surface
    value = int(value)
    size = int(size)
    with wid.canvas:
        Rectangle(pos=(value * stepWidth + 0.1 * width, stepHeight * (size - 1 + 0.2 * (size + 1))),
                  size=(stepWidth, stepWidth))

    surface[0][value] = True
    pass


def drawPoints():
    for i in range(size):
        for j in range(size):
            if surface[i][j]:
                with wid.canvas:
                    Color(1, 1, 1, 1)
                    Rectangle(pos=(j * stepWidth + 0.1 * width, stepHeight * (size - i - 1 + 0.2 * (size + 1))),
                              size=(stepWidth, stepWidth))

    pass


def on_enter_size(value):
    global size, surface
    size = int(value.text)
    surface = [[False for x in range(size)] for y in range(size)]

    updateMesh(value.text)


def on_enter_starting_point(value):
    if int(value.text) > size:
        return
    drawStartingPoint(value.text)


def calculateAction(self):
    global surface
    newSurface = calculate(surface, size, rule)
    surface = newSurface

    drawPoints()


def reset(self):
    wid.canvas.clear()
    updateMesh(size)

    pass


class CellularAutomatonApp(App):

    def build(self):
        Window.size = (600, 680)

        layout.add_widget(Label(text='Starting point:', size_hint_x=None, width=100, size_hint=(.2, .08),
                                pos_hint={'x': 0.05, 'y': 1.9}))
        self.startingPoint = TextInput(size_hint_x=None, width=30, multiline=False, size_hint=(.09, .08),
                                       pos_hint={'x': .25, 'y': 1.9}, input_filter='int')
        self.startingPoint.bind(on_text_validate=on_enter_starting_point)
        layout.add_widget(self.startingPoint)

        resetButton = Button(text='RESET', size_hint_x=None, width=100, size_hint=(.2, .08),
                             background_color=(1, 0, 0, 1), pos_hint={'x': 0.7, 'y': 1.9})
        resetButton.bind(on_press=reset)
        layout.add_widget(resetButton)

        layout.add_widget(Label(text='Enter size:', size_hint_x=None, width=100, size_hint=(.2, .1),
                                pos_hint={'x': 0.05, 'y': 0.1}))

        sizeInput = TextInput(size_hint_x=None, width=50, multiline=False, size_hint=(.2, .1),
                              pos_hint={'x': .25, 'y': .1}, input_filter='int')
        sizeInput.bind(on_text_validate=on_enter_size)

        layout.add_widget(sizeInput)
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
        dropdown.bind(on_select=lambda self, mainbutton: selected(mainbutton))

        layout.add_widget(mainbutton)

        calculateButton = Button(text='Calculate', size_hint_x=None, width=100, size_hint=(.2, .1),
                                 pos_hint={'x': 0.75, 'y': 0.1})
        calculateButton.bind(on_press=calculateAction)
        layout.add_widget(calculateButton)

        root = BoxLayout(orientation='vertical')
        root.add_widget(wid)
        root.add_widget(layout)

        return root


if __name__ == '__main__':
    layout = FloatLayout(size=(600, 600))
    wid = Widget()
    CellularAutomatonApp().run()
