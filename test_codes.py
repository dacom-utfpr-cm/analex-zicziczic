# estados = [i for i in range (62)]
# print(estados)

# Create the dictionary
states = {}

# Automate for 'q0'
states['q0'] = {key: 'q2' for key in ['a', 'b', 'c', 'd']}

# Example of adding more states
for i in range(1, 3):  # Replace 3 with how many states you want
    states[f'q{i}'] = {key: f'q{i+1}' for key in ['a', 'b', 'c', 'd']}

# Print the resulting dictionary
import pprint
pprint.pprint(states)
