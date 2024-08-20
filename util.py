import re

def remove_surrogate_pairs(string):
    return re.sub(r"[\ud800-\udfff]", "", string)

def remove_invild_escape(string):
    return re.sub(r'\\(?!["\\/bfnrt])', '', string)

def clean_string(string):
    return remove_invild_escape(remove_surrogate_pairs(string))