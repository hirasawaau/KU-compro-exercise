def What(s: str):
    global type
    if ord(s[0]) < 97:
        type = 'Photobook'
        return 'Photobook'
    else:
        type = 'Album'
        return 'Album'


def SStatus():
    global type
    return type


def RReal(s: str):
    firstCode = ord(s[0])
    lastCode = ord(s[-1])

    firstCode += 1

    if firstCode == lastCode:
        return True
    else:
        return False


type = 'Dont Check'
code = input()

What(code)
print(SStatus())

print(RReal(code))
