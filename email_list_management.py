# initialize empty sets
subscribers = set()
unsubscribers = set()


# Define a function that will add a new email to a specified set. It will logs this addition
def add_email(email, set_name):
    # ensures consistency in letter casing
    user_email = email.lower()

    # determines to which set email should be added
    set_name.add(user_email)

    # notifies user of addition
    print(f"Email {email} has been added to set {set_name}")


add_email("eb@example.com", subscribers)
add_email("aj@example1.com", unsubscribers)
add_email("dh@example2.com", subscribers)
add_email("ea@example3.com", unsubscribers)
add_email("bn@example4.com", subscribers)
add_email("ie@example5.com", unsubscribers)


# Define a function that will remove a specific email from a determined set
def remove_email(email, set_name):
    # searches set for email
    if email in set_name:
        set_name.remove(email)
        print(f"Email {email} was removed from set {set_name}")
    else:
        print(f"Email {email} was not found in set {set_name}")


remove_email("eb@example.com", subscribers)
remove_email("dh@example2.com", subscribers)
remove_email("ea@example3.com", unsubscribers)


def display_set_contents(set_name):
    print("Content Results: ")
    for email in set_name:
        print(f"{email} is included in this set")


display_set_contents(subscribers)
display_set_contents(unsubscribers)


# Define a function that will return only the emails of subscribers. No parameters needed.
def find_subscribers():
    print("Current Subscribers:")
    for subscriber in subscribers:
        print(f"{subscriber}")
        
find_subscribers()