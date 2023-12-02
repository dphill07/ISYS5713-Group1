import requests
import json
import textwrap
from datetime import datetime
from utils import text_print_utils as utils
from utils.text_print_options import PrintOptions, Term

def display_heroes(base_url):
    global api_url_base
    api_url_base = base_url

    print_options = PrintOptions(border_marker_color=Term.GREEN, line_divider_color=Term.GREEN)
    utils.print_text_block(text="Hero Viewer", bottom_border = False, options=print_options)


    options = print_options
    display_limit = None

    while True:

        utils.print_text_block(text="How many heroes would you like to view at a time? Please enter a whole number.", bottom_border = False, options=options)
        utils.print_divider(options=options)
        user_input = utils.get_input("Enter a number: ")
        try:
            display_limit = int(user_input)
            break
        except:
            print("Invalid input. Please try again.")






    url = f"{api_url_base}heroes"

    limit = 750
    params = {'limit': limit}
    data = {}
    response = requests.get(url, params=params, data=data)

    if response.status_code == 200:
        heroes = response.json()
        if len(heroes) == 0:
            print("No heroes found.")
            return


        utils.print_divider(options=options)


        displayed_heroes = 0
            
        for hero in heroes:
            if displayed_heroes >= display_limit:
                # Add user prompt
                user_input = utils.get_input("Press enter to continue or type 'cancel' to stop: ")
                displayed_heroes = 0
                if user_input.lower() == 'cancel':
                    break




            options.alignment = 'center'
            utils.print_text(f"Displaying Hero: {hero['hero_name']}", options)

            options.line_divider_char = '-'
            utils.print_divider(options=options)

            utils.print_blank_line(options=options)

            ordered_keys = [
            'alignment'
            , 'eye_color'
            , 'gender'
            , 'hair_color'
            , 'height'
            , 'hero_id'
            , 'hero_name'
            , 'publisher'
            , 'skin_color'
            , 'species'
            , 'weight'
            ]

            rename_keys = {
            'alignment' : 'Alignment'
            , 'eye_color' : 'Eye Color'
            , 'gender' : 'Gender'
            , 'hair_color' : 'Hair Color'
            , 'height' : 'Height'
            , 'hero_id' : 'Hero Id'
            , 'hero_name' : 'Hero Name'
            , 'publisher' : 'Publisher'
            , 'skin_color' : 'Skin Color'
            , 'species' : 'Species'
            , 'weight' : 'Weight'
            }


            options.tab_spaces = 0
            options.alignment = 'left'
            utils.print_json_in_table_format(hero, ordered_keys, rename_keys, options=options)


            utils.print_blank_line(options=options)
            utils.print_divider(options=options)

            displayed_heroes += 1








def run(base_url):
    global api_url_base
    api_url_base = base_url

    print_options = PrintOptions(border_marker_color=Term.GREEN, line_divider_color=Term.GREEN)
    utils.print_text_block(text="Hero Viewer", bottom_border = False, options=print_options)

    menu_options = ["1. Display Heroes", "0. Main Menu"]
    quit = False
    while not quit:
        print_options.alignment = 'center'
        utils.print_text_block(header="Options:", text=menu_options, options=print_options)
        user_input = utils.get_input("Enter a command: ")
        # user_input = input("Enter a command: ")

        if user_input == "1":
            display_heroes(print_options)
        # elif user_input == "2":
        #     display_technician_information(print_options)
        # elif user_input == "3":
        #     display_technician_avg_ticket_times(print_options)
        # elif user_input == "4":
        #     display_technician_managers(print_options)
        # elif user_input == "5":
        #     display_ticket_information(print_options)
        elif user_input == "0":
            print("Exiting Hero Viewer.")
            quit = True
        else:
            print("Invalid command. Please try again.")
