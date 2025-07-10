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
    try:
        path = argv[1]
    except IndexError:
        print("\nError: Missing  the *.tree source file.\nUsage: python main.py <source_file>\n")
        exit()
    MainApp(path).run()
