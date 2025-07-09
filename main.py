from sys import argv
from kivymd.app import MDApp
from screens.tree_screen import TreeScreen

class MainApp(MDApp):
    def __init__(self, path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = path

    def build(self):
        self.theme_cls.primary_palette = "Red"
        return TreeScreen(self.path)

if __name__=='__main__':
    path = argv[1]
    MainApp(path).run()
