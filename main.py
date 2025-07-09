from kivymd.app import MDApp
from screens.tree_screen import TreeScreen

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        return TreeScreen()

if __name__=='__main__':
    MainApp().run()