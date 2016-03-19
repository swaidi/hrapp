__author__ = 'HP'
import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.checkbox import CheckBox
from kivy.uix.widget import Widget
import sqlalchemy
from kivy.uix.image import Image
import pony
import plyer
from kivy.uix.scrollview import ScrollView
from kivy.uix.listview import ListItemButton


Builder.load_file('screens.kv')
Builder.load_file('addlocation.kv')




class ScreenOne(Screen,BoxLayout):
    first_screen = ObjectProperty(None)
    def __init__(self,**kwargs):
        super (ScreenOne,self).__init__(**kwargs)


    def changer(self,*args):
        self.manager.current = 'screen4'

    def change(self,*args):
        self.manager.current = 'screen4'





class ScreenTwo(Screen,BoxLayout):
    second_screen = ObjectProperty(None)
    def __init__(self,**kwargs):
        super (ScreenTwo,self).__init__(**kwargs)


    def changer(self,*args):
        self.manager.current = 'screen4'

    def change(self,*args):
        self.manager.current = 'screen4'

class ScreenThree(Screen, FloatLayout):
    third_screen = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(ScreenThree,self).__init__(**kwargs)

    def change(self,*args):
        self.manager.current = 'screen4'

class ScreenFour(Screen, GridLayout):
    fourth_screen = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(ScreenFour,self).__init__(**kwargs)

    def changer(self,*args):
        self.manager.current = 'screen1'


    def change(self,*args):
        self.manager.current = 'screen5'

class ScreenFive(Screen, BoxLayout):
    fifth_screen = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(ScreenFive,self).__init__(**kwargs)

    def change(self,*args):
        self.manager.current = 'screen1'

class AddLocationForm(BoxLayout):
    def __init__(self, **kwargs):
        super(AddLocationForm,self).__init__(**kwargs)

class TestApp(App):
    def on_pause(self):
        pass


    def on_resume(self):
        return True
    def build(self):
        self.title = 'unIBOOk! :-)'
        my_screenmanager = ScreenManager()
        screen1 = ScreenOne(name='screen1')
        screen2 = ScreenTwo(name='screen2')
        screen3 = ScreenThree(name = 'screen3')
        screen4 = ScreenFour(name = 'screen4')
        screen5 = ScreenFive(name = 'screen5')
        my_screenmanager.add_widget(screen1)
        my_screenmanager.add_widget(screen2)
        my_screenmanager.add_widget(screen3)
        my_screenmanager.add_widget(screen4)
        my_screenmanager.add_widget(screen5)
        return my_screenmanager


if __name__ == '__main__':
    from kivy.core.window import Window
    from kivy.utils import get_color_from_hex
    Window.clearcolor = get_color_from_hex('#008CD4')
    LabelBase.register(name='Roboto',
                       fn_regular='Roboto-Thin.ttf',
                       fn_bold= 'Roboto-Medium.ttf',
                       )

    LabelBase.register(name='Modern Pictograms',
                       fn_regular='modernpics.ttf',
                    )

    LabelBase.register(name='Heydings',
                       fn_regular='heydings_icons.ttf',
                    )

    TestApp().run()


