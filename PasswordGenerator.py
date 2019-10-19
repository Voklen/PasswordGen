import string
import random
i = 0
error = 0
password = str()
lettersAndPunctuation = string.punctuation + string.ascii_letters
while True:
    print("How long do you want your password to be?")
    try:
        lenthOfPassword = int(input())
        if lenthOfPassword < 0:
            print("*ahem*")
            print("Lets try that again")
        else:
            if lenthOfPassword > 1000000:
                print("try a resonable number")
            else: break
    except:
        print("Please type in a --->number<---")
        print("Lets try that again")
while i < lenthOfPassword:
    i = i+1
    password = password + random.choice(lettersAndPunctuation)
print (password)
