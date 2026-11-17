import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    # TODO - Complete the function so it loads the data from the file into a list
    # The function returns a tuple that contains the list of values and the total number 
    # of values in the column
    numbers = []
    with open (filepath, 'r') as infile:
        for line in infile:
            pass


def calculate_average(numbers:list)->float:
    # TODO - Complete the function to return the average of the list of numbers
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def get_max_and_min(numbers:list)->tuple[float, float]:
    # TODO - Complete the function to return a tuple with the maximum and minimum
    # values in the list, in that order
    if not numbers:
        return 0
    return (max(numbers),min(numbers))

def calculate_variance(numbers:list)->float:
    # TODO - Complete the function to return the variance of the numbers in the list
    if len(numbers) <= 1:
        return 0
    
    mean = sum(numbers) / len(numbers)
    sum_dev = sum((number - mean) ** 2 for number in numbers)
    return sum_dev / (len(numbers) - 1)

def calculate_std_dev(numbers:list)->float:
    # TODO - Complete the function to return the standard deviation of the numbers in the list
    pass

def calculate_median(number:list)->float:
    # TODO - Complete the function to return the median of the numbers in the list
    pass