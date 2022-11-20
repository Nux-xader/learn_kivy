from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

# Window.size = (400, 720)


# class Grid(GridLayout):
#     def __init__(self, **kwargs):
#         super(Grid, self).__init__(**kwargs)
#         self.cols = 1

#         self.inside = GridLayout()
#         self.inside.cols = 2

#         self.inside.add_widget(Label(text="Name: "))
#         self.name = TextInput(multiline=False)
#         self.inside.add_widget(self.name)

#         self.inside.add_widget(Label(text="Address: "))
#         self.address = TextInput(multiline=False)
#         self.inside.add_widget(self.address)

#         self.inside.add_widget(Label(text="Email: : "))
#         self.email = TextInput(multiline=False)
#         self.inside.add_widget(self.email)

#         self.add_widget(self.inside)

#         self.submit = Button(text="Submit")
#         self.submit.bind(on_press=self.pressed)
#         self.add_widget(self.submit)
    
#     def pressed(self, instance):
#         name = self.name.text
#         address = self.address.text
#         email = self.email.text

#         self.name.text = ""
#         self.address.text = ""
#         self.email.text = ""

#         print(name)
#         print(address)
#         print(email)



class KvGrid(Widget):
    name = ObjectProperty(None)
    address = ObjectProperty(None)

    def btn(self):
        print(self.name.text, self.address.text)
        self.name.text = ""
        self.address.text = ""

def other_btn(instance):
    print("Clicked")


class Root(App):
    def build(self):
        self.load_kv('ui.kv')
        return KvGrid()

if __name__ == "__main__":
    Root().run()