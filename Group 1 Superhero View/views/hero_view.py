import requests
import threading
import time
import concurrent.futures
from utils import text_print_utils as utils
from utils.text_print_options import PrintOptions, Term

class Power:
    def __init__(self, power_type, power_name, power_level):
        self.power_type = power_type
        self.power_name = power_name
        self.power_level = power_level

def fetch_powers(hero_ids):
    powers_list = []

    def fetch_hero_powers(hero_id):
        url = f"{api_url_base}heroes/{hero_id}/powers"
        response = requests.get(url)
        if response.status_code == 200:
            powers = response.json()
            hero_powers = powers['powers']
            return hero_powers

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_hero_id = {executor.submit(fetch_hero_powers, hero_id): hero_id for hero_id in hero_ids}
        for future in concurrent.futures.as_completed(future_to_hero_id):
            powers = future.result()
            powers_list.append(powers)

    return powers_list
def display_heroes(base_url):
    global api_url_base
    api_url_base = base_url

    print_options = PrintOptions(border_marker_color=Term.BLUE, line_divider_color=Term.BLUE)
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
            utils.print_text("No heroes found.")
            return

        utils.print_divider(options=options)

        displayed_heroes = 0

        def fetch_powers_batch(hero_ids, powers_list):
            powers = fetch_powers(hero_ids)
            powers_list.extend(powers)

        # Fetch powers for the first batch of heroes
        first_hero_ids = [hero['hero_id'] for hero in heroes[0:display_limit]]
        all_powers = []
        fetch_powers_thread = threading.Thread(target=fetch_powers_batch, args=(first_hero_ids, all_powers))
        fetch_powers_thread.start()

        for i in range(0, len(heroes), display_limit):
            hero_batch = heroes[i:i+display_limit]

            # Wait for the powers to be fetched if necessary
            while len(all_powers) < i + display_limit:
                time.sleep(0.1)  # Wait a bit before checking again

            powers_batch = all_powers[i:i+display_limit]

            for hero, powers in zip(hero_batch, powers_batch):

                utils.print_divider(options=options)

                options.alignment = 'center'

                options.text_color = Term.RESET
                utils.print_text(f"Displaying Hero: {hero['hero_name']}", options)

                options.line_divider_char = '-'
                utils.print_divider(options=options)

                utils.print_blank_line(options=options)

                alignment_colors = {
                    'good': Term.GREEN,
                    'bad': Term.RED,
                    'neutral': Term.YELLOW,
                    '': Term.BLUE,  # Use 'blue' for null alignments
                    None: Term.BLUE  # Use 'blue' for null alignments
                }

                alignment_color = alignment_colors[hero['alignment']]
                options.text_color = alignment_color

                ordered_hero_keys = [
                'publisher'
                , 'species'
                , 'alignment'
                , 'eye_color'
                , 'gender'
                , 'hair_color'
                , 'height'
                , 'weight'
                , 'skin_color'
                ]

                rename_hero_keys = {
                'publisher' : 'Publisher'
                , 'species' : 'Species'
                , 'alignment' : 'Alignment'
                , 'eye_color' : 'Eye Color'
                , 'gender' : 'Gender'
                , 'hair_color' : 'Hair Color'
                , 'height' : 'Height'
                , 'weight' : 'Weight'
                , 'skin_color' : 'Skin Color'
                }

                rename_power_keys = {
                'power_type' : 'Power Type'
                , 'power_name' : 'Power Name'
                , 'power_level' : 'Power Level'
                }

                options.tab_spaces = 0
                options.alignment = 'center'

                utils.print_json_in_table_format(hero, ordered_hero_keys, rename_hero_keys, options=options)

                options.text_color = Term.RESET
                # options.alignment = 'center'
                utils.print_text(hero['hero_name'] + "'s Powers", options=options)
                # options.alignment = 'left'
                options.text_color = alignment_color

                # Sort power_list by power_type, then power_name
                sorted_power_list = sorted(powers, key=lambda power: (power['power_type'], power['power_name']))

                # Convert dictionaries to Power objects
                power_objects = [Power(power['power_type'], power['power_name'], power['power_level']) for power in sorted_power_list]

                utils.print_objects_in_table_format(power_objects, rename_power_keys, options=options)

                utils.print_blank_line(options=options)
                utils.print_divider(options=options)


            displayed_heroes += display_limit


            # Fetch powers for the next batch of heroes
            if i + display_limit < len(heroes):
                next_hero_ids = [hero['hero_id'] for hero in heroes[i+display_limit:i+2*display_limit]]
                fetch_powers_thread = threading.Thread(target=fetch_powers_batch, args=(next_hero_ids, all_powers))
                fetch_powers_thread.start()


            user_input = utils.get_input("Press enter to continue or type 'cancel' to stop: ")
            if user_input.lower() == 'cancel':
                break

