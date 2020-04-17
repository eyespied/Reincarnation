import random

death_probability = 0
death_multiplier = 0
life_expectancy = 0


def death(location):
    global death_multiplier
    global death_probability
    i = 0
    prob_of_death = 0
    result = 0

    if location == "Spain":
        while result <= 100:
            death_probability = 0.01 * i
            i = i + 1
            death_multiplier = 0.07
            print("Year: " + str(i))
            random_death = random.uniform(0, death_multiplier)
            prob_of_death += (death_probability * random_death)
            result = prob_of_death * 100
            print("Probability of death: " + str(result) + "%")

    if location == "United Kingdom":
        death_multiplier = 0.5

    if location == "Japan":
        death_multiplier = 0.1


if __name__ == "__main__":
    locations_list = [["Spain"], ["United Kingdom"], ["Japan"]]
    chosen_location = []
    random_yes = random.randint(0, len(locations_list) - 1)
    random_location = str(locations_list[random_yes])
    new = random_location.replace("'", "").replace("[", "").replace("]", "")
    print("Current location = " + new)

    death(new)
