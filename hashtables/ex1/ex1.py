"""
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
"""

def get_indices_of_item_weights(weights, _, limit):
    """
    YOUR CODE HERE
    """
    weight_table = {}

    # build table of k=weight v=[idxs]
    for idx, weight in enumerate(weights):
      # because there may be items of the same weight, the index is stored in an array
      if weight not in weight_table:
        weight_table[weight] = [idx] # first
      else:
        weight_table[weight].append(idx) # additional (only need two of them via rules)

    # loop again trying to locate the matching weight
    for weight in weights:
      needed_weight = limit - weight
    
      # special case for items with the same weight
      if needed_weight == weight and len(weight_table[weight]) > 1:
        idx1 = weight_table[weight][1] # this idx is always larger
        idx2 = weight_table[weight][0]
        return (idx1, idx2)
      
      if needed_weight in weight_table:
        if weight + needed_weight == limit:
          # found the 2nd weight
          idx1 = weight_table[weight][0]
          idx2 = weight_table[needed_weight][0]
          if idx1 > idx2: # don't understand the purpose of this rule but ok
            return (idx1, idx2)
          else:
            return (idx2, idx1)

    return None