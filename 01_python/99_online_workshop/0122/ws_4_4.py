dummy_data = [
    {'company': 'Deckow-Crist',
     'lat': '-43.9509',
     'lng': '-34.4618',
     'name': 'Ervin Howell'},
    {'company': 'Romaguera-Jacobson',
     'lat': '-68.6102',
     'lng': '-47.0653',
     'name': 'Clementine Bauch'},
    {'company': 'Keebler LLC',
     'lat': '-31.8129',
     'lng': '62.5342',
     'name': 'Chelsey Dietrich'},
    {'company': 'Considine-Lockman',
     'lat': '-71.4197',
     'lng': '71.7478',
     'name': 'Mrs. Dennis Schulist'},
    {'company': 'Johns Group',
     'lat': '24.8918',
     'lng': '21.8984',
     'name': 'Kurtis Weissnat'},
    {'company': 'Hoeger LLC',
     'lat': '-38.2386',
     'lng': '57.2232',
     'name': 'Clementina DuBuque'},
]


black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


def create_user(user_data):
    censored_user_list = {}
    for data in user_data:
        censored_user_list.get(data['company'], [])
        # .append(data['name'])


def censorship():
    pass
