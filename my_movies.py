# This module will be responsible for creating a list.
# I will be adding, removing, displaying, and counting list items.

# Task:
# 1. Initialize an Empty List

favorites_movies = []

# 2. Write a function, add_movie(movie) that will add a string to the initialized
# list. It will print a string of what was added to the list.


# Movie as a parameter initializes the dependency for positional arguments.
def add_movie(movie):
    favorites_movies.append(movie)
    print(f"You have added '{movie}' to your favorite movies list!")


# Movie in this function invocation is a positional argument.

# 3. Write a function remove_movie(movie) that will remove a string list item from the favorite_movies list.


def remove_movie(movie):
    # Remove function iterates through list for item matching argument.
    # If not found, list.remove(x): x not in list
    favorites_movies.remove(movie)
    print(f"You have removed '{movie}' from your favorite movies list...")


# 4. Write a function that displays all of the movies in the list.
# This function will not need any parameters.
def display_movies(movie_list):
    if len(movie_list):
        print("Your favorite Movies Collection")
        for movie in movie_list:
            print(f"- {movie}")
    else:
        print("There are no entries in this collection!")


# 5. Write a function, count_movies that counts the items in the list


def count_movies(movies_list):
    # len() is a built in list method that finds the number of items in a list, the length of the list.
    # count() is a built in list method that takes one argument and searches the list for an item matching the argument
    # count() returns the amount of times that particular list item occurs in the list. 
    amount = len(movies_list)
    print(f"Amount of movies in your favorite movies collection: {amount}")

# 6 Write a function, find_movie that iterates the list to find a corresponding item to the passed in argument

def find_movie(movie):
    if movie in favorites_movies:
        print(f"Found movie {movie} in your favorite movies collection!")
    else :
        print(f"{movie} is not in your favorite movies collection...would you like to add it?")

# Write a function, clear_movies that removes all items from the list

def clear_movies():
    # .remove() list method removes first encounter of iterating item. 
    # favorites_movies.remove(movie)
    favorites_movies.clear()
    print("All movies have been removed from the movies list!")

add_movie("Star Wars: The Phantom Menace")
add_movie("Star Wars: Attack of the Clones")
add_movie("Star Wars: Revenge of the Sith")

display_movies(favorites_movies)

count_movies(favorites_movies)

find_movie("Star Wars: Attack of the Clones")

remove_movie("Star Wars: Attack of the Clones")

find_movie("Star Wars: Attack of the Clones")

display_movies(favorites_movies)

count_movies(favorites_movies)

clear_movies()

display_movies(favorites_movies)