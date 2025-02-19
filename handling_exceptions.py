my_dict = {"name": "Alice", "age": 30, "city": "New York"}


# function that looks up a key value pairs in a dictionary
def get_value(dictionary, key):
    try:
        # attempts first
        value = dictionary[key]
        print(f"The value for '{key}' is: {value}")
        # if key is not in the dictionary, raises a KeyError
    except KeyError as e:
        print(f"The value for {key} was not found or may not exist in {dictionary}")


# Example usage
get_value(my_dict, "name")
get_value(my_dict, "occupation")
