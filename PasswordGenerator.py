import random
import string

i = 0
password = str()
lettersAndPunctuationAndNumbers = (
    string.ascii_letters + string.punctuation + "0123456789"
)


def AskForLenthOfPassword():
    print("How long do you want your password to be?")
    try:
        lenthOfPassword = int(input())
    except ValueError:
        print("Please type in a --->number<---")
        print("Lets try that again")
        return AskForLenthOfPassword()
    if lenthOfPassword < 0:
        print("*ahem*")
        print("Lets try that again")
        return AskForLenthOfPassword()
    if lenthOfPassword > 1000000:
        print("try a resonable number")
        return AskForLenthOfPassword()
    return lenthOfPassword


lenthOfPassword = AskForLenthOfPassword()
while i < lenthOfPassword:
    i = i + 1
    password = password + random.choice(lettersAndPunctuationAndNumbers)
print(password)
