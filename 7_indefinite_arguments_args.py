"""
def tea_order(customer_name, tea_type, **kwargs): # don't need to use "args", you can use any other word, just have to have the "*" | Arg is a tuple                # kwargs ** makes it into a dictionary, great for key words. "*" doesn't handel keywords
    print(customer_name, "ordered a", tea_type, "tea")
    for key, value in kwargs.items():
        print(" + Add", key, ":", value)
"""
        
def tea_order(customer_name, tea_type, *args, **kwargs): #posital arguemnts first then keywords (*arg first)
    print(customer_name, "ordered a", tea_type, "tea")
    for arg in args:
        print(" + add", arg)
    for key, value in kwargs.items():
        print(" + Add", key, ":", value)
 
tea_order("Alice", "chamolle")
tea_order("Bob", "black", milk="oat")
tea_order("Tony", "black", "oat", sweetener="honey")






# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).

# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"