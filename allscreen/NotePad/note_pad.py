from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Ellipse, Line

class NotePadView(Screen):
    points = []


    def on_touch_down(self, touch):
        with self.canvas:
            Color(1,1,1)
            d = 2
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]