def named(**kwargs):    
    """
    """
    print(kwargs)

named(name="Bob", age=25)


# DETAILS AS NAME, BUT AGE = BLANK
def named_two(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}
named_two(details, 25)


# SPLIT DETAILS: NAME = NAME, AGE = AGE
def named_three(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}
named_three(**details)
