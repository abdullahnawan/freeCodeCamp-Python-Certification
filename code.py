def add_setting(settings_dict, key_value_tuple):
    key = key_value_tuple[0].lower()#breaks the new key value tuple into its key and makes it lowercase
    value = key_value_tuple[1].lower#breaks the new key value tuple into its value and makes it lowercase

    if key in settings_dict:
        return f'Setting {key} already exists! Cannot add a new setting with this name.' #checks if the tuples key already exists in the dictionary and if it does it say cant do that

    settings_dict[key] = value #adds the tuple item into the dictionary
    return f'Setting {key} added with value {value} successfully!' #returns statement of completion

def update_setting(settings_dict, key_value_tuple):
    key = key_value_tuple[0].lower()
    value = key_value_tuple[1].lower

    if key in settings_dict:
        settings_dict[key] = value
        return f'Setting {key} updated to {value} successfully!' #checks to see if the key already exists in the dictionary and if it does it updates it 
    
    return f'Setting {key} does not exist! Cannot update a non-existing setting.'#return statement if the key does not exist in the dictionary

def delete_setting(settings_dict, key):
    key = key.lower()
    
    if key in settings_dict:
        del settings_dict[key]
        return f'Setting {key} deleted successfully!' #checks to see if the key exists in the dictionary and if it does it delets it 
    
    return 'Setting not found' #return statment if not found

def view_settings():
    pass

test_settings = {
    'Theme': 'dark',
    'Notifications': 'enabled',
    'Volume': 'high'
}