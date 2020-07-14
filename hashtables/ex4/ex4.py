import math

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    num_table = {} # key is abs, value is 0 for found pair, otherwise not
    list_of_pairs = []
    
    # iterate over array and check for pos/neg

    for num in a:
      key = abs(num)
      
      if key in num_table:
        # if pair found, update entry, add to result
        if num_table[key] + num == 0:
          num_table[key] = 0 # prevents duplicates
          list_of_pairs.append(key)
      else:
        # add entry
        num_table[key] = num

    return list_of_pairs


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
