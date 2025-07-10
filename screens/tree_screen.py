from kivy.uix.widget import Widget

from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDButtonText, MDFabButton
from kivymd.uix.divider import MDDivider
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogSupportingText, MDDialogContentContainer, MDDialogButtonContainer, MDDialogIcon

from tree import Tree

fonts = {
    "copernicus": "fonts/CopernicusTrial-BookItalic.ttf",
    "georgia": "fonts/Georgia.ttf",
    "antiqua": "C:/Windows/Fonts/AntQuaI.ttf",
    "book": "C:/Windows/Fonts/BookOsI.ttf",
    "bodoni": "C:/Windows/Fonts/Bod_I.ttf",
    "bell": "C:/Windows/Fonts/BellI.ttf",
    "californian": "C:/Windows/Fonts/CalifI.ttf",
    "calisto": "C:/Windows/Fonts/CalistI.ttf",
    "century": "C:/Windows/Fonts/SchlBkI.ttf",
    "century": "C:/Windows/Fonts/SchlBkI.ttf", # *
    "cooper": "C:/Windows/Fonts/CoopBl.ttf",
    "garamond": "C:/Windows/Fonts/GaraIT.ttf",
    "goudy": "C:/Windows/Fonts/GoudOsI.ttf", # *
    "high tower": "C:/Windows/Fonts/HTowerTI.ttf",
    "palatino": "C:/Windows/Fonts/PalaI.ttf", # *
    "perpetua": "C:/Windows/Fonts/Peri____.ttf", # *
    "times": "C:/Windows/Fonts/TimesI.ttf", # *
    "minion": "C:/Users/Solis/Downloads/MinionPro-It.otf", # *
    "minion rm": "C:/Users/Solis/Downloads/MinionPro-Regular.otf", # *
}

class TreeLayout(MDBoxLayout):
    def __init__(self, tree, *args, depth=1, **kwargs):
        super().__init__(
            size_hint=(0.8, 0.8),
            pos_hint={"center_x": .5, "center_y": .5},
            orientation='vertical',
            )

        self.tree = tree
        self.depth = depth

        self.titulo = Título(tree.node)
        self.add_widget(self.titulo)

        self.stack = MDStackLayout(spacing=(0,10))
        self.add_widget(self.stack)

        self.typeset(clear=False)

    def typeset(self, clear=True):
        if clear:
            self.stack.clear_widgets()

        for n,p,l in self.tree.leaf_pairs:
            match l:
                case str():
                    for l in l.split():
                        self.stack.add_widget(Palavra(l, p, level=n))
                case Tree():
                    self.stack.add_widget(Link(l, p, level=n))

class Título(MDLabel):
    def __init__(self, texto, *args, **kwargs):
        super().__init__(text=texto, *args, **kwargs)
        self.pos_hint = {"center_x": 0.5, "center_y": .5}
        self.font_style = 'Body'
        self.halign = 'center'
        self.font_size = 60
        self.font_name = fonts["times"]

class Fechável():
    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return False

        if not touch.is_double_tap:
            print("A")
            if hasattr(self, 'on_press'):
                print("B")
                self.on_press()
            return False

        # if the touch collides with our widget, let's grab it
        touch.grab(self)
        print('okay')

        self.fecha()

        # and accept the touch.
        return True

    def fecha(self):
        self.pai.expanded = False
        self.parent.parent.typeset()

class Palavra(Fechável, MDLabel):
    def __init__(self, texto, pai, level, *args, **kwargs):
        super().__init__(text=texto, *args, **kwargs)
        self.pai = pai
        self.level = level
        self.pos_hint = {"center_x": 0.5, "center_y": .5}
        self.adaptive_width = True
        self.size_hint_y = None
        self.height = 50
        self.color = (0,0,0)
        self.padding_x = 5
        self.font_size = 24
        self.font_name = fonts["minion rm"]
        self.md_bg_color = (1, 0, 0, 1 - 0.97**(1.0*self.level + 1))
        self.radius = 15, 15

class Link(Fechável, MDButton):
    def __init__(self, tree, pai, level, *args, **kwargs):
        texto = MDButtonText(text=tree.node, italic=True)
        texto.font_name = fonts['minion']
        texto.font_size = 24
        super().__init__(texto, *args, **kwargs)
        self.tree = tree
        self.pai = pai
        self.level = level
        self.texto = texto
        self.style = "elevated"
        self.pos_hint = {"center_x": 0, "center_y": .5}
        self.on_press = self.abre
    
    def integra(self, *args, **kwargs):
        self.tree.expanded = True
        self.parent.parent.typeset()
        self.dialog.dismiss()

    def abre(self):
        t = TreeLayout(self.tree, depth=self.parent.parent.depth+1,)
        t.add_widget(MDFabButton(icon='pencil-outline', pos_hint={'center_x': 1.02}, on_press=self.integra))
        t.add_widget(Widget(size_hint=(None, 0.2)))
        d = MDDialog(
            t,
            orientation='vertical',
            size_hint=[0.9**self.parent.parent.depth, 0.9**self.parent.parent.depth],
        )
        d.open()
        self.dialog = d

class TreeScreen(MDScreen):
    def __init__(self, path, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = self.theme_cls.surfaceColor
        tree = Tree.parse(path)
        self.layout = TreeLayout(tree)
        self.add_widget(self.layout)
