with open('pi') as file:
    lines = file.readlines()

pi1 = ''
for line in lines:
    pi1 += line.rstrip()

while True:
    birthday = input("Enter your birthday, in the form mmddyy(input q to quit): ")
    if birthday == 'q':
        break
    else:
        if birthday in pi1:
            print("Your birthday appears in the first million digits of pi ! ")
        else:
            print("Your birthday does not appear in the first million digits of pi.")


