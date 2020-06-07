"""
IN
[
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
]

OUT
[1, 2]
"""


def intersection(arrays):
    """
    YOUR CODE HERE
    """
    list_count = len(arrays) # if count is this, we have an intersection
    counting_table = {}
    result_list = []

    # create a counting hash table
    
    for array in arrays:
      for num in array:
        if num in counting_table:
          counting_table[num] += 1
          if counting_table[num] == list_count: # only happens once so it covers duplicate entries
            result_list.append(num) # winner!
        else:
          counting_table[num] = 1

    return result_list


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
