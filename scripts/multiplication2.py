# Input the size of multiplication table
table_size = int(input("Enter the size of the multiplication table: "))

# Print the heading of each column
print('   |', end='')
for i in range(1, table_size + 1):
    print(str(i).rjust(5), end='')
print('\n---+' + '-----' * table_size)

# Loop over all numbers from 1 to the specified table size
for i in range(1, table_size + 1):
    # Print the number label on the left side
    print(str(i).rjust(3) + '|', end=' ')
    
    # Loop over all numbers from 1 to the specified table size
    for j in range(1, table_size + 1):
        # Print the product, padded to four digits, followed by a space
        print(str(i * j).rjust(4), end=' ')
    
    # After the loop, print a newline to end the row
    print()
