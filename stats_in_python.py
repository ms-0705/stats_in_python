import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    # Complete the function so it loads the data from the file into a list
    # The function returns a tuple that contains the list of values and the total number 
    # of values in the column
    numbers = []
    with open (filepath, 'r') as infile:
        for line_num, line in enumerate(infile, start=1):
            try:
                  num = line.split("\t")[column]
                  num = float(num)
            except IndexError:
               print(f"Exiting: There is no valid 'list index' in column {column} in line {line_num} in file: {filepath}")
               sys.exit()
            except ValueError:
                continue
            if math.isnan(num):
               continue
           
            numbers.append(num)

    if not numbers:
        print(f"Error: There were no valid number(s) in column {column} in file: {filepath}")
        sys.exit()
    return (numbers,line_num)

def calculate_average(numbers:list)->float:
    # Complete the function to return the average of the list of numbers
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def get_max_and_min(numbers:list)->tuple[float, float]:
    # Complete the function to return a tuple with the maximum and minimum
    # values in the list, in that order
    if not numbers:
        return (0.0, 0.0)
    return (max(numbers),min(numbers))

def calculate_variance(numbers:list)->float:
    # Complete the function to return the variance of the numbers in the list
    if len(numbers) <= 1:
        return 0
    mean = sum(numbers) / len(numbers)
    sum_dev = sum((number - mean) ** 2 for number in numbers)
    return sum_dev / (len(numbers) - 1)

def calculate_std_dev(numbers:list)->float:
    # Complete the function to return the standard deviation of the numbers in the list
    variance = calculate_variance(numbers)
    return math.sqrt(variance)

def calculate_median(numbers:list)->float:
    # Complete the function to return the median of the numbers in the list
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) % 2 != 0:
        middle_index = len(numbers) // 2
        return float(sorted_numbers[middle_index])
    index_right = len(numbers) // 2
    middle_two_num = sorted_numbers[index_right - 1] + sorted_numbers[index_right]
    return middle_two_num / 2