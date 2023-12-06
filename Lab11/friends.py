FRIENDS = {
    "Albert": ["Egbert", "Victor"],
    "Egbert": ["Albert", "Farrah", "Qani"],
    "Farrah": ["Egbert", "Ichabod", "Victor"],
    "Ichabod": ["Qani", "Farrah", "Victor"],
    "Kamala": [],
    "Qani": ["Egbert", "Ichabod", "Vicotr"],
    "Victor": ["Albert", "Ichabod", "Farah", "Qani"]
}

PEOPLE = ['Albert', 'Bethany', 'Chandra', 'Dorothy', 'Egbert',
          'Farrah', 'Gikuyu', 'Horace', 'Ichabod', 'Jane',
          'Kamala', 'Langston', 'Minerva', 'Nestor', 'Olajuwan',
          'Piotr', 'Qani', 'Rakesh', 'Soren', 'Tilde', 'Ursula',
          'Victor', 'Winston', 'Xavier', 'Yolanda', 'Zoe']


for key in FRIENDS:
    print(key)

for value in FRIENDS.values():
    print(value)

for entry in FRIENDS.items():
    print(f"{entry[0]}: {entry[1]}")