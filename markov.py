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
year = None

periods = ['born', 'toddler', 'earlylife', 'teen', 'youngadult', 'adult', 'elderly']
current_period = periods[0]


# Updates the story depending on which period the program is up to.
def updateStory(current_year):
    global year, current_period
    year = current_year
    # if year in range(0, 2):
    if year in range(0, 2):
        current_period = periods[0]
        templateStory(current_period)
    elif year in range(2, 5):
        current_period = periods[1]
        templateStory(current_period)
    elif year in range(5, 12):
        current_period = periods[2]
        templateStory(current_period)
    elif year in range(12, 18):
        current_period = periods[3]
        templateStory(current_period)
    elif year in range(18, 30):
        current_period = periods[4]
        templateStory(current_period)
    elif year in range(30, 50):
        current_period = periods[5]
        templateStory(current_period)
    else:
        current_period = periods[6]
        templateStory(current_period)


model = None


# Function that opens the specific period markov.txt file
def templateStory(period):
    global model, story, current_string, duplicate
    name = gui.name
    with open("texts/{}.txt".format(period), encoding="utf8") as f:
        period = f.read()
        model = markovify.Text(period, state_size=2)

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

    story += current_string + "\n"
