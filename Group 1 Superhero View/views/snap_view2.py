import os
import time
import random
import imageio
from PIL import Image
import numpy as np
import sys, requests
from utils import text_print_utils as utils
from utils.text_print_options import PrintOptions, Term
import aiohttp
import asyncio

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display a frame in the terminal
def display_frame(frame_str):
    clear_screen()
    print("Thanos is about to snap...\n{}".format(frame_str))
    time.sleep(0.1)

# Function to convert a frame to grayscale
def convert_frame_to_grayscale(frame):
    grayscale_frame = ""
    for row in frame:
        for pixel in row:
            # Choose a character based on pixel intensity
            intensity = sum(pixel) / 3
            # Adjust the indexing to prevent going out of range
            grayscale_frame += " ░▒▓█"[min(int(intensity / 256 * 5), 4)]
        grayscale_frame += "\n"
    return grayscale_frame

# Function to resize a frame
def resize_frame(frame, new_width, new_height):
    img = Image.fromarray(frame)
    img = img.resize((new_width, new_height))
    return np.array(img)

# Function to fade out text
def fade_out_print(text, duration):
    steps = 10  # Number of steps for the fading effect
    delay = duration / steps

    for i in range(steps + 1):
        alpha = 1 - i / steps
        faded_text = f"\x1b[1;37;48;2;255;255;255;{int(alpha * 255)}m{text}\x1b[0m"  # ANSI escape code for fading
        sys.stdout.write("\r" + faded_text)
        sys.stdout.flush()
        time.sleep(delay/100)

    sys.stdout.write("\r" + " " * len(text))  # Clear the line
    sys.stdout.flush()

# Function to animate the Thanos snap with a gif
def thanos_snap_gif_animation():

    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Provide the absolute path on Windows
    gif_path = os.path.join(current_directory, "snap2.gif")
    target_width, target_height = 55, 20  # Set the desired width and height

    gif = imageio.get_reader(gif_path)
    frames = [frame[:, :, :] for frame in gif]  # Extract frames without resizing

    for frame in frames:
        resized_frame = resize_frame(frame, target_width, target_height)
        grayscale_frame_str = convert_frame_to_grayscale(resized_frame)
        display_frame(grayscale_frame_str)

# Function to perform the Thanos snap
async def thanos_snap_async(all_heroes):
    thanos_snap_gif_animation()

    # Copy the list to track disappeared items
    disappeared_items = all_heroes.copy()

    # Rest of the snap logic
    remaining_percentage = 0.5
    remaining_count = int(len(all_heroes) * remaining_percentage)
    remaining_elements = random.sample(all_heroes, remaining_count)

    # Identify disappeared items
    for item in remaining_elements:
        disappeared_items.remove(item)

    # Display the fading-out effect for disappeared items
    print("\nHeroes that have disappeared:")
    for item in disappeared_items:
        fade_out_print(item, duration=2)  # Adjust duration as needed

    async with aiohttp.ClientSession() as session:
        tasks = [delete_hero_by_id_async(session, get_hero_id(item, all_heroes)) for item in disappeared_items]
        deleted_results = await asyncio.gather(*tasks)

    # Display the remaining elements without fading effect
    print("\nSurvivors after Thanos Snap:")
    for item in remaining_elements:
        print(item)
    
    print("\nThanos has snapped! Changes have taken place, and a new reality awaits.")

def get_hero_id(hero_name, all_heroes):
    if isinstance(all_heroes[0],dict):
        for hero in all_heroes:
            if hero['hero_name'] == hero_name:
                return hero['hero_id']
    elif isinstance(all_heroes[0],str):
        try:
            return all_heroes.index(hero_name)
        except ValueError:
            return None
    return None

async def delete_hero_by_id_async(session, hero_id):

    url = f"{api_url_base}/heroes/{hero_id}"
    async with session.delete(url) as response:
        # Return True if the deletion is successful (status code 204), otherwise False
        return response.status == 204
    


def get_all_heroes():
    url = f"{api_url_base}/heroes"

    limit = 750
    params = {'limit': limit}
    data = {}
    response = requests.get(url, params=params, data=data)

    if response.status_code == 200:
        heroes = response.json()
        if len(heroes) == 0:
            print("No heroes found.")
            return
        
        
        return heroes
    
    else:
        print(f"Error: {response.status_code}")
        return None

def filter_heroes_variables():
    
    heroes = get_all_heroes()
    all_heroes = []

    if heroes is not None:
        for hero in heroes:
            all_heroes.append(hero['hero_name'])

    return all_heroes


def run(base_url):
    global api_url_base
    api_url_base = base_url

    print_options = PrintOptions(border_marker_color=Term.BLUE, line_divider_color=Term.BLUE)
    utils.print_text_block("THANOS SNAP", bottom_border = False, options=print_options)

    menu_options = ["Are you sure you want to snap your fingers?", "1.Yes", "2.No"]
    quit = False
    while not quit:
        utils.print_text_block("Menu Options:", menu_options, options=print_options)
        user_input = utils.get_input("Enter a command: ")

        if user_input == "1":
            warningmessage = "Warning: Initiating the snap effect will result in significant changes. Be prepared for a transformation. Your current state will be altered irreversibly. Are you sure you want to proceed?\n\nRemember: with great power comes great responsibility.\n 1.Proceed\n 2.Cancel"
            utils.print_text_block("Important Message: Before You Snap!",warningmessage, bottom_border = False, options=print_options)
            user_input = utils.get_input("Enter a command: ")
            if user_input == "1":
                result = filter_heroes_variables()
                asyncio.run(thanos_snap_async(result))
                quit = True
            elif user_input == "2":
                utils.print_text("Your decision to cancel the snap effect has been acknowledged. Wise choice! If you have any further questions or concerns, feel free to explore other features or contact support. Thank you for your discretion.")
                quit = True
            else:
                utils.print_text("Invalid command. Please try again.")
        
        elif user_input == "2":
            utils.print_text("Exiting the system.")
            quit = True
        else:
            utils.print_text("Invalid command. Please try again.")












