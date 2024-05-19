from rickandmorty import Character
import csv

def save_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

# Obtém todos os personagens
all_characters = Character.get_all_characters()

# Salva os personagens em um arquivo CSV
save_csv('characters.csv', all_characters)
