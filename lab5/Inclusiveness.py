def greet_user(name, gender):
    if gender.lower() == 'male':
        title = "Mr."
    elif gender.lower() == 'female':
        title = "Mrs."
    else:
        title = ""  # for unknown or unspecified genders

    greeting = f"Hello {title} {name}, welcome to our platform!"
    return greeting


# Example usage
print(greet_user("John", "Male"))
print(greet_user("Sara", "Female"))
print(greet_user("Alex", "Non-binary"))