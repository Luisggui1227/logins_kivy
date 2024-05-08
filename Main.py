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

        # Adiciona imagem de fundo
        self.add_widget(Image(source='data:image/jpeg;base64,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', allow_stretch=True, keep_ratio=False))

        # Adiciona logo
        logo_image = Image(source='', size_hint=(None, None), size=(150, 150), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.add_widget(logo_image)

        # Adiciona campos de entrada
        self.username_input = TextInput(hint_text="Nome de usuário", pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(None, None), size=(300, 50))
        self.senha_input = TextInput(hint_text="Senha", password=True, pos_hint={'center_x': 0.5, 'center_y': 0.4}, size_hint=(None, None), size=(300, 50))
        self.add_widget(self.username_input)
        self.add_widget(self.senha_input)

        # Adiciona botões
        self.cadastrar_button = Button(text="Cadastrar", background_color=(0.1, 0.5, 0.8, 1), pos_hint={'center_x': 0.3, 'center_y': 0.3}, size_hint=(None, None), size=(150, 50))
        self.cadastrar_button.bind(on_press=self.cadastrar_usuario)
        self.login_button = Button(text="Entrar", background_color=(0.1, 0.7, 0.3, 1), pos_hint={'center_x': 0.7, 'center_y': 0.3}, size_hint=(None, None), size=(150, 50))
        self.add_widget(self.cadastrar_button)
        self.add_widget(self.login_button)
        self.mensagem_label = Label(text="", pos_hint={'center_x': 0.5, 'center_y': 0.2}, size_hint=(None, None), size=(400, 50))
        self.add_widget(self.mensagem_label)
    def cadastrar_usuario(self, instance):
        self.mensagem_label.text = "Usuário cadastrado"

class MyApp(App):
    def build(self):
        return Login()

if __name__ == '__main__':
    MyApp().run()
