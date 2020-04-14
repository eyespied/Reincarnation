__author__ = "James Clark"
__credits__ = ["James Clark"]
__version__ = "1.0"

# Import libraries
import random
import gui

characters = {}


# Chooses random names to populate the dictionary at application start.
# Selects 5 characters for the story.
def initializeCharacters():
    # Stores a list of names from first-names.txt
    names_file = open("data/first-names.txt", 'r', encoding="utf8")
    names = names_file.readlines()
    chosen_names = []
    name_list = []

    # Adds all names to a list
    for line in names:
        values = [line.strip()]
        name_list.append(values)

    # Depending on counter specified in gui, choose random name from the names list and add it to chosen names.
    # Replaces the rejected characters with null
    # Chooses a random name based on the a random, length of the names list.
    for i in range(5):
        random_value = random.randint(0, len(name_list))
        convert_name = str(name_list[random_value])
        chosen_names.append(convert_name.replace("'", "").replace("[", "").replace("]", ""))

    # Adds five random names to a character
    characters['character_one'] = chosen_names[0]
    characters['character_two'] = chosen_names[1]
    characters['character_three'] = chosen_names[2]
    characters['character_four'] = chosen_names[3]
    characters['character_five'] = chosen_names[4]


# Location dictionary
location = {'United Kingdom': ['London', 'Canterbury', 'Oxford', 'Manchester'],
            'USA': ['New York', 'Los Angeles', 'San Fransisco'], 'Japan': ['Tokyo', 'Kyoto', 'Osaka'],
            'Germany': ['Berlin', 'Munich', 'Frankfurt'], 'France': ['Paris', 'Nice', 'Lyon'],
            'China': ['Beijing', 'Shanghai', 'Shenzhen']}

starting_city = ''


# Initializes the country where the character is from.
# Randomly select a starting city for the character to begin.
def initializeCountry():
    global starting_city
    # List of countries that can be chosen
    countries = ['United Kingdom', 'USA', 'Germany', 'China']
    random_value = random.randint(0, len(countries))
    starting_location = countries[random_value - 1]
    cities = location.get(starting_location)
    random_value = random.randint(0, len(cities))
    starting_city = cities[random_value - 1]


age = 0


# TODO: Add additional information to the character:
#   - Health
#   - Friends
#   - Siblings
#   - Occupation
#   - COD (Change of death)
#   - Wealth
#   - Relationship

def characterInfo():
    global age
    age = gui.year
    # Storing the characters information in a dictionary to be accessed
    character = {'name': gui.name, 'age': age, 'location': starting_city, 'parents': [characters['character_one'],
                                                                                      characters['character_two']]}
    print(character)

# TODO: Saving information about the story to a list (dict?), so the markov chains can use it in future to improve
#  the story.
