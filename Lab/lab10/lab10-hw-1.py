from math import sqrt

pi = 3.14

class Rectangle:
    def __init__(self,l:int,w:int) -> None:
        self.l = l
        self.w = w

    def is_square(self):
        if self.l == self.w:
            return 'This rectangle is square too.'
        else:
            return 'This rectangle is not square.'

    def area(self):
        return self.l * self.w

    def perimeter(self):
        return 2*self.l + 2*self.w
class Triangle:
    def __init__(self,*args) -> None:
        self.li = list(args)

    def is_right_triangle(self):
        self.li.sort()

        a,b,c = self.li

        if c**2 == a**2 + b**2:
            return 'This triangle is right triangle too.'
        else:
            return 'This triangle is not right triangle.'

    def area(self):
        s = self.perimeter() / 2
        return sqrt(s*(s-self.li[0])*(s-self.li[1])*(s-self.li[2]))

    def perimeter(self):
        return sum(self.li)

class Circle:
    def __init__(self,r:int) -> None:
        self.r = r

    def area(self):
        return pi*self.r**2
    
    def perimeter(self):
        return 2*pi*self.r
    


l = int(input("Enter rectangle length : "))  
w = int(input("Enter rectangle width : "))  
p1 = Rectangle(l,w)  
print(f'Area is {p1.area()}.')  
print(f'Perimeter is {p1.perimeter()}.')  
print(p1.is_square()) 

l1 = int(input("Enter triangle first side length : "))  
l2 = int(input("Enter triangle second side length : "))  
l3 = int(input("Enter triangle third side length : "))  
p2 = Triangle(l1,l2,l3)  
print(f'Area is {p2.area()}.')  
print(f'Perimeter is {p2.perimeter()}.')  
print(p2.is_right_triangle()) 

r = int(input("Enter circle radius : "))  
p3 = Circle(r)  
print(f'Area is {p3.area():.2f}.')  
print(f'Perimeter is {p3.perimeter():.2f}.')  