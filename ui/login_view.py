from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string("""
<LoginView>:
    BoxLayout:
        orientation: 'vertical'
        padding: 50
        spacing: 20
        Label:
            text: "AUTO-CHOWANY"
            font_size: 32
        TextInput:
            id: nick_input
            hint_text: "Twój Nick"
            multiline: False
            size_hint_y: None
            height: 50
        Button:
            text: "STWÓRZ GRĘ"
            on_release: root.create_game()
        Button:
            text: "DOŁĄCZ DO GRY"
            on_release: root.join_game()
""")

class LoginView(Screen):
    def create_game(self):
        app = self.manager.app
        app.player_nick = self.ids.nick_input.text
        app.is_host = True
        self.manager.current = 'lobby'

    def join_game(self):
        app = self.manager.app
        app.player_nick = self.ids.nick_input.text
        app.is_host = False
        self.manager.current = 'lobby'