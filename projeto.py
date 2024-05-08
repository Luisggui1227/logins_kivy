from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Rectangle

class Login(RelativeLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_ui()

    def setup_ui(self):
        # Adiciona fundo gradiente
        with self.canvas.before:
            Color(0.8, 0.8, 0.8, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Adiciona imagem de fundo
        self.add_widget(Image(source='data:image/jpeg;base64,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', allow_stretch=True, keep_ratio=False))

        # Adiciona logo
        logo_image = Image(source='logo.png', size_hint=(None, None), size=(150, 150), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.add_widget(logo_image)

        # Adiciona campos de entrada
        self.username_input = TextInput(hint_text="Nome de usuário", pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(None, None), size=(300, 50))
        self.senha_input = TextInput(hint_text="Senha", password=True, pos_hint={'center_x': 0.5, 'center_y': 0.4}, size_hint=(None, None), size=(300, 50))
        self.add_widget(self.username_input)
        self.add_widget(self.senha_input)

        # Adiciona botões
        self.cadastrar_button = Button(text="Cadastrar", background_color=(0.1, 0.5, 0.8, 1), pos_hint={'center_x': 0.3, 'center_y': 0.3}, size_hint=(None, None), size=(150, 50))
        self.login_button = Button(text="Entrar", background_color=(0.1, 0.7, 0.3, 1), pos_hint={'center_x': 0.7, 'center_y': 0.3}, size_hint=(None, None), size=(150, 50))
        self.add_widget(self.cadastrar_button)
        self.add_widget(self.login_button)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class MyApp(App):
    def build(self):
        return Login()

if __name__ == '__main__':
    MyApp().run()
