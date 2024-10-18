##### Try to use map and reduce in the next 3 exercises
# 1)
# Create a function called "count_simba" that counts and returns
# the number of times that Simba appears in a list of
# strings. Example:
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#
from functools import reduce

def count_simba(strings: list[str]) -> int: 
    # Use map to create a list of counts of "Simba" in each string
    simba_counts = map(lambda s: s.count("Simba"), strings)
    
    # Use reduce to sum the counts together
    total_simba = reduce(lambda x, y: x + y, simba_counts)
    
    return total_simba
# 2)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
#

import pandas as pd

def get_day_month_year(dates:list[datetimes.date]) -> pd.DataFrame:
    # Use map to extract day, month, and year for each date
    day_month_year = map(lambda d: (d.day, d.month, d.year), dates)
    
    # Convert the mapped result into a pandas DataFrame
    df = pd.DataFrame(day_month_year, columns=["day", "month", "year"])
    
    return df

# 3) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#
from geopy.distance import distance

def compute_distance(coordinates):
    # Use map to calculate the distance between each pair of coordinates
    distances = map(lambda c: distance(c[0], c[1]).km, coordinates)
    
    # Convert the result to a list and return
    return list(distances)

#################################################
# 4)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#
def sum_general_int_list(lst):
    total_sum = 0
    for element in lst:
        if isinstance(element, int):
            # If the element is an integer, add it to the total sum
            total_sum += element
        elif isinstance(element, list):
            # If the element is a list, recursively call the function
            total_sum += sum_general_int_list(element)
    return total_sum



