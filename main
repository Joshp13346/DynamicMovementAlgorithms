# CS 330, Fall 2024
# Project 1, Dynamic Movement
# Purpose: Main, exhibits the use of the Dynamic Movement Algorithms Update, Seek, Flee, and Arrive
# Author: Josh Phillips, jp0196@uah.edu
# Created: 9/29/24

import numpy
import math
import helpers
import movement
import steeringOutput

CONTINUE = 1
SEEK = 6
FLEE = 7
ARRIVE = 8

time = 0    # Simulation time

# This class is used to store the output of each function to return

class Character(object):
    def __init__(self):
        self.ID = 0 # Character ID
        self.steer = 2  # Steer value
        self.position = numpy.array([0.0, 0.0])  # 2D position vector (x, y)
        self.orientation = 0.0  # Orientation in radians
        self.velocity = numpy.array([0.0, 0.0])  # 2D velocity (vx, vy)
        self.rotation = 0.0  # Rotation speed
        self.linear = numpy.array([0.0, 0.0])  # 2D linear acceleration (ax, ay)
        self.maxLinear = 0.0    # Maximum linear acceleration
        self.angular = 0.0  # Angular acceleration
        self.maxAngular = 0.0  # Maximum angular acceleration
        self.maxVelocity = 0.0  # Maximum velocity
        self.maxRotation = 0.0  # Maximum rotation
        self.arriveRadius = 0.0  # Radius for arriving
        self.arriveSlow = 0.0  # Distance to start slowing down
        self.arriveTime = 0.0  # Time to reach the target
        self.colCollided = False    # Collision boolean
        self.target = self  # Establish target to reference in dynamic movement algorithms


deltaTime = 0.5
stopTime = 50

character1 = Character()
character1.ID = 101
character1.steer = CONTINUE

character2 = Character()
character2.ID = 102
character2.steer = FLEE
character2.position = numpy.array([-30.0, -50.0])
character2.velocity = numpy.array([2.0, 7.0])
character2.orientation = math.pi / 4
character2.maxVelocity = 8
character2.maxLinear = 1.5
character2.target = character1

character3 = Character()
character3.ID = 103
character3.steer = SEEK
character3.position = numpy.array([-50.0, 40.0])
character3.velocity = numpy.array([0.0, 8.0])
character3.orientation = 3 * math.pi / 2
character3.maxVelocity = 8
character3.maxLinear = 2
character3.target = character1

character4 = Character()
character4.ID = 104
character4.steer = ARRIVE
character4.position = numpy.array([50.0, 75.0])
character4.velocity = numpy.array([-9.0, 4.0])
character4.orientation = math.pi
character4.maxVelocity = 10
character4.maxLinear = 2
character4.target = character1
character4.arriveRadius = 4
character4.arriveSlow = 32
character4.arriveTime = 1

characters = [character1, character2, character3, character4]   # List of characters

filename = 'CS 330 Programming Assignment 1 output.txt' # Program output file
f = open(filename, 'w') # Will create file if one doesnt exist
# Iterate through each of the 4 characters and print to filename
for character in characters:
    print(time, character.ID, character.position[0],character.position[1], character.velocity[0], character.velocity[1], 
          character.linear[0], character.linear[1], character.orientation, character.steer, character.colCollided, sep = ", ", end = "\n", file=f)
f.close()

# Iterate through 50 time intervals at .5 intervals, totaling 100 time steps
while time < stopTime:
    time += deltaTime
    # Iterate through each of the 4 characters and update them based on their steer function
    for character in characters:
        if character.steer == CONTINUE:
            steering = steeringOutput.Result.steerContinue(character)
        elif character.steer == SEEK:
            steering = movement.seek(character)
        elif character.steer == FLEE:
            steering = movement.flee(character)
        elif character.steer == ARRIVE:
            steering = movement.arrive(character)

        character = helpers.update(deltaTime, character, steering)

    # Iterate through each of the 4 characters and print to filename
    f = open(filename, 'a')
    for character in characters:
        print(time, character.ID, character.position[0], character.position[1], character.velocity[0], character.velocity[1], character.linear[0], character.linear[1], 
          character.orientation, character.steer, character.colCollided, sep = ", ", end = "\n", file=f)
    f.close()
