def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(r):
    circle_area = r*r*3.14
    return circle_area

radius = get_radius("반지름: ")

result = get_circle_area(radius)
print('원의 넓이는: ', result)
