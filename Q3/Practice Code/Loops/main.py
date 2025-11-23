

# Direct iteration over elements

fruits: list = ["apple", "banana", "cherry"]

for a in fruits:
    print(a)


# Iteration using indexes
#            0         1         2
fruits = ["apple", "banana", "cherry"]

# 3
fruits_length = len(fruits)

#        0, 1, 2
for i in range(3):
    print(fruits[i])



# Break example in while loop
while True:
    user_input = input("Type 'exit' to stop: ")
    if user_input.lower() == 'exit':
        print("Goodbye!") # user entered 'exit'
        break # breaking the loop



# Continue example in for loop
shopping_list = ["apples", "oranges", "bananas", "chocolate"]

for item in shopping_list:
    if item == "bananas":  # bananas are out of stock
        continue  # skip this item
    print(f"Buying {item}")