import requests
import json
from utils import text_print_utils as utils
from utils.text_print_options import PrintOptions, Term
from views import hero_view, snap_view2, restoredb


api_url_base = "http://localhost:5000/"

index = 0

menu_options = ["1. Show Heroes", "2. Thanos Snap","3. Bring Heroes Back","0. Quit"]

def run_system():
    utils.print_text_block(header="Group 1's Superhero API Viewer", text="Main Menu", bottom_border=False)

    while True:
        utils.print_text_block("Options:", menu_options)
        user_input = input("Enter a command: ")

        if user_input == "1":
            hero_view.display_heroes(api_url_base)
        elif user_input == "2":
            snap_view2.run(api_url_base)
        elif user_input == "3":
            restoredb.run(api_url_base)
        # elif user_input == "4":
            # organization_view.run(api_url_base)
        # elif user_input == "5":
            # department_view.run(api_url_base)

        elif user_input == "0":
            utils.print_text("Exiting the system.")
            break
        else:
            print("Invalid command. Please try again.")

        utils.print_text_block("Main Menu", top_border=True, bottom_border=False)

run_system()