import flet as ft
import math

# --- LOGIKA MATEMATYCZNA ---
def calculate_distance(lat1, lon1, lat2, lon2):
    # Prostsza wersja dystansu (dla małych odległości można użyć Pitagorasa)
    # Dla precyzji używamy wzoru Haversine
    R = 6371000  # Promień ziemi w metrach
    # ... (tutaj obliczenia) ...
    return distance_in_meters

# --- LOGIKA "TEMPERATURY" ---
def get_status(distance):
    if distance < 5:
        return "MAM CIĘ!", "red"
    elif distance < 15:
        return "GORĄCO!", "orange"
    elif distance < 40:
        return "CIEPŁO", "yellow"
    else:
        return "ZIMNO...", "blue"

# --- INTERFEJS UŻYTKOWNIKA (UI) ---
def main(page: ft.Page):
    page.title = "Chowany GPS"
    
    status_text = ft.Text("Szukanie znajomych...", size=30)
    distance_display = ft.Text("Dystans: -- m")

    def update_game():
        # 1. Pobierz GPS znajomego z serwera
        # 2. Pobierz GPS Twojego telefonu
        # 3. Oblicz dystans
        # 4. Odśwież UI
        pass

    page.add(status_text, distance_display)

ft.app(target=main)