import argparse
import itertools
import string

# Create the parser
cli = argparse.ArgumentParser(description="Create list of existing 4 letter/character usernames on Instagram")

# Add the parser arguments
cli.add_argument("--disable-letters", dest="letters", store="store_false")
def create_list():
    # Create list of alphabet characters
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)

    # Create list of numbers 0-9
    num_list = list(range(0,10))
