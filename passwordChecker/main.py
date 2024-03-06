from utils import *


password = input("password to check: ")


hasUppercaseLetters = False
hasLowerCaseLetters = False
hasNumbers = False
hasSpecialCharacters = False
isLong = False


print("calculating length")
if IsLong(password):
    isLong = True

print("checking uppercase letters")
if HasUppercase(password):
    hasUppercaseLetters = True

print("checking lower case letters")
if HasLower(password):
    hasLowerCaseLetters = True

print("checking numbers")
if HasNumbers(password):
    hasNumbers = True

print("checking special characters")
if HasSpecialCharacters(password):
    hasSpecialCharacters = True


print("calculating strength")
print()
print(f"password strength: {GetPasswordStrength(hasUppercaseLetters, hasLowerCaseLetters, hasNumbers, hasSpecialCharacters, isLong)}")
