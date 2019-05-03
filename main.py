from math import floor

from kivy.app import App
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from algorithm import calculate

global width, height, stepHeight, stepWidth, size, rule, surface, iteration


def updateMesh():
    global width, height
    global stepWidth
    global stepHeight
    global size, iteration

    wid.canvas.clear()

    height = Window.height
    width = Window.width

    stepWidth = floor(width / (size + 1))
    stepHeight = floor(height / (size + 1))
    with wid.canvas:
        Color(1., 1, 1)

        for index in range(0, iteration + 1):
            # poziome
            Line(points=[0.1 * width,
                         stepHeight*(size-index),
                         size * stepWidth + 0.1 * width,
                         stepHeight * (size-index)],
                 width=1)

        for index in range(0, size + 1):
            # pionowe
            Line(points=[(size - index) * stepWidth + 0.1 * width,
                         stepHeight*size,
                         (size - index) * stepWidth + 0.1 * width,
                         stepHeight*(size-iteration)],
                 width=1)

    pass


def drawStartingPoint(value):
    global size
    global surface
    value = int(value)
    size = int(size)
    with wid.canvas:
        Rectangle(pos=(value * stepWidth + 0.1 * width, stepHeight * (size - 1 + 0.2 * (size + 1))),
                  size=(stepWidth, stepWidth))
        pass

    surface[0][value] = True
    pass


def drawPoints():
    global iteration

    for i in range(iteration):
        for j in range(size):
            if surface[i][j]:
                with wid.canvas:
                    Color(1, 1, 1, 1)
                    Rectangle(pos=(j * stepWidth + 0.1 * width, stepHeight * (size - i - 1 + 0.2 * (size + 1))),
                              size=(stepWidth, stepWidth))

    pass


def on_enter_size(value):
    global size, surface, iteration
    size = int(value.text)


def rule_input(value):
    global rule
    rule = int(value.text)
    pass


def iteration_input(value):
    global iteration, surface

    iteration = int(value.text)
    surface = [[False for x in range(size)] for y in range(iteration)]
    updateMesh()


def on_enter_starting_point(value):
    if int(value.text) > size:
        return
    drawStartingPoint(value.text)


def calculateAction(self):
    global surface, rule, iteration
    newSurface = calculate(surface, size, rule, iteration)
    surface = newSurface

    updateMesh()
    drawPoints()


def reset(self):
    wid.canvas.clear()
    updateMesh()
    pass


class NewClass(FloatLayout):

    def __init__(self, **kwargs):
        super(NewClass, self).__init__(**kwargs)

        Window.size = (600, 680)

        self.add_widget(Label(text='Starting point:', size_hint_x=None, width=100, size_hint=(.2, .08),
                              pos_hint={'x': 0.05, 'y': 1.9}))
        self.startingPoint = TextInput(size_hint_x=None, width=30, multiline=False, size_hint=(.09, .08),
                                       pos_hint={'x': .25, 'y': 1.9}, input_filter='int')
        self.startingPoint.bind(on_text_validate=on_enter_starting_point)
        self.add_widget(self.startingPoint)

        resetButton = Button(text='RESET', size_hint_x=None, width=100, size_hint=(.2, .08),
                             background_color=(1, 0, 0, 1), pos_hint={'x': 0.7, 'y': 1.9})
        resetButton.bind(on_press=reset)
        self.add_widget(resetButton)

        self.add_widget(Label(text='Enter size:', size_hint_x=None, width=100, size_hint=(.2, .1),
                              pos_hint={'x': 0.05, 'y': 0.1}))

        sizeInput = TextInput(size_hint_x=None, width=50, multiline=False, size_hint=(.2, .1),
                              pos_hint={'x': .25, 'y': .1}, input_filter='int')
        sizeInput.bind(on_text_validate=on_enter_size)

        self.add_widget(sizeInput)
        self.add_widget(Label(text='Rule:', size_hint_x=None, width=100, size_hint=(.2, .1),
                              pos_hint={'x': .40, 'y': .1}))

        ruleInput = TextInput(size_hint_x=None, width=50, multiline=False, size_hint=(.2, .1),
                              pos_hint={'x': .55, 'y': .1}, input_filter='int')
        ruleInput.bind(on_text_validate=rule_input)
        self.add_widget(ruleInput)

        self.add_widget(Label(text='Iteration No.:', size_hint_x=None, width=100, size_hint=(.2, .1),
                              pos_hint={'x': .33, 'y': 1.89}))

        iterationInput = TextInput(size_hint_x=None, width=30, multiline=False, size_hint=(.1, .1),
                                   pos_hint={'x': .5, 'y': 1.89}, input_filter='int')
        iterationInput.bind(on_text_validate=iteration_input)
        self.add_widget(iterationInput)

        calculateButton = Button(text='Calculate', size_hint_x=None, width=100, size_hint=(.2, .1),
                                 pos_hint={'x': 0.75, 'y': 0.1})
        calculateButton.bind(on_press=self.tmp)
        self.add_widget(calculateButton)


    def tmp(self, *args):
        global width, height


        with self.canvas.before:
            Color(1, 0, 0, 1)
            Rectangle(pos=self.pos,
                      size=self.size)

        print(self.width)
        print(self.height)

        print(width)
        print(height)


class CellularAutomatonApp(App):

    def build(self):
        root = BoxLayout(orientation='vertical')
        root.add_widget(wid)
        root.add_widget(NewClass())
        return root


if __name__ == '__main__':
    # self = FloatLayout(size=(600, 600))
    wid = Widget()
    CellularAutomatonApp().run()
