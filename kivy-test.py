from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MainApp(MDApp):
    def build(self):
        return MDLabel(text="Photosynthesis is how plants make food.", halign="center")

MainApp().run()