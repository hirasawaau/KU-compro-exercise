from math import pi


def inputShape():
    return int(input('Input Shape: '))


def calculateSphere():
    radius = int(input('Input radius(meter): '))
    r3 = radius * radius * radius
    volume = 4 * pi * r3 / 3
    print(f'The volume is {float(volume):.2f} cubic meter.')
    return volume


def calculateCone():
    radius = int(input('Input radius(meter): '))
    height = int(input('Input height(meter): '))

    volume = (pi * (radius**2) * height) / 3
    print(f'The volume is {float(volume):.2f} cubic meter.')
    return volume


def calculateCylinder():
    radius = int(input('Input radius(meter): '))
    height = int(input('Input height(meter): '))

    volume = pi * (radius**2) * height
    print(f'The volume is {float(volume):.2f} cubic meter.')
    return volume


def calculatePrism():
    width = int(input('Input width(meter): '))
    length = int(input('Input length(meter): '))
    height = int(input('Input height(meter): '))

    volume = width * length * height
    print(f'The volume is {float(volume):.2f} cubic meter.')
    return volume


def calculatePyramid():
    width = int(input('Input width(meter): '))
    length = int(input('Input length(meter): '))
    height = int(input('Input height(meter): '))

    volume = width * length * height / 3
    print(f'The volume is {float(volume):.2f} cubic meter.')
    return volume


def calculatePrice(v):

    price_per_baht = int(input('Price(Bath) per 1 cubic meter: '))

    print(f'The price is{float(v*price_per_baht): .2f} Baht.')


i = inputShape()

volume = calculateSphere() if i == 1 else calculateCone(
) if i == 2 else calculateCylinder() if i == 3 else calculatePrism(
) if i == 4 else calculatePyramid() if i == 5 else None

calculatePrice(volume)