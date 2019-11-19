#Too hot

def too_hot(temperature, isSummer):
    if 60 <= temperature <= 90 and not isSummer:
        return True
