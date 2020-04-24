__author__ = "James Clark"
__credits__ = ["James Clark"]
__version__ = "2.0"

import tracery
from tracery.modifiers import base_english

import gui

final = None
export_story = ''


# TODO (story):
#   - Understand english language structure, create sentences around this.
#   - Occupation
#   - Stories: Add a simple story for each period, before expanding them.
#       - A list of 'life events'
#       - Occupation

# Creates rules for the story before creating a story.
def createStory():
    global final, export_story
    rules = {

        # Adjectives
        'adj_personality': ['aggressive', 'agreeable', 'ambitious', 'brave', 'calm', 'delightful', 'eager', 'faithful',
                            'gentle', 'happy', 'jolly', 'kind', 'lively', 'nice', 'polite', 'proud', 'silly',
                            'thankful',
                            'witty', 'wonderful', 'zealous', 'angry', 'bewildered', 'clumsy', 'defeated', 'embarrassed',
                            'fierce', 'grumpy', 'helpless', 'jealous', 'lazy', 'nervous', 'mysterious', 'obnoxious',
                            'scary', 'thoughtless', 'uptight', 'worried', 'sad', 'joyful', 'relieved', 'funny',
                            'surprised', 'angry', 'excited', 'fearful'],
        'adj_appearance': ['attractive', 'bald', 'beautiful', 'dazzling', 'elegant', 'fancy', 'glamorous',
                           'gorgeous', 'handsome', 'magnificent', 'plain', 'quaint', 'scruffy', 'short',
                           'ugly', 'unkempt', 'unsightly'],
        'adj_good_bad': ['good', 'bad', 'clumsy', 'ambitious'],
        'adj_color': ['black', 'blue', 'gray', 'green', 'icy', 'lemon', 'mango', 'orange', 'purple', 'red', 'salmon',
                      'white', 'yellow'],

        # Verbs
        'verb': ['am', 'are', 'was', 'were', 'be', 'being', 'been', 'is', 'have', 'has', 'had', 'could', 'should',
                 'would', 'may', 'might', 'must', 'shall', 'can', 'will', 'do', 'did', 'does', 'having'],

        # General story attributes
        'character_name': [gui.name],
        'name': ['Jordan', 'Riley', 'Parker', 'Blake', 'Hayden', 'Taylor', 'Charlie', 'Finley', 'Morgan', 'Elliot',
                 'Drew', 'Jamie', 'Kelly', 'Jessie', 'Reese', 'Harley', 'Rory', 'Rowen', 'Joey', 'Frankie',
                 'Alex', 'Andy', 'Billy', 'Cameron', 'Casey', 'Ellis', 'Evan', 'Kieran', 'Murphy', 'Nico',
                 'Owen', 'Addison', 'Ashley', 'Blake', 'Carter', 'Georgie', 'Jesse', 'Kennedy', 'Kyle', 'Nicky',
                 'Perry', 'Quinn', 'Sam', 'Tyler', 'Bobby', 'Chris', 'Dana', 'Danny', 'Francis', 'Kelly', 'Max',
                 'Sky'],
        'location': ['United Kingdom', 'United States', 'China', 'Japan', 'Germany', 'India', 'France', 'Italy',
                     'Brazil', 'Canada', 'Russia', 'Spain', 'Australia', 'Mexico', 'Netherlands', 'Turkey',
                     'Switzerland', 'Sweden', 'Belgium', 'Austria', 'Norway', 'Ireland', 'Hong Kong', 'Singapore',
                     'Denmark', 'Romania', 'New Zealand', 'Ukraine', 'Croatia', 'Finland'],

        'sport': ['football', 'cricket', 'basketball', 'tennis', 'volleyball', 'table tennis', 'baseball',
                  'golf', 'rugby', 'boxing', 'swimming', 'gymnastics'],

        'occupation': ['n accountant', 'n actor', ' pilot', 'n artist', ' lawyer', ' lifeguard', ' banker', ' chef',
                       ' dentist', ' teacher', ' farmer', ' historian', ' programmer', ' firefighter', ' policeman',
                       ' dancer', ' model', ' racing driver', ' politician', ' paramedic', ' nurse', ' doctor',
                       ' trader', ' writer', 'journalist'],

        'success': ['won', 'lost'],

        'setPronouns': ["'[charThey:she]', '[charThem:her]', '[charTheir:her]', '[charTheirs:hers]'",
                        "'[charThey:he]', '[charThem:him]', '[charTheir:his]', '[charTheirs:his]'"],
        'learning': ['talking', 'walking', 'shouting', 'crawling', 'reading', 'writing'],
        'health': ['a healthy', 'an unhealthy'],

        'parent_reactions': ["#father.capitalize# was #adj_personality#",
                             "#mother.capitalize# was #adj_personality#"],
        'baby': ['boy', 'girl'],

        # Stages of stories
        'born': "\n#character.capitalize# was born in #location#.\n"
                "#charThey.capitalize# had two parents named #father.capitalize# and #mother.capitalize#.\n"
                "#character.capitalize# was #health# baby.\n"
                "#charThey.capitalize# is #adj_personality# and #adj_appearance#.\n",

        'toddler': ["#character.capitalize# just learnt #learning#,"
                    " #charThey# is very #adj_personality#.\n"
                    "#parent_reactions# about it!\n"
                    "#toddler_life_event#\n"],

        'toddler_life_event': ['#character.capitalize# just had their first haircut.',
                               '#character.capitalize# lost their first tooth!',
                               '#character.capitalize# learnt to ride a bike',
                               '#character.capitalize# is interested in #character_sport#.',
                               '#character.capitalize# met #charTheir# neighbourhood friend called #relationship#.'],

        'earlylife': '#character.capitalize# attended school for the first time!\n'
                     '#charThey.capitalize# was #adj_personality# by the experience.\n'
                     '#earlylife_event#',

        'earlylife_event': ['#charThey.capitalize# was put in the same class as #charTheir# friend #relationship#.\n'
                            '#character.capitalize# thought #relationship# was #adj_appearance#.\n'
                            '#character.capitalize# took #character_sport# at school and was #adj_good_bad# at it.\n'],
        'teen': ['#teen_event#'],

        'teen_event': ['#character.capitalize# took part in a #character_sport# tournament and #success#!\n',
                       '#character.capitalize# was interested in working as a#character_occ#\n',
                       '#character.capitalize# got into a relationship with #relationship#\n'],
        'youngadult': ['#character.capitalize# landed their first job as a#character_occ#.\n'
                       '#charThey.capitalize# was #adj_personality#.\n'
                       '#father.capitalize# was #adj_personality# and #mother.capitalize# was #adj_personality#.\n'
                       '#youngadult_event#'],
        'youngadult_event': ['#character.capitalize# left home and moved to #location#.\n',
                             '#character.capitalize# passed #charTheir# driving test!\n',
                             '#character.capitalize# went on holiday with #relationship# to #location#.\n',
                             '#character.capitalize# attended University in #location#.\n',
                             '#character.capitalize# was promoted at work!\n'],
        'adult': ['#character.capitalize# just bought #charTheir# first house!\n',
                  '#character.capitalize# was promoted at work!\n',
                  '#character.capitalize# moved in with #relationship#.\n'
                  '#character.capitalize# married #relationship#.\n'
                  '#character.capitalize# had a baby, its a #gender#!\n'
                  '#charThey.capitalize# named #charThem# #babyname#\n'],

        'elderly': ['#character.capitalize# was #adj_personality# with how #charTheir# life turned out.\n'
                    '#charThey.capitalize# retired from working as a#character_occ#.\n'
                    '#charThey.capitalize# finally could relax, #charThey# was #adj_personality# about this.\n']
    }

    # Creates a grammar with the specific rules.
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)

    # Origin of the story
    story = grammar.flatten("[#setPronouns#][character:#character_name#][father:#name#]"
                            "[mother:#name#][relationship:#name#][character_sport:#sport#][character_occ:#occupation#]"
                            "[gender:#baby#][babyname:#name#]"
                            "#born#\n\n#toddler#\n\n#earlylife#\n\n#teen#\n\n#youngadult#\n\n#adult#\n\n#elderly#")
    # Splits each period when two new lines are found.
    final = story.split("\n\n")

    # Adds each line to export string
    counter = 0
    for period in final:
        counter += 1
        export_story += period

    export_story = "This is the story of {}... \n\n".format(gui.name) + export_story

    # List type of story : 0 = born, 1 = toddler, 2 = early_life, 3 = teen, 4 = young_adult, 5 = adult, 6 = Elderly
    print(final)

    # String type of the story.
    print(export_story)
