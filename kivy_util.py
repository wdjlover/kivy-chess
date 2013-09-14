from kivy.resources import resource_find
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Rectangle
from kivy.graphics import Color

class ScrollableLabel(ScrollView):
    def __init__(self, text, ref_callback=None, *args, **kwargs):
        super(ScrollableLabel, self).__init__(*args, **kwargs)
        with self.canvas:
            Color(0.7, .02, 0.91, mode="hsv")
            # Color(.69, .93, .93)

            self.background = Rectangle(size_hint=(1,1))
        self.label = Label(text=text, font_size=13, font_name='DroidSans', size_hint_y=None, pos_hint={'x':0.1, 'y':0.1})
        self.label.bind(texture_size=self._set_summary_height, on_ref_press=ref_callback)
        # self.label.text=text
        self.label.markup=True

        self.add_widget(self.label)
        self.bind(pos=self.change_position)
        self.bind(size=self.change_size)

    def _set_summary_height(self, instance, size):
        instance.height = size[1]

    def change_position(self, instance, position):
        self.background.pos = position

    def change_size(self, instance, size):
        self.background.size = size
        self.label.text_size = (size[0]-50, None)

