students = ["Tanner", "Paul", "Jason"]

# print(students[0])
# print(students[1])

# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "food goes here is a good food".

foods = ("Oranges", "Chicken", "Burritos")

# for food in foods:
#     print(f"{food} IS AMAZING FOOD")

# Using a for loop, print just the last two food strings from foods.

# for idx, food in enumerate(foods):
#     if idx != 0:
#         print(idx, food)

# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"

home_town = {
    'city': 'Upland',
    'state': 'CA',
    'population': 100000
}

# print(f"I was born in {home_town['city']}, {home_town['state']} - with a population of {home_town['population']}")

# for key in home_town:
#    print( f"{key} = {home_town[key]}" )

# Create an empty list named cohort.

# Using a for loop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape:

#  {
#  	'student': 'Tina',
#  	'fav_food' 'Cheeseburger'
#  }
# Iterate over cohort printing out each element.

cohort = []

for idx, student in enumerate(students):
    cohort.append({'student': student, 'fav_food': foods[idx]})
# print(cohort)


# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_students printing out each string.

awesome_students = [f"{student} is awesome!" for student in students]
# print(awesome_students)

# Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a.

for food in foods:
    for f in food:
        if f == 'a':
            print(food)