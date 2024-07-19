        #THE SPEED DETACTOR 
# Write a program that takes the speed of a car as input e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
#    > For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.

# print("Enter the speed of your car")
spd_limit = 70
demerit_points_per_5km = 5
max_demerit_points = 12
max_speed ="OK!"
over_speed = "License suspended! Visit KENHA"

def check_speed(speed):
    if speed < spd_limit:
      print(max_speed)
      return max_speed
    else:
        demerit_points = (speed - spd_limit) // int(demerit_points_per_5km)
        if demerit_points > max_demerit_points:
            print(over_speed)
            return over_speed
        else:
            print(f"Points: {demerit_points}")  

speed = int(input("Enter the speed of the car: ")) 
check_speed(speed)

    # THE END OF THE PROGRAM 