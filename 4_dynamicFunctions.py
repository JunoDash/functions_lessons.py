# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.
numbers = [10, 5, 1, 6, 7]
def all_positives(list):
    for number in list:
        if number <= 0:
            return False
    return True
print(all_positives(numbers))




# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.

def sum_less(list):
    for number in list:
        if number < 0 or number > 1000:
            return
    return sum(list)

print(sum_less(numbers))



# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.
def count_event(list):
    odd = len(list)
    for number in list:
        if number % 2 == 0:
            list.pop(number)
    odd =- len(list)

count_event(list)