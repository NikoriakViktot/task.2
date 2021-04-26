# Task 1

# Run the python interpreter via the terminal. Get familiar with running python commands in the terminal, work with output, etc.*


# Task 2

# Create a python program named “task2”, and use the built-in function `print` in it several times. Try to pass “sep”, “end” params and pass several parameters separated by commas.

# Also, provide a comment text above each print statement, mentioned above, with the expected output after execution of the particular print statement.

# (Ex.
# ‘hello world’
# print(“hello world”)
print('Привіт')
print('Привіт' + ' Друзі!')
print(1, 2, 3, sep='|')
print(1, 2, 3, sep=f"\n{'-' * 10}\n")
a = '1'
b = '2'
d = '3'
print(a, b, d, end='*')
print("3 2 1", end='')
print()
# Task 3

# Write a program, which has two print statements to print the following text (capital letters “O” and “H”, made from “#” symbols):

#########
#       #
#       #
#       #
#########

#       #
#       #
#########
#       #
#       #
# Pay attention that usage of spaces is forbidden, as well as creating the whole result text string using “”” ”””, use ‘\n’ and ‘\t’ symbols instead.
O = "O"
H = "H"

print(O*9,
      O+'\t'+O,
      O+'\t'+O,
      O+'\t'+O,
      O*9, sep='\n', end='\n\n')
print(
    H+'\t'+H,
    H+'\t'+H,
    H*9,
    H+'\t'+H,
    H+'\t'+H, sep='\n', end='\n')
