
def to_dict(obj): 
    return {column.name: getattr(obj, column.name) for column in obj.__table__.columns}

def to_lower_case(input_string):
    return input_string.lower()