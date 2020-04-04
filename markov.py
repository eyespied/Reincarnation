__author__ = "James Clark"
__credits__ = ["James Clark"]
__version__ = "1.0"

# Import necessary libraries
import markovify

import gui

current_string = ''
story = ''
current_year_story = ''
duplicate = False


def startStory():
    global current_string
    global current_year_story
    global story
    global duplicate

    with open("texts/born.txt", encoding="utf8") as f:
        born = f.read()

    born_model = markovify.Text(born, state_size=2)
    name = gui.name

    current_year_story = ''

    # Creates three sentences from markov chain
    start_sentence_one = born_model.make_short_sentence(150, tries=100)
    start_sentence_two = born_model.make_short_sentence(150, tries=100)
    start_sentence_three = born_model.make_short_sentence(150, tries=100)

    # Conditionals to make sure generated text is not duplicated in the year story.
    if start_sentence_one == start_sentence_two or start_sentence_one == start_sentence_three:
        duplicate = True
        startStory()

    elif start_sentence_two == start_sentence_one or start_sentence_two == start_sentence_three:
        duplicate = True
        startStory()

    elif start_sentence_three == start_sentence_one or start_sentence_three == start_sentence_two:
        duplicate = True
        startStory()

    else:
        duplicate = False
        # Current string concatenates the three sentences together
        original_string = start_sentence_one + "\n" + start_sentence_two + "\n" + start_sentence_three
        current_string = original_string.replace("Name", name)

        # Story adds all current strings together
        story += current_string + "\n"


def updateStory():
    print("test")
