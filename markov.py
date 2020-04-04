__author__ = "James Clark"
__credits__ = ["James Clark"]
__version__ = "1.0"

# Import necessary libraries
import random
import markovify
import gui

current_string = ''
story = ''
current_year_story = ''
duplicate = False


def getRandomName(counter):
    # Stores a list of names from first-names.txt
    names_file = open("data/first-names.txt", 'r', encoding="utf8")
    names = names_file.readlines()
    name_list = []
    chosen_names = []

    # Adds all names to a list
    for line in names:
        values = [line.strip()]
        name_list.append(values)

    # Depending on counter specified in gui, choose random name from the names list and add it to chosen names.
    # Replaces the rejected characters with null
    # Chooses a random name based on the a random, length of the names list.
    for i in range(counter):
        random_value = random.randint(0, len(name_list))
        convert_name = str(name_list[random_value])
        chosen_names.append(convert_name.replace("'", "").replace("[", "").replace("]", ""))

    setStoryNames(chosen_names)


# Same function as above but for locations
def getRandomLocations(counter):
    location_file = open("data/locations.txt", 'r', encoding="utf8")
    locations = location_file.readlines()
    location_list = []
    chosen_locations = []

    for line in locations:
        values = [line.strip()]
        location_list.append(values)

    for i in range(counter):
        random_value = random.randint(0, len(location_list))
        convert_name = str(location_list[random_value])
        chosen_locations.append(convert_name.replace("'", "").replace("[", "").replace("]", ""))

    setLocationName(chosen_locations)


def setLocationName(location):
    location_one = location[0]
    location_two = location[1]
    print("Location one: " + location_one)
    print("Location two: " + location_two)


def setStoryNames(names):
    family_one = names[0]
    family_two = names[1]
    friend_one = names[2]
    friend_two = names[3]
    relationship = names[4]
    # Prints out the randomly generated names.
    print("Family one: " + family_one)
    print("Family two: " + family_two)
    print("Friend one: " + friend_one)
    print("Friend two: " + friend_two)
    print("Relationship: " + relationship)


def updateStory(year):
    global current_string
    global current_year_story
    global story
    global duplicate

    # if year in range(0, 2):
    with open("texts/born.txt", encoding="utf8") as f:
        born = f.read()
        model = markovify.Text(born, state_size=2)

    # if year in range(2, 5):
    # print("Early Life")

    # if year in range(5, 12):
    # print("Childhood")

    # if year in range(12, 18):
    # print("Teenage Years")

    # if year in range(18, 30):
    # print("Early Adulthood")

    # if year in range(30, 50):
    # print("Adulthood")

    # if year in range(50, 1000):
    # print("Older")

    name = gui.name

    current_year_story = ''

    # Creates three sentences from markov chain
    start_sentence_one = model.make_short_sentence(150, tries=100)
    start_sentence_two = model.make_short_sentence(150, tries=100)
    start_sentence_three = model.make_short_sentence(150, tries=100)

    # Conditionals to make sure generated text is not duplicated in the year story.
    if start_sentence_one == start_sentence_two or start_sentence_one == start_sentence_three:
        duplicate = True
        updateStory(year)

    elif start_sentence_two == start_sentence_one or start_sentence_two == start_sentence_three:
        duplicate = True
        updateStory(year)

    elif start_sentence_three == start_sentence_one or start_sentence_three == start_sentence_two:
        duplicate = True
        updateStory(year)

    else:
        duplicate = False
        # Current string concatenates the three sentences together
        original_string = start_sentence_one + "\n" + start_sentence_two + "\n" + start_sentence_three
        current_string = original_string.replace("Name", name)

        # Story adds all current strings together
        story += current_string + "\n"
