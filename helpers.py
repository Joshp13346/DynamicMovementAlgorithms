# CS 330, Fall 2024
# Project 1, Dynamic Movement
# Purpose: This file stores helper functions
# Author: Josh Phillips, jp0196@uah.edu
# Created: 9/29/24

import numpy
import math

# This function takes in a vector and returns the length of said vector
def length(vector):
    return math.sqrt(vector[0]**2 + vector[1]**2)


# This function takes in a vector input, and returns the normalized vector
def normalize(vector):
    vectorLength = length(vector)

    if vectorLength != 0:
        return numpy.array([vector[0] / vectorLength, vector[1] / vectorLength])
    else:
        return numpy.array([0, 0])


# Dynamic Update Function
def update(deltaTime, character, steering):

    # Newton-Euler-1 integration
    character.position += character.velocity * deltaTime
    character.orientation += character.rotation * deltaTime

    # Keep orientation in the range <0, 2*pi>
    character.orientation %= (2 * numpy.pi)

    # Update velocity and rotation
    character.velocity += steering.linear * deltaTime
    character.rotation += steering.angular * deltaTime

    # Update linear and angular acceleration
    character.linear = steering.linear
    character.angular = steering.angular

    # Ensure velocity doesn't exceed maximum
    if length(character.velocity) > character.maxVelocity:
        character.velocity = character.maxVelocity * normalize(character.velocity)

    # Ensure linear acceleration doesn't exceed maximum
    if length(character.linear) > character.maxLinear:
        character.linear = character.maxLinear * normalize(character.linear)

    # Ensure rotation doesn't exceed maximum
    if abs(character.rotation) > character.maxRotation:
        character.rotation = character.maxRotation * numpy.sign(character.rotation)

    # Ensure angular acceleration doesn't exceed maximum
    if abs(character.angular) > character.maxAngular:
        character.angular = character.maxAngular * numpy.sign(character.angular)

    return character
