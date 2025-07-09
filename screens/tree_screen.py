
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDButtonText
from tree import Tree

class Palavra(MDLabel):
    def __init__(self, palavra, *args, **kwargs):
        texto = MDButtonText(text=palavra)
        super().__init__(texto, *args, **kwargs)
        self.texto = texto
        self.style = "tonal" # "text"
        self.pos_hint = {"center_x": 0, "center_y": .5}
        self.radius = 0,0,0,0
        #self.width = 0.5*self.width
        #print(f'radius: {self.radius}')

    def __init__(self, texto, *args, **kwargs):
        #texto = MDButtonText(text=palavra)
        super().__init__(text=texto, *args, **kwargs)
        #self.texto = texto
        #self.style = "tonal" # "text"
        self.pos_hint = {"center_x": 0.5, "center_y": .5}
        # self.adaptive_size = True
        self.adaptive_width = True
        # self.size_hint_y = 0.2
        self.size_hint_y = None
        self.height = 50
        self.color = (0,0,0)
        self.padding_x = 5
        #self.radius = 0,0,0,0
        #self.width = 0.5*self.width
        #print(f'radius: {self.radius}')

class Link(MDButton):
    def __init__(self, tree, *args, **kwargs):
        texto = MDButtonText(text=tree.node)
        super().__init__(texto, *args, **kwargs)
        self.tree = tree
        self.texto = texto
        self.style = "elevated"
        self.pos_hint = {"center_x": 0, "center_y": .5}
        self.on_press = self.abre

    def abre(self):
        i = self.parent.children.index(self)
        for l in self.tree.leaves:
            match l:
                case str():
                    for l2 in l.split():
                        self.parent.add_widget(Palavra(l2), i)
                case Tree():
                    self.parent.add_widget(Link(l), i)
        self.parent.remove_widget(self)

class TreeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.md_bg_color = self.theme_cls.surfaceColor
        self.tree = Tree.parse('exemplo2.tree')
        self.layout = MDBoxLayout(size_hint=(0.8, 0.8), pos_hint={"center_x": .5, "center_y": .5}, orientation='vertical')
        self.add_widget(self.layout)
        self.layout.add_widget(MDLabel(text='Photosynthesis', font_style='Display', halign='center'))
        self.sublayout = MDStackLayout(spacing=(0,10))
        self.layout.add_widget(self.sublayout)

        for l in self.tree.leaves:
            match l:
                case str():
                    self.sublayout.add_widget(Palavra(l))
                case Tree():
                    self.sublayout.add_widget(Link(l))