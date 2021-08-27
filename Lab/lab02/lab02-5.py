s = int(input('s: '))

min = int(s/60)
sec = int(s%60)
hour = int(min/60)
min = int(min%60)


print(f'{s} seconds equals {hour} hour(s) {min} minute(s) and {sec} second(s)')