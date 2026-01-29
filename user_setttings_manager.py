test_settings = {
    'kEy1': 'STring 1',
    'kEy2': 'sTRing 2',
    'kEy3': 'sTRing 3'
}


def add_setting(dictionary, tuples):
    key, value = tuples
    key = key.lower()
    value = value.lower()
    if key in dictionary:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    dictionary[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(dictionary, tuples):
    key, value = tuples
    key = key.lower()
    value = value.lower()
    if key in dictionary:
        dictionary[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    

def delete_setting(dictionary, key):
    key = key.lower()
    if key in dictionary:
        dictionary.pop(key, 'Setting not found!')
        return f"Setting '{key}' deleted successfully!"
    return f'Setting not found!'


def view_settings(dictionary):
    if not dictionary:
        return f'No settings available.'
    else:
        result = "Current User Settings:\n"
        for key, value in dictionary.items():
            result += f"{key.capitalize()}: {value}\n"
        return result


print(add_setting({'theme': 'light'}, ('THEME', 'dark')))
print('\n')
print(add_setting({'theme': 'light'}, ('volume', 'high')))
print('\n')
print(update_setting({'theme': 'light'}, ('theme', 'dark')))
print('\n')
print(delete_setting({'theme': 'light'}, 'theme'))
print('\n')
print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))
