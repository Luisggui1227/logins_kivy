from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout

class Login(RelativeLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.add_widget(Image(source='data:image/png;base64,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',
                               size_hint=(None, None), size=(70, 70), pos_hint={'center_x': 0.5, 'center_y': 0.9}))
        
        self.add_widget(Label(text="LOGIN", font_size=30, pos_hint={'center_x': 0.5, 'center_y': 0.8}))

        self.username_input = TextInput(hint_text="Nome de usuário ...", pos_hint={'center_x': 0.5, 'center_y': 0.6}, size_hint=(None, None), size=(200, 50))
        self.senha_input = TextInput(hint_text="Digite sua senha ...", password=True, pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(None, None), size=(200, 50))

        self.add_widget(Label(text="Nome de usuário:", pos_hint={'center_x': 0.5, 'center_y': 0.7}))
        self.add_widget(self.username_input)
        self.add_widget(Label(text="Senha:", pos_hint={'center_x': 0.5, 'center_y': 0.4}))
        self.add_widget(self.senha_input)

        self.cadastrar_button = Button(text="Cadastrar", background_color=(0, 0, 0.75), pos_hint={'center_x': 0.5, 'center_y': 0.3}, size_hint=(None, None), size=(150, 50))
        self.login_button = Button(text="Já possuo uma conta", background_color=(0, 0, 10), pos_hint={'center_x': 0.5, 'center_y': 0.2}, size_hint=(None, None), size=(150, 50))
        self.add_widget(self.cadastrar_button)
        self.add_widget(self.login_button)

class MyApp(App):
    def build(self):
        return Login()

if __name__ == '__main__':
    MyApp().run()
