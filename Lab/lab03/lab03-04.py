from math import pi, sin, cos, tan


def convertPi(degree: int) -> float:
    return degree * pi / 180


degree = int(input('Degree : '))

rad = convertPi(degree)

print(f'sin : {sin(rad):.2f}')
print(f'cos : {cos(rad):.2f}')
print(f'tan : {tan(rad):.2f}')
