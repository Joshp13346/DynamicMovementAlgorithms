# CS 330, Fall 2024
# Project 1, Dynamic Movement
# Purpose: This file stores the class to create the steering output objects
# Author: Josh Phillips, jp0196@uah.edu
# Created: 9/29/24

import numpy

class Result:
    def __init__(self):
        self.linear = numpy.array([0, 0])  # Instance variable initialized to (0, 0)
        self.angular = 0       # Instance variable initialized to 0

    # This method returns the current steering based on the character's current linear and angular acceleration values
    def steerContinue(character):
        continueOutput = Result()    # Initialize continue steering output
        continueOutput.linear = character.linear    # Maintain linear acceleration value
        continueOutput.angular = character.angular  # Maintain angular acceleration value
        return continueOutput
