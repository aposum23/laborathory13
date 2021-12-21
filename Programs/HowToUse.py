def print_scores(student, *scores):
    print(f'Student Name: {student}')
    for score in scores:
        print(score)

print_scores('Jonathan', 100, 95, 88, 92, 99)


def print_pet_names(owner, **pets):
    print(f'Owner Name: {owner}')
    for pet, name in pets.items():
        print(f'{pet}: {name}')

print_pet_names(
    'Jonathan',
    dog='Brock',
    fish=['Larry', 'Curly', 'Moe'],
    tutrle='Shelldon')
