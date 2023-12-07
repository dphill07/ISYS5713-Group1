import os
import time
import random
import imageio
from PIL import Image
import numpy as np
import sys, requests
from utils import text_print_utils as utils
from utils.text_print_options import PrintOptions, Term

def restore_db():
    url = f"{api_url_base}/config/reset_database"
    response = requests.put(url)
    if response.status_code == 200:
        utils.print_text("Heroes have been brought back to this Universe.")
    else:
        utils.print_text(f"Error: {response.status_code}")

def run(base_url):
    global api_url_base
    api_url_base = base_url

    print_options = PrintOptions(border_marker_color=Term.BLUE, line_divider_color=Term.BLUE)
    utils.print_text_block("THANOS SNAP", bottom_border = False, options=print_options)

    utils.print_text_block("Thanos has snapped his fingers. Half of the heroes have been deleted from the Universe.", bottom_border = False, options=print_options)
    quit = False
    while  not quit:
        utils.print_text_block("Would you like to bring them back?", bottom_border = False, options=print_options)

        utils.print_divider(options=print_options)

        user_input = utils.get_input("Enter 'yes' or 'no': ")

        if user_input.lower() == 'yes':
            restore_db()
            quit = True
        elif user_input.lower() == 'no':
            utils.print_text("Alright, they won't be back.")
            quit = True
        else:
            utils.print_text("Invalid input. The database will not be restored.")

        utils.print_divider(options=print_options)