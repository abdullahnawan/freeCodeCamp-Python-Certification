def add_setting(settings_dict, key_value_tuple):
    key = key_value_tuple[0].lower()#breaks the new key value tuple into its key and makes it lowercase
    value = key_value_tuple[1].lower#breaks the new key value tuple into its value and makes it lowercase

    if key in settings_dict:
        print(f'Setting {key} already exists! Cannot add a new setting with this name.') #checks if the tuples key already exists in the dictionary and if it does it say cant do that

    settings_dict[key] = value #adds the tuple item into the dictionary
    return f'Setting {key} added with value {value} successfully!' #returns statement of completion

def update_setting():
    pass

def delete_setting():
    pass

def view_settings():
    pass

test_settings = {
    'Theme': 'dark',
    'Notifications': 'enabled',
    'Volume': 'high'
}