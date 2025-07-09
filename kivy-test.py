from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDButtonText #MDFlatButton #, MDButtonIcon, MDButtonText
from kivy.lang import Builder

from screens.tree_screen import TreeScreen

class Palavra(MDButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.style = "elevated"
        self.pos_hint = {"center_x": 0, "center_y": .5}
        self.on_press = self.abre # lambda: print("oi")

    def abre(self):
        self.children[0].text, self.replacement = self.replacement, self.children[0].text
        word = self.children[0].text
        self.width = 30 + 10*len(word)

def button(word, replacement=None):
    s = f'''
            Palavra:
                theme_width: "Custom"
                width: {30 + 10*len(word)} 
                replacement: "{replacement or word}"

                MDButtonText:
                    text: "{word}"
                    pos_hint: {{"center_x": 0.5, "center_y": .5}}
                    # md_bg_color: app.theme_cls.primaryColor
                    id: "texto"
'''
    return s


KV = ('''
MDScreen:
    md_bg_color: app.theme_cls.surfaceColor

    BoxLayout:
        orientation: "vertical"

        MDLabel:
            text: "Título"
            # halign: "center"
            adaptive_size: True
            pos_hint: {"center_x": .5, "center_y": .5}
            padding: "0dp", "20dp"
            font_style: "Display"
            # color: (0,0,0,1)
            color: app.theme_cls.primaryColor
            bold: True

        MDStackLayout:
            # md_bg_color: app.theme_cls.primaryColor
            size_hint: (0.8, 0.8)
            pos_hint: {"center_x": .5, "center_y": .5}
            spacing: (0, 10)

''') + \
'\n'.join((button(word, r) for word, r in zip("Photosyntesis is how plants make food".split(),
                                              ["", "", "a process by which", "green plants", "fabricate", "sugars"])))

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

class MainApp(MDApp):
    def build(self):
        return TreeScreen()


if __name__=='__main__':
    MainApp().run()