__author__ = "James Clark"
__credits__ = ["James Clark"]
__version__ = "1.0"

# Import libraries
import random
import gui
import markov

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
location = {'United Kingdom': [['London', 'Canterbury', 'Oxford', 'Manchester'], ['0.7']],
            'USA': [['New York', 'Los Angeles', 'San Fransisco'], ['0.8']],
            'Japan': [['Tokyo', 'Kyoto', 'Osaka'], ['0.8']],
            'Germany': [['Berlin', 'Munich', 'Frankfurt'], ['0.8']],
            'France': [['Paris', 'Nice', 'Lyon'], ['0.7']],
            'China': [['Beijing', 'Shanghai', 'Shenzhen'], ['0.6']]}

starting_city = ''
starting_location = ''
health_system = 0


# Initializes the country where the character is from.
# Randomly select a starting city for the character to begin.
def initializeCountry():
    global starting_city, starting_location, health_system
    # List of countries that can be chosen
    countries = ['United Kingdom', 'USA', 'Japan', 'Germany', 'France', 'China']
    random_value = random.randint(0, len(countries))
    # Stores the country in a variable based on the random value
    starting_location = countries[random_value - 1]
    # Stores all cities for that country
    cities = location.get(starting_location)[0]
    random_value = random.randint(0, len(cities))
    # Stores a city based on the country and their list items randomly
    starting_city = cities[random_value - 1]
    # Stores the health_system for the chosen country
    health_system = [location.get(starting_location)[1]]
    # Converts the list item into a floating point
    x = list(map(str, health_system[0]))
    health_system = float(x[0])


age = 1


personal_health = 1
chance_of_death = 0
wealth = 0
occupation = None
relationship = None


def characterInfo():
    global age
    age = gui.year
    # Storing the characters information in a dictionary to be accessed
    character = {'name': gui.name, 'age': age, 'country': starting_location, 'city': starting_city,
                 'health_system': health_system, 'personal_health': personal_health,
                 'COD': chance_of_death, 'wealth': wealth,
                 'occupation': occupation,
                 'parents': [characters['character_one'], characters['character_two']],
                 'relationship': relationship,
                 'period': markov.current_period
                 }
    print(character)

# TODO: Saving information about the story to a list (dict?), so the markov chains can use it in future to improve
#  the story.
