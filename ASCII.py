
# Initialize an empty dictionary
d = {}

# Loop through the alphabet from 'a' to 'z'
for i in range(97, 123):
  # Add a key-value pair to the dictionary, where the key is the character and the value is its ASCII value
  d[chr(i)] = i

# Print the resulting dictionary
print(d)
