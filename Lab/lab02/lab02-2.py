kilo = int(input('Input distance(kilometer): '))
time = 0

for i in range(0,kilo):
    time+=10
    if i%6==0 and i!=0:
        time+=10

hour = int(time/60)
min = time%60

print(f'It takes {hour} hours and {min} minutes to reach the destination.')