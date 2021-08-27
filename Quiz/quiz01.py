score = int(input('Enter your score : '))

while not (score >= 0 and score <= 100):
    score = int(input('Error score... Enter your score again : '))

if score >= 80:
    print('Grade A')
elif score >= 70:
    print('Grade B')
elif score >= 60:
    print('Grade C')
elif score >= 50:
    print('Grade D')
else:
    print('Grade F')
