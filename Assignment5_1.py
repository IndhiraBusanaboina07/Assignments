from math import pi

 

class Circle:

    pass

 

def create(radius):

    t=Circle()

    t.radius=radius

    return t

 

def perimeter(t):

    return 2*pi*(t.radius)

 

def area(t):

    return pi*t.radius*t.radius

   

 

def info(t):

    return f'Circle Radius={t.radius}'

 

def draw(t):

    print(info(t))

def test_Circle(radius):

    t=create(radius)

    draw(t)

    print(f'Area={area(t)}')

    print(f'Perimeter={perimeter(t)}')  


test_Circle(3)      
