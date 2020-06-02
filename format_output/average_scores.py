"""
Program: test_average_scores.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: calculate the average test scores
"""


def average():
    score_one = input('Please Enter Score 1:')
    score_two = input('Please Enter Score 2:')
    score_three = input('Please Enter Score 3:')

    return (float(score_one) + float(score_two) + float(score_three)) / 3
