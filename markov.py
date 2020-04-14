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


# TODO: Figure out how to have different markov chains for different year ranges
#   - Fill out these stories
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

# TODO: Split this into its own function, that takes a parameter 'age group' that relates to a story filename.txt

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
