"""
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
"""

def get_indices_of_item_weights(weights, _, limit):
    """
    YOUR CODE HERE
    """
    weight_table = {}

    for idx, weight in enumerate(weights):
      weight_table[weight] = [limit - weight, idx]

    for weight in weight_table:
      needed_weight = weight_table[weight][0]
      if needed_weight in weight_table:
        if weight + needed_weight == limit:
          idx1 = weight_table[weight][1]
          idx2 = weight_table[needed_weight][1]
          if idx1 > idx2:
            return (idx1, idx2)
          else:
            return (idx2, idx1)

    return None

print(get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 0, 21))
print(get_indices_of_item_weights([ 4, 4 ], 0, 8))