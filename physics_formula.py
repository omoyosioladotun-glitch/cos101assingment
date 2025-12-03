gravitational_force = "a"
potential_energy ="b"
moment ="c"
speed = "d"
pressure = "e"

print ("a=gravitational force"
       "b=potential energy"
       "c=moment"
       "d=speed"
       "e=pressure")
user = input("what formula do you want to solve")
if user == gravitational_force:
    gravitational_constant = 6.67 * 10**-11
    mass1 = int(input("enter mass 1"))
    mass2 = int(input("enter mass 2"))
    radius =int(input("enter radius"))
    gravitational_force = gravitational_constant*mass1*mass2/radius**2
    print (gravitational_force)
elif user == potential_energy:
    mass =int(input("enter mass"))
    gravity =int(input("enter gravity"))
    height =int(input("enter height"))
    potential_energy = mass*gravity*height
    print(potential_energy)
elif user == moment:
    force =int(input("enter force"))
    distance =int(input("enter distance"))
    moment = force*distance
    print(moment)
elif user == speed:
    distance =int(input("enter distance"))
    time =int(input("enter time"))
    speed = distance/time
    print(speed)
elif user == pressure:
    force =int(input("enter force"))
    area =int(input("enter area"))
    pressure = force/area
    print(pressure)
