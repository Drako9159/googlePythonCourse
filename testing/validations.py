def validate_user(username, minlen):
    # assert is a keyword that will raise an AssertionError if the following statement is false
    assert type(username) == str, "username must be a string" 
    if minlen < 1:
        # raise is a keyword that will raise an exception
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

# print(validate_user("blue.kale", 3)) # False
# print(validate_user([3]. 1)) # AssertionError