##############################################
# -------------- Introduction -------------- #
##############################################

# Opening your comic book store, the Sorcery Society, has been a lifelong dream come true. You quickly diversified your
# shop offerings to include miniatures, plush toys, collectible card games, and board games. Eventually, the store
# became more a games store with a selection of this week's newest comic books and a small offering of graphic novel
# paperbacks. Completing your transformation means offering space for local tabletop gamers. They love to play their
# favorite RPG, "Abruptly Goblins!" and will happily pay you per chair to secure the space to do it. Unfortunately,
# planning the game night has fallen to you. If you pick the wrong night, not enough people will come and the game
# night will be cancelled. You decide it's best that you automate the game night selector to get the most people
# through the door. First you need to create a list of people who will be attending the game night.


##############################################
# ------------------ Code ------------------ #
##############################################


### 1- Create an empty dictionary called gamers. This will be your list of people who are attending game night. ###


gamers_dict = {}


# Now we want to create a function that will update this dict and add a new gamer to the gamers list. Each gamer should
# be a dictionary with the following keys:
# "name": a string that contains the gamer's full or presumed name. E.g., "Vicky Very"
# "availability": a list of strings containing the names of the days of the week that the gamer is available.
# E.g., ["Monday", "Thursday", "Sunday"]


### 2- Create a function called add_gamer that takes two parameters: gamer and gamers_list. ###
# The function should check that the argument passed to the gamer parameter has both "name" and an "availability" as
# keys and if so add gamer to gamers_list.


def add_gamer(gamer, gamers_list):
    if "name" in gamer and "availability" in gamer:
        name = gamer["name"]
        availability = gamer["availability"]
        gamers_list[name] = availability
    else:
        print("Gamer missing critical information")


### 3- Next we want to add our first gamer! ###
# Her name is Kimberly Warner and she's available on Mondays, Tuesdays, and Fridays. Create a dictionary called kimberly
# with the name and availability given above. Call add_gamer with kimberly as the first argument and gamers as the
# second.


kimberly = {"name": "Kimberly Warner",
            "availability": ["Monday", "Tuesday", "Friday"]}

add_gamer(kimberly, gamers_dict)


# Great! Let's add a couple more gamers to the list!


add_gamer({'name': 'Thomas Nelson', 'availability': ["Tuesday", "Thursday", "Saturday"]}, gamers_dict)
add_gamer({'name': 'Joyce Sellers', 'availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers_dict)
add_gamer({'name': 'Michelle Reyes', 'availability': ["Wednesday", "Thursday", "Sunday"]}, gamers_dict)
add_gamer({'name': 'Stephen Adams', 'availability': ["Thursday", "Saturday"]}, gamers_dict)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers_dict)
add_gamer({'name': 'Latasha Bryan', 'availability': ["Monday", "Sunday"]}, gamers_dict)
add_gamer({'name': 'Crystal Brewer', 'availability': ["Thursday", "Friday", "Saturday"]}, gamers_dict)
add_gamer({'name': 'James Barnes Jr.', 'availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers_dict)
add_gamer({'name': 'Michel Trujillo', 'availability': ["Monday", "Tuesday", "Wednesday"]}, gamers_dict)


### 4- Finding the perfect availability. ###
# Now that we have a list of the people interested in game night, we want to be able to calculate which nights
# would have the most participation. First we need to create a frequency table which correlates each day of the week
# with gamer availability. Create a function called `build_daily_frequency_table` that takes no argument returns a
# dictionary with the days of the week as keys and `0`s for values. We'll be using this to count the availability per
# night. Call `build_daily_frequency_table` and save the results to a variable called `count_availability`.


def build_daily_frequency_table():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    frequency_table = {day: 0 for day in days_of_week}
    return frequency_table


### 5- Next we need to count the number of people every night. ###
# Write a function called calculate_availability that takes a list of gamers as an argument gamers_list and a frequency
# table available_frequency. The function should iterate through each gamer in gamers_list and iterate through each day
# in the gamer's availability. For each day in the gamer's availability, add one to that date on the frequency table.
# Now let's use these tools to find the best night to run Abruptly Goblins!
# Call calculate_availability with gamers and count_availability. Print out count_availability afterwards.


def calculate_availability(gamers_list, available_frequency):
    # first, reset the "available_frequency"
    available_frequency = build_daily_frequency_table()

    for gamer, availability in gamers_list.items():
        for day in availability:
            if day in available_frequency:
                available_frequency[day] += 1
    return available_frequency


count_availability = build_daily_frequency_table()
count_availability = calculate_availability(gamers_dict, count_availability)
print("Number of Gamers Based on Days: " + str(count_availability))


# Lastly we need a way to pick the day with the most available people to attend so that we can schedule game night on
# Write a function find_best_night that takes a dictionary availability_table and returns the key with the highest
# number.


def find_best_night(availability_table):
    katilimci = 0
    for day, availability in availability_table.items():
        if availability > katilimci:
            best_night = day
            katilimci = availability
    return best_night


### 6- Now let's find the best day to host game night. ###
# Call find_best_night with count_availability, store the result in a variable called game_night. Print out game_night
# to find out which day it is.


game_night = find_best_night(count_availability)
print("The Best Night: " + str(game_night))


### 7- And let's make a list of all of the people who are available that night. ###
# Create a function available_on_night that takes two parameters: gamers_list and day and returns a list of people who
# are available on that particular day. Call available_on_night with gamers and game_night and save the result into the
# variable attending_game_night.
# Print attending_game_night.


def available_on_night(gamers_list, day):
    valid_gamer = []
    for gamer, availability in gamers_list.items():
        if day in availability:
            valid_gamer.append(gamer)
    return valid_gamer


attending_game_night = available_on_night(gamers_dict, game_night)
print("The Players Who Comes to The Game on The Best Night: " + str(attending_game_night))


### 8- Define a string, called form_email with interpolation variables {name}, {day_of_week}, and {game} ###
# (in case we decide we want to use this featureset to host a different game night) Use it to tell your gaming
# attendees the night their Abruptly Goblins! game can be played.


form_email = """
Dear {name},

The Sorcery Society is happy to host "{game}" night and wishes you will attend. Come by on {day_of_week} 
and have a blast!

Magically Yours,
the Sorcery Society
"""


### 9- Create a function send_email with three parameters: gamers_who_can_attend, day, and game. ###
# Print form_email for each gamer in gamers_who_can_attend with the appropriate day and game. Call send_email with
# attending_game_night, game_night, and "Abruptly Goblins!".


def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer, game=game, day_of_week=day))


send_email(attending_game_night, game_night, "Abruptly Goblins!")


### 10- Create a list for who can not come ###
# Create unable_to_attend_best_night list of everyone in gamers that wasn't able to attend game night on game_night.
# unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer['availability']]


unable_to_attend_best_night = {}
for gamers, availability in gamers_dict.items():
    if not game_night in availability:
        unable_to_attend_best_night[gamers] = availability


print("The Players Who Can't Attend to The Game on The Best Night:" + str(unable_to_attend_best_night.keys()))


# Call calculate_availability with unable_to_attend_best_night and second_night_availability.


second_night_availability = build_daily_frequency_table()
print(second_night_availability)


### 11- Find the second best night and prepare an email for them ###
# Create second_night_availability frequency table by calling build_daily_frequency_table.
# Call find_best_night with the now filled-in second_night_availability, save the results in second_night.


second_night_availability = calculate_availability(unable_to_attend_best_night, second_night_availability)
print("The Common Day for Who Can Not Attend The Game Night: " + str(second_night_availability))

second_night = find_best_night(second_night_availability)
print("The Best 2nd Night: " + str(second_night))


# Create the list available_second_game_night by calling available_on_night with gamers and second_night
# Let the gamers know by calling send_email with available_second_game_night, second_night, and "Abruptly Goblins!"


available_second_game_night = available_on_night(gamers_dict, second_night)
send_email(available_second_game_night, second_night, "Abruptly Goblins!")