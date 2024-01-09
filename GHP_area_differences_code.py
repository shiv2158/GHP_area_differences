#import necessary libraries
import math
import numpy as np


try:
    #arrays to store input coordinates
    x_coordinates = []
    y_coordinates = []

    #user input of coordinates
    for i in range(1, 7):
        x_coordinates.append(float(input(f"Enter x coordinate {i}:")))
        y_coordinates.append(float(input(f"Enter y coordinate {i}:")))

    #translation of coordinates
    minx = min(x_coordinates)
    miny = min(y_coordinates)
    for i in range(6):
        x_coordinates[i] = x_coordinates[i] - minx
        y_coordinates[i] = y_coordinates[i] - miny

    #determining whether the rectangle has sides parallel to the axes on a plane
    #based on the number of points with an x coordinate equal to the maximum x coordinate
    count = 0
    for i in range(len(x_coordinates)):
        if x_coordinates[i] == max(x_coordinates):
            count += 1

    #if the rectangle does not have sides parallel to the axes on a plane
    if count == 1:
        #translating the rectangle so one vertex is at the origin
        basex = x_coordinates[y_coordinates.index(0)]
        for i in range(6):
            x_coordinates[i] = x_coordinates[i] - basex

        #calculating the angle by which the rectangle should be rotated
        angle = -math.atan(y_coordinates[x_coordinates.index(max(x_coordinates))]/(max(x_coordinates)))
        #the rotation matrix
        rotation_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        #dot product of rotation matrix and each point on the rectangle
        for i in range(6):
            [x_coordinates[i], y_coordinates[i]] = np.round(np.dot(rotation_matrix, [x_coordinates[i], y_coordinates[i]]), 3)

    #calculating the length and width of the largest rectangle
    lenside1 = max(y_coordinates)
    lenside2 = max(x_coordinates)

    for i in range(6):
        #determining which point intersects one side of the larger rectangle
        if (x_coordinates[i] != max(x_coordinates) and x_coordinates[i] != min(x_coordinates)):
            #determining one dimension of the smallest rectangle
            lenshortside1 = min(x_coordinates[i], (max(x_coordinates) - x_coordinates[i]))
                
        #determining which point intersects the second side of the larger rectangle
        if (y_coordinates[i] != max(y_coordinates) and y_coordinates[i] != min(y_coordinates)):
            #determining the second dimension of the smallest rectangle
            lenshortside2 = min(y_coordinates[i], (max(y_coordinates) - y_coordinates[i]))

    #calculation of the difference in areas between the larger rectangle and the smallest rectangle
    areadifference = lenside1 * lenside2 - lenshortside1 * lenshortside2
    
    #reporting area difference
    print(f"The difference between the area of the larger recatangle and the smallest rectangle is: {np.round(areadifference, 3)}")

#an error indicates that invalid coordinates were entered
#if there is an error, this is run
except:
    #reporting the error
    print("There is an error. Please enter valid coordinates.")
