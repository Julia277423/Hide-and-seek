from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.lang import Builder

Builder.load_string("""
<GameView>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: role_label
            text: "Twoja rola: ?"
        Label:
            id: timer_label
            text: "15:00"
            font_size: 50
        Label:
            id: status_label
            text: "Dystans: Oczekiwanie..."
""")

class GameView(Screen):
    def on_enter(self):
        self.time_left = 900
        Clock.schedule_interval(self.update_game, 1)
        # Tu w przyszłości dodasz nasłuchiwanie GPS

    def update_game(self, dt):
        if self.time_left > 0:
            self.time_left -= 1
            m, s = divmod(self.time_left, 60)
            self.ids.timer_label.text = f"{m:02d}:{s:02d}"
        
        # Przykładowy status (później dane z GPS)
        self.ids.status_label.text = "CIEPŁO..."