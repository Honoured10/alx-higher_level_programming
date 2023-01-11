#!/usr/bin/python3
def class_to_json(obj):
    # Initialize an empty dictionary to store the object's attributes
    json_obj = {}
    
    # Get the object's attributes
    obj_attributes = obj.__dict__
    
    # Iterate through the object's attributes
    for attr in obj_attributes:
        # Get the value of the current attribute
        attr_value = obj_attributes[attr]
        
        # Check if the value is serializable (list, dictionary, string, 
        # integer, or boolean)
        if isinstance(attr_value, (list, dict, str, int, bool)):
            # If it is, add it to the json_obj dictionary
            json_obj[attr] = attr_value
        else:
            # If the value is not serializable, raise an exception
            raise TypeError("Attribute '{}' is not serializable".format(attr))
    
    # Return the json_obj dictionary
    return json_obj
