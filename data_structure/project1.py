people = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

# Display old list
for name, fact in people.items():
    print(name + ": " + fact)

# Change a fact
people["Jeff"] = "Is afraid of heights."

# Add new person
people["Jill"] = "Can hula dance."

print()

# Display updated list
for name, fact in people.items():
    print(name + ": " + fact)