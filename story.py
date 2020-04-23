__author__ = "James Clark"
__credits__ = ["James Clark"]
__version__ = "2.0"

import tracery
from tracery.modifiers import base_english

import gui

final = None
export_story = ''


# Creates rules for the story before creating a story.
def createStory():
    global final, export_story
    rules = {

        # General story attributes
        'character_name': [gui.name],
        'name': ["Bob", "Alice", 'James', 'Lauren'],
        'location': ['London', 'Spain', 'Japan'],
        'health': ['a healthy', 'an unhealthy'],
        'setPronouns': ["'[charThey:she]', '[charThem:her]', '[charTheir:her]', '[charTheirs:hers]'",
                        "'[charThey:he]', '[charThem:him]', '[charTheir:his]', '[charTheirs:his]'"],
        'learning': ['talking', 'walking', 'shouting', 'crawling', 'reading', 'writing'],

        # Emotions
        'emotions': ['happy', 'sad', 'joyful', 'relieved', 'funny', 'surprised', 'angry', 'excited', 'fearful'],
        'parent_reactions': ["#father.capitalize# was very #emotions#.", "#mother.capitalize# was very #emotions#."],

        # Stages of stories
        'born': "\n#character.capitalize# was born in #location#.\n"
                "#charThey.capitalize# had two parents named #father.capitalize# and #mother.capitalize#.\n"
                "#character.capitalize# was #health# baby.\n",

        'toddler': ["#character.capitalize# just learnt #learning#,"
                    " #charThey# was very #emotions# about it!\n"
                    "#parent_reactions#\n"],

        'earlylife': '#character.capitalize# attended school for the first time!\n'
                     '#charThey.capitalize# was #emotions# by the experience.'

    }

    # Creates a grammar with the specific rules.
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)

    # Origin of the story
    story = grammar.flatten("[#setPronouns#][character:#character_name#][father:#name#]["
                            "mother:#name#]#born#\n\n#toddler#\n\n#earlylife#\n\n")
    # Splits each period when two new lines are found.
    final = story.split("\n\n")

    # Adds each line to export string
    counter = 0
    for period in final:
        counter += 1
        export_story += period

    # List type of story : 0 = born, 1 = toddler, 2 = early_life, 3 = teen, 4 = young_adult, 5 = adult, 6 = Elderly
    print(final)

    # String type of the story.
    print(export_story)
