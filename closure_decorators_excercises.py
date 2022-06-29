# Closures-Decorators Exercises

# Closure Exercise
# Using a closure, create a function, multiples_of(n) which we can use to
# create generators that generate multiples of n less than a given number.

def multiples_of(num):
    # enclose multi function
    def multi(max_num):
        i = 1
        while i * num < max_num:
            yield i * num
            i += 1

    return multi


m3 = multiples_of(3)
m3_under30 = m3(30)
m7_under30 = multiples_of(7)(30)

print(type(m3_under30))
# output: <class 'generator'>

print(*m3_under30)
# output: 3 6 9 12 15 18 21 24 27

print(*m7_under30)


# output: 7 14 21 28
# ----------------------------------------------------------------------

# Decorators Exercise 1
# @make_upper – make every letter of a string returned from the decorated
# function uppercase.

def make_upper(original):
    def upper_case():
        return original().upper()

    return upper_case


@make_upper
def hello_world():
    return 'hello young, good day!!'


print(hello_world())  # output: HELLO YOUNG, GOOD DAY!!


# -----------------------------------------------------------------------

# Decorators Exercise 2
# @print_func_name – print the name of the decorated function before
# executing the function.

def print_func_name(original):
    def printing():
        print(f"{original.__name__} is running...")
        return original()

    return printing


@print_func_name
def my_func():
    print('Python is fun!!')


my_func()  # output: my_func is running...


# Python is fun!!
# ----------------------------------------------------------------------

# Decorators Exercise 3
# @give_name(name) – concatenate the given name at the end of a string
# returned from the decorated function.
def give_name(original):
    def concatenate(name):
        return original(name) + ' ' + name

    return concatenate


@give_name
def greeting(name):
    return 'Hello'


print(greeting('Theresa'))  # output: Hello Theresa


# ---------------------------------------------------------------------

# Decorators Exercise 4
# @print_input_type – print a data type of the input argument before
# executing the decorated function.

def print_input_type(original):
    def data_printer(n):
        print(f'The input data type is {type(n)}')
        return original(n)

    return data_printer


@print_input_type
def square(n):
    return n ** 2


print(square(3.5))  # output: The input data type is <class 'float'>


# 12.25
# -------------------------------------------------------------------

# Decorators Exercise 5
# @check_return_type(return_type) – check if the return type of the
# decorated function is return_type and print the result before executing
# the function.

def check_return_type(original):
    def checker(n):
        if type(original(n)) == type(''):
            return '=========Error!!'
        else:
            print(f'The return type is {type(original(n))}')
            return original(n)

    return checker


@check_return_type
def square(n):
    return n ** 2


print(square(6))  # output: =========Error!!


# The return type is NOT <class 'str'>
# 36

@check_return_type
def square(n):
    return n ** 2


print(square(2.9))  # output: The return type is <class 'float'>

# 8.41
# ------------------------------------------------------------------------

# Decorators Exercise 6
# @execute_log – write a function execution log on the log file. (log below)
system_log = []


def execute_log(original):
    from datetime import datetime

    def sys_logs(*args, **kwargs):
        system_log.append(str(datetime.now()) + ' ' + original.__name__)
        return original(*args, **kwargs)

    return sys_logs


@execute_log
def multiply(*nums):
    mult = 1
    for n in nums:
        mult *= n
    return mult


@execute_log
def hello_world():
    return 'hello world!!'


print(multiply(6, 2, 3))  # 36
print(hello_world())  # hello world!!
print(multiply(2.2, 4))  # 8.8
print(hello_world())  # hello world!!

# function_execution.log
# 2020-05-01 13:55:53.059315 multiply
# 2020-05-01 13:55:53.060312 hello_world
# 2020-05-01 13:55:53.060314 multiply
# 2020-05-01 13:55:53.060323 hello_world
