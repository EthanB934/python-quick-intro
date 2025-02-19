# Initialize an empty list
movie_collection = []


# Define a function that will create a new tuple and add it to the movie_collection list
def add_movie(title, director, year):
    movie = (title, director, year)
    movie_collection.append(movie)
    print(f"{movie} has been appended to the your movie collection")


# adding movies to the list
add_movie("Coraline", "Henry Selick", 2009)
add_movie("Brave", "Brenda Chapman", 2012)
add_movie("Kung Fu Panda", "Mark Osborne", 2008)
add_movie("Major Payne", "Nick Castle", 1995)


# define a function that displays all movies
def display_movie_hoard():
    print("Your Movie Collection:")
    for title, director, year in movie_collection:
        print(
            f"Your movie {title} was directed by {director} and was produced in {year}"
        )


display_movie_hoard()


# define a function that finds a movie by the director
def director_movies(director):
    print(f"{director} Movies in your movie collection:")
    for movie_info in movie_collection:
        if director in movie_info:
            print(f"{movie_info[0]} - {movie_info[2]}")


director_movies("Henry Selick")


# define a function that removes a movie from the movie collection
def remove_movie(movie_name):
    # iterates tuples in list
    for movie in movie_collection:
        # destructures values in tuples
        if movie_name in movie:
            print(f"{movie_name} was found and removed from your collection")


remove_movie("Major Payne")


# define a function that updates movie info
def update_movie_info(title, new_director, new_year):
    # iterates movie tuples
    for movie in movie_collection:
        # finds movie by title
        if title in movie:
            # removes matching movie
            movie_collection.remove(movie)
            # creates a new tuple from arguments
            movie = (title, new_director, new_year)
            # readds tuple into list
            movie_collection.append(movie)
            # notifies user in log
            print(f"Your movie collection has been updated: {movie}")


update_movie_info("Coraline", "Mr. Burns", 2011)

display_movie_hoard()


# defined a function that can sort the movie collection by the years
def sort_movies_by_year(movie_list):
    # sorts list based on second index, hopefully 
    sorted_movie_list = sorted(movie_list, key=lambda movie: movie[2])
    print("Your Sorted Movie Collection:")
    for title, director, year in sorted_movie_list:
        print(
            f"Your movie {title} was directed by {director} and was produced in {year}"
        )


sort_movies_by_year(movie_collection)
