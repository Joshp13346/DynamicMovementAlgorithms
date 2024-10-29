# CS 330, Fall 2024
# Project 1, Dynamic Movement
# Purpose: Dynamic Movement Functions
# Author: Josh Phillips, jp0196@uah.edu
# Created: 9/29/24

import helpers
import steeringOutput
import numpy

def seek(character):
    # Calculates the seek steering vector towards a target

    seekOutput = steeringOutput.Result()  # Initialize seek steering output
    
    # Calculate direction towards the target
    seekOutput.linear = numpy.array([character.target.position[0] - character.position[0],
                     character.target.position[1] - character.position[1]])
    
    # Normalize the direction and scale it by maxLinear
    seekOutput.linear = helpers.normalize(seekOutput.linear)
    seekOutput.linear = numpy.array([seekOutput.linear[0] * character.maxLinear,
                     seekOutput.linear[1] * character.maxLinear])
    
    seekOutput.angular = 0
    
    return seekOutput


def flee(character):
    # Calculates the flee steering vector from a target

    fleeOutput = steeringOutput.Result() # Create an instance of the Result class

    # Calculate flee direction
    fleeOutput.linear = numpy.array([character.position[0] - character.target.position[0], character.position[1] - character.target.position[1]])

    # Normalize flee direction and scale by maxLinear
    fleeOutput.linear = helpers.normalize(fleeOutput.linear)
    fleeOutput.linear = numpy.array([fleeOutput.linear[0] * character.maxLinear,
                        fleeOutput.linear[1] * character.maxLinear])
    
    fleeOutput.angular = 0

    return fleeOutput


def arrive(character):
    # Calculates arrive steering vector towards a target
    arriveOutput = steeringOutput.Result()  # Initialize arrive steering output
    
    # Calculate direction towards the target
    direction = (character.target.position[0] - character.position[0], character.target.position[1] - character.position[1])
    distance = helpers.length(direction)

    # Determine arrival speed based on distance
    if distance < character.arriveRadius:
        arriveSpeed = 0
    elif distance > character.arriveSlow:
        arriveSpeed = character.maxVelocity
    else:
        arriveSpeed = character.maxVelocity * (distance / character.arriveSlow)

    # Calculate arriveVelocity
    arriveVelocity = helpers.normalize(direction)
    arriveVelocity = (arriveVelocity[0] * arriveSpeed, 
                       arriveVelocity[1] * arriveSpeed)

    # Calculate the linear steering vector
    arriveOutput.linear = numpy.array([arriveVelocity[0] - character.velocity[0], arriveVelocity[1] - character.velocity[1]])
    
    # Scale linear by time to reach the target
    arriveOutput.linear = numpy.array([arriveOutput.linear[0] / character.arriveTime, arriveOutput.linear[1] / character.arriveTime])

    # Scale linear velocity to maxLinear value
    if helpers.length(arriveOutput.linear) > character.maxLinear:
        arriveOutput.linear = helpers.normalize(arriveOutput.linear)
        arriveOutput.linear = numpy.array([arriveOutput.linear[0] * character.maxLinear, arriveOutput.linear[1] * character.maxLinear])

    return arriveOutput
