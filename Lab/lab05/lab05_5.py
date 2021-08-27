n = int(input('How many animals are there in the zoo? : '))

data = {}

for i in range(n):
    question,answer = map(str,input().split())
    data.setdefault(question,answer)

r = int(input('How many questions do you want to ask? : '))

for i in range(r):
    question = input()
    try:
        print(data[question])
    except KeyError:
        print("Sorry we don't have that animal.")