def sort_list_last_element(tuples_list):
  return sorted(tuples_list, key=lambda x: x[-1])

# Example usage
test_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sort_list_last_element(test_list))

# Output: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
