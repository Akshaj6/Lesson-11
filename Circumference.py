def calculate_circumference(radius):
    pi = 3.14
    circumference = 2 * pi * radius
    return circumference
radius = float(input("Enter the length of the radius of the circle :"))
print("The circumference of the circle is ", calculate_circumference(radius))