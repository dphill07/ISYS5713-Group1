import requests
import random
from colorama import Fore, Style

def get_heroes():
    api_url = "http://127.0.0.1:5000/heroes"  # Replace with the actual API endpoint
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch heroes. Status code: {response.status_code}")
        return []

def pick_random_heroes(heroes, num_to_pick):
    return random.sample(heroes, min(num_to_pick, len(heroes)))

def display_heroes(heroes, picked_heroes):
    for hero in heroes:
        hero_name = hero["name"]
        color = Fore.GREEN if hero_name in picked_heroes else Fore.RED
        print(f"{color}{hero_name}{Style.RESET_ALL}")

def main():
    all_heroes = get_heroes()
    if not all_heroes:
        return

    num_to_pick = 5
    picked_heroes = pick_random_heroes(all_heroes, num_to_pick)

    print("Picked Heroes:")
    display_heroes(all_heroes, picked_heroes)

if __name__ == "__main__":
    main()
