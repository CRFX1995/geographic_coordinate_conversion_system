#!/usr/bin/env python
"""
    Team 10B – PYTHON PROGRAM
    Offers the user a menu to convert from geographic
    (latitude/longitude) coordinates to vector formatting.
    
    For testing purposes:
        Louisville:
            Operation One: 38° 13′ 31.2″ N, 85° 44′ 30″ W
            Operations Two and Four: 38.225333, -85.741667
        Lexington:
            Operation One: 38° 1′ 47″ N, 84° 29′ 41″ W
            Operations Two and Four: 38.029722, -84.494722 
        Cincinnati:
            Operation One: 39° 6′ 0″ N, 84° 31′ 0″ W
            Operations Two and Four: 39.1, -84.516667
"""

import os
import math

# Operation 1: Geographic Coordinate Conversion
#   From degrees/minutes/seconds to decimal degrees:
def operation1(degrees, minutes, seconds):
	tot = degrees + (minutes / 60.0) + (seconds / 3600)
	return tot

# Operation 2: Geographic Coordinate to Vector
#   From decimal degrees to vector in î and ĵ:
def operation2(lat1, long1, lat2, long2):
    cearth = 40000.0
    kft = 3280.4

    x1 = long1 * ((cearth/360.0) * kft)
    y1 = lat1 * ((cearth/360.0) * kft)
    x2 = long2 * ((cearth/360.0) * kft)
    y2 = lat2 * ((cearth/360.0) * kft)

    xvect = x2 - x1
    yvect = y2 - y1

    print("\nThe ij vector from the first coordinate to the second coordinate in feet is: %.3fi + %.3fj" % (xvect, yvect))
    return None


# Operation 4: The Haversine Method
#   Compares the result of Operation 2 with that of a more technical method
def operation4(lat1, long1, lat2, long2):
    # First, a run through of operation2's functions:
    cearth = 40000.0
    kft = 3280.4

    x1 = long1 * ((cearth/360.0) * kft)
    y1 = lat1 * ((cearth/360.0) * kft)
    x2 = long2 * ((cearth/360.0) * kft)
    y2 = lat2 * ((cearth/360.0) * kft)

    xvect = x2 - x1
    yvect = y2 - y1
    
    # Now convert to r/theta:
    xvectrad = math.radians(xvect)
    yvectrad = math.radians(yvect)
    rop2 = math.sqrt((xvect ** 2) + (yvect ** 2))
    thetaop2 = math.degrees(math.atan2(yvectrad, xvectrad))
    
    # Angle correction
    #   Quadrant III:
    if xvect < 0 and yvect < 0:
        thetaop2 += 360
    #   Quadrant IV
    elif xvect > 0 and yvect < 0:
        thetaop2 = 360 + thetaop2


    # Now begin the Haversine calculations:
    dlong = long2 - long1
    dlat = lat2 - lat1

    # Some constants...let's use feet because the distances are small:
    dkm = 12742
    dmi = 7912
    dft = dmi * 5280

    # From degrees to radians (for the trig functions)
    lat1rad = math.radians(lat1)
    long1rad = math.radians(long1)
    lat2rad = math.radians(lat2)
    long2rad = math.radians(long2)
    dlongrad = math.radians(dlong)
    dlatrad = math.radians(dlat)

    a = (((math.sin(dlatrad / 2)) ** 2) + (math.cos(lat1rad) * math.cos(lat2rad) * ((math.sin(dlongrad / 2)) ** 2)))
    rhav = dft * math.asin(math.sqrt(a))
    thetahav = math.degrees(math.atan((math.sin(dlongrad) * math.cos(lat2rad)) / ((math.cos(lat1rad) * math.sin(lat2rad)) - (math.sin(lat1rad) * math.cos(lat2rad) * math.cos(dlongrad)))))
    
    # Angle correction
    #   Quadrant II
    if xvect < 0 and yvect > 0:
        thetahav = 180.0 + thetahav
    #   Quadrant III
    elif xvect < 0 and yvect < 0:
        thetahav += 180
    #   Quadrant IV
    elif xvect > 0 and yvect < 0:
        thetahav = 360 + thetahav
    
    # Printing the results:
    print("\nThe Haversine vector from the first coordinate to the second coordinate in feet is: %.3f / %.3f degrees" % (rhav, thetahav))
    print("Operation 2's polar vector from the first coordinate to the second coordinate is: %.3f / %.3f degrees" % (rop2, thetaop2))
    print("The difference is a distance of %.3f feet, %.3f degrees" % (math.fabs(rhav - rop2), math.fabs(thetahav - thetaop2)))
    return None



# Demonstration of functionality:
menu = 0

# The Main Menu
while True:
    os.system('CLS')

    print("Log in successful. Welcome to the Geographic Coordinate Conversion System.")
    print("\nPlease choose an option:")
    print("Operation 1 (convert DMS to decimal degrees)")
    print("Operation 2 (convert decimal degrees to vector coordinates)")
    print("Operation 3 (quit)")
    print("Operation 4 (utilise the Haversine formula)\n")

    menu = int(input())

    if menu == 1:   # Operation 1
        print("\nPlease enter the unsigned number of degrees:", end=" ")
        degrees = float(input())
        print("Please enter the unsigned number of minutes:", end=" ")
        minutes = float(input())
        print("Please enter the unsigned number of seconds:", end=" ")
        seconds = float(input())

        decimaldegrees = operation1(degrees, minutes, seconds)
        print("\nThe decimal degrees for the coordinate you entered is: %.3f." % decimaldegrees)
        os.system("pause")

    elif menu == 2:   # Operation 2
        print("\nPlease enter the latitude of your first coordinate in decimal degrees:", end=" ")
        lat1 = float(input())
        print("Please enter the longitude of your first coordinate in decimal degrees:", end=" ")
        long1 = float(input())
        print("Please enter the latitude of your second coordinate in decimal degrees:", end=" ")
        lat2= float(input())
        print("Please enter the longitude of your second coordinate in decimal degrees:", end=" ")
        long2= float(input())

        operation2(lat1, long1, lat2, long2)

        print("")
        os.system("pause")

    elif menu == 3:   # Quit
        break

    elif menu == 4:   # Operation 4
        print("\nPlease enter the latitude of your first coordinate in decimal degrees:", end=" ")
        lat1 = float(input())
        print("Please enter the longitude of your first coordinate in decimal degrees:", end=" ")
        long1 = float(input())
        print("Please enter the latitude of your second coordinate in decimal degrees:", end=" ")
        lat2= float(input())
        print("Please enter the longitude of your second coordinate in decimal degrees:", end=" ")
        long2= float(input())

        operation4(lat1, long1, lat2, long2)

        print("")
        os.system("pause")
        
    else:   # To catch any weird input:
        print("\nSorry, could you please try that again?")
        os.system("pause")

# Bidding the user farewell when quitting:
os.system('CLS')
print("Thanks for playing!\n")
os.system("pause")

