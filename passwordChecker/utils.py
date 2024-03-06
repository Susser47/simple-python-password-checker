def HasUppercase(password):
    return any(char.isupper() for char in password)


def HasLower(password):
    return any(char.islower() for char in password)


def HasNumbers(password):
    return any(char.isdigit() for char in password)


def HasSpecialCharacters(password):
    specialCharacters = "!£$%&/()=?^*[]§°@#-_.:,;<>|"

    return any(char in specialCharacters for char in password)


def IsLong(password):
    return len(password) >= 12


def GetPasswordStrength(hasUppercaseLetters: bool, hasLowerCaseLetters: bool, hasNumbers: bool, hasSpecialCharacters: bool, isLong: bool):
    # calculated a grade from 0 to 4
    grade = 0

    if hasUppercaseLetters:
        grade += 1
    if hasLowerCaseLetters:
        grade += 1
    if hasNumbers:
        grade += 1
    if hasSpecialCharacters:
        grade += 1
    if isLong:
        grade += 1

    if grade == 0:
        return "very weak"
    elif grade == 1:
        return "weak"
    elif grade == 2:
        return "mediocre"
    elif grade == 3:
        return "strong"
    elif grade == 4:
        return "very strong"
    elif grade == 5:
        return "very very strong"