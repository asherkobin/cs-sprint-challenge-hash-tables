# Your code here
from os import path

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # build index

    file_index = {}

    for abs_file_path in files:
      file_name = path.basename(abs_file_path)

      if file_name in file_index:
        file_index[file_name].append(abs_file_path)
      else:
        file_index[file_name] = [abs_file_path]
        
    # enumerate queries

    search_results = []

    for query in queries:
      if query in file_index:
        search_results.extend(file_index[query]) # if index contians query, add it to results
    
    return search_results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
