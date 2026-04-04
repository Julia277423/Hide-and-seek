from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_string("""
<LobbyView>:
    BoxLayout:
        orientation: 'vertical'
        padding: 30
        Label:
            id: info_label
            text: "Lobby"
        Label:
            id: code_display
            text: "KOD: ------"
            font_size: 40
        Button:
            id: start_btn
            text: "START (Tylko Host)"
            disabled: True
            on_release: root.start_game()
""")

class LobbyView(Screen):
    def on_enter(self):
        app = self.manager.app
        if app.is_host:
            code = app.engine.generate_code()
            self.ids.code_display.text = f"KOD: {code}"
            self.ids.start_btn.disabled = False
        else:
            self.ids.info_label.text = "Czekaj na start hosta..."

    def start_game(self):
        self.manager.current = 'game'