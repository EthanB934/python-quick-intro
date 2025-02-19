planet_list = ["Mercury", "Mars"]

# Add two new list items to the end of planet_list

# Comma-Separated Items are initialized as a tuple.
# additional_planets = "Jupiter", "Saturn"

additional_planets_list = ["Uranus", "Neptune"]

# Append takes one argument at a time
planet_list.append("Jupiter")
planet_list.append("Saturn")

# Extend allows one list to be extended by, include, another list. Extend may convert tuples into a list.
# Extend cannot be used directly on a tuple.
planet_list.extend(additional_planets_list)


# Use .insert to add two new strings, "Earth", and "Venus", in the correct order.
# Insert takes two arguments. An index of a list, and the value to be found at that index.

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

# If extend is used without a list, it creates a comma separated list.
# Not what I needed, but cool
# pluto = "Pluto"
# planet_list.extend(pluto)

planet_list.append("Pluto")


# This is list slicing. The first integer at the colon is the first index item to be included in the range of the slice
# The colon represent a range.
# The final index is where the slicing ends. It does not include the list item at that index. Index 4 in this case is Jupiter.
rocky_planets = planet_list[0:4]

# print(rocky_planets)

# Del keyword removes item from list. If not iterating, access index directly.
# del planet_list[-1]

# print(planet_list)


# Create a new list containing tuples.
# Each tuple will hold the name of a spacecraft, and the names of the planets that the spacecraft has visited.

spacecraft = [
    ("Mariner 10", "Mercury"),
    ("MESSENGER", "Mercury"),
    ("Venera 1-16", "Venus"),
    ("Mariner 2", "Venus"),
    ("Mariner 5", "Venus"),
    ("Mariner 10", "Venus"),
    ("Pioneer Venus 1 and 2", "Venus"),
    ("Vega 1 and 2", "Venus"),
    ("Galileo", "Venus"),
    ("Magellan", "Venus"),
    ("Cassini", "Venus"),
    ("MESSENGER", "Venus"),
    ("Venus Express", "Venus"),
    ("Parker Solo Probe", "Venus"),
    ("Mariner 4", "Mars"),
    ("Mariner 6 and 7", "Mars"),
    ("Mariner 9", "Mars"),
    ("Viking 1 and 2", "Mars"),
    ("Mars Pathfinder", "Mars"),
    ("Mars Odyssey", "Mars"),
    ("Spirit", "Mars"),
    ("Opportunity", "Mars"),
    ("Phoenix", "Mars"),
    ("Dawn", "Mars"),
    ("Curiosity", "Mars"),
    ("Insight", "Mars"),
    ("Perseverance", "Mars"),
    ("Pioneer 10 and 11", "Jupiter"),
    ("Voyager 1 and 2", "Jupiter"),
    ("Ulysses", "Jupiter"),
    ("Galileo", "Jupiter"),
    ("Cassini", "Jupiter"),
    ("New Horizons", "Jupiter"),
    ("Juno", "Jupiter"),
    ("Pioneer 11", "Saturn"),
    ("Voyager 1 and 2", "Saturn"),
    ("Cassini", "Saturn"),
    ("Voyager 2", "Uranus"),
    ("Voyager 2", "Neptune"),
    ("New Horizons", "Pluto"),
]

# Problem: I have a list of planets, and I have a list of tuples. The tuples contain two strings,
# one is a spacecraft and the other is the name of a planet. I want to know which planets a spacecraft has
# visited. According to the tuple, a planet may only be visited by one spacecraft at a time, but a
# spacecraft may visit more than one planet. This means that the planets are unique.
#
# Strategy:  I have a list of planets. A planet can only receive one spacecraft at a time, but multiple
# spacecraft may visit one planet. Can I use the list of planets in some way to isolate which crafts
# have visited it?



for craft, destination in spacecraft:
    flight_log = print(f" {craft} has visited \n =============================")
    for mission in spacecraft:
        if craft == mission[0]:
            print(f"\t{mission[1]} \n")
            spacecraft.remove(mission)
