age = int(input('Enter your age : '))

if(age <= 12):
    print("You are Child.")
elif(age <= 18):
    print("You are Adolescence.")
elif(age<= 59):
    print("You are Adult.")
else:
    print("You are Senior Adult.")