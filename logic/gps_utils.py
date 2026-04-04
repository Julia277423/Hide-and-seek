import math

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371000  # Promień Ziemi w metrach
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def get_status_text(distance, is_seeker):
    if is_seeker:
        if distance < 50: return "LODOWATO! (Zaraz go masz)"
        if distance < 200: return "GORĄCO"
        if distance < 500: return "CIEPŁO"
        if distance < 1000: return "ZIMNO"
        return "LODOWATO"
    else:
        return f"Szukający jest {int(distance)}m od Ciebie!"