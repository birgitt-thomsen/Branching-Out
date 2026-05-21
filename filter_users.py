""" Program to filter users by name and age """

import json


def load_data():
    with open("users.json", "r") as file:
        return json.load(file)


def filter_users_by_name(data, name):
    """ Filter users by name """
    filtered_users = [user for user in users if
                      user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(data, age):
    """ Filter users by age """
    filtered_users = [user for user in users if
                      user["age"] == int(age)]

    for user in filtered_users:
        print(user)


def filter_users_by_email(data, email):
    """ Filter users by email """
    filtered_users = [user for user in users if
                      user["email"].lower() == email.lower()]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input(
        "What would you like to filter by? (Fields 'name', 'age' and 'email "
        "are supported): ").strip().lower()

    users = load_data()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(users, name_to_search)
    elif filter_option == "age":
        age_to_search = input("Enter an age to filter users: ").strip()
        filter_users_by_age(users, age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(users, email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
