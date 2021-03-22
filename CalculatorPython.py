from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

class CalcApp(App):

    def build(self):
        self.formula = "0"
        bl = BoxLayout (orientation = 'vertical', padding =25)
        gl = GridLayout(cols = 4, spacing=2, size_hint = (1, .7), )

        self.lbl = Label(text="0", font_size = 40, halign = "right", size_hint =(1, .4))
        bl.add_widget(self.lbl)

        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Button(text="Clean", on_press = self.clean))

        gl.add_widget(Button(text="7", on_press = self.add_nomber))
        gl.add_widget(Button(text="8", on_press = self.add_nomber))
        gl.add_widget(Button(text="9", on_press = self.add_nomber))
        gl.add_widget(Button(text="X", on_press = self.add_operation))

        gl.add_widget(Button(text="4", on_press = self.add_nomber))
        gl.add_widget(Button(text="5", on_press = self.add_nomber))
        gl.add_widget(Button(text="6", on_press = self.add_nomber))
        gl.add_widget(Button(text="-", on_press = self.add_nomber))

        gl.add_widget(Button(text="1", on_press = self.add_nomber))
        gl.add_widget(Button(text="2", on_press = self.add_nomber))
        gl.add_widget(Button(text="3", on_press = self.add_nomber))
        gl.add_widget(Button(text="+", on_press = self.add_operation))

        gl.add_widget(Button(text="0", on_press = self.add_operation))
        gl.add_widget(Button(text = "/", on_press = self.add_operation))
        gl.add_widget(Button(text=".", on_press = self.add_operation))
        gl.add_widget(Button(text="=", on_press = self.cal_result))

        bl.add_widget(gl)

        return bl

    def update_label(self):
        self.lbl.text =self.formula    

    def add_nomber(self, instance):
        if (self.formula == "0"):
            self.formula = ""

        self.formula += str(instance.text)
        self.update_label()

    def add_operation (self, instance):
        if( str(instance.text).lower() == "x"):
            self.formula+="*"
        else:    
            self.formula += str(instance.text)
        self.update_label()

    def cal_result (self, instance):
        try:
            self.lbl.text= str(eval(self.lbl.text))
        except ZeroDivisionError:
            self.lbl.text="На 0 не делится"    
        self.formula="0"

    def clean (self, instance):
        self.formula="0"
        self.update_label()        

if __name__ == "__main__":
    Window.clearcolor = (0, 0, 0.5, 1) 
    CalcApp().run()