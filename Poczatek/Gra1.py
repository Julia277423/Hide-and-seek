import math

def calculate_distance(lat1, lon1, lat2, lon2):
    # Promień Ziemi w kilometrach
    R = 6371.0
    
    # Zamiana stopni na radiany
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    # Wzór Haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distance = R * c
    return distance # wynik w kilometrach

# Przykład działania:
seeker_pos = (52.2297, 21.0122) # Warszawa
hider_pos = (52.2350, 21.0150)  # Okolice

dist = calculate_distance(seeker_pos[0], seeker_pos[1], hider_pos[0], hider_pos[1])

if dist < 0.1:
    print("WRZĄTEK! (poniżej 100m)")
elif dist < 0.5:
    print("GORĄCO! (poniżej 500m)")
else:
    print(f"ZIMNO... ({dist:.2f} km)")