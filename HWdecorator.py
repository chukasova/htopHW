#----decorator-----------

def counter(f):
    def _wrap_count(*args, **kwargs):
        res = f(*args, **kwargs)
        _wrap_count.calls += 1
        return res

    name_decorated.append(f.__name__)
    _wrap_count.calls = 0
    return _wrap_count

name_decorated = []


def separate(fn):
    def wrapped(*args, **kwargs):
        print("-"*10)
        print("Call function with name: {}".format(fn.__name__))
        a = fn(*args, **kwargs)
        print("-"*10)
        return a
    separate_line.append(fn.__name__)
    return wrapped

separate_line = []


def wrap(f):
    def wrapper(*args, **kwargs):
        print("args: ", args)  # kwargs
        res = f(*args, **kwargs)
        print("result: ", res)
        return res
    enter_data.append(f.__name__)
    return wrapper


enter_data = []

#-----function list------


@separate
def print_f():
    print("exemple 1")
print_f()



@wrap
def add(a, b):
    return(a + b)
print(add(1, 3))



@wrap
def many(*arg, **kwargs):
    print(arg)
    print(kwargs)
many(1, 2, 3, "milk", coffe="black")



@wrap
def multi(a, b):
    res = a*b
    return(res)
print(multi(2, 3))


@counter

def square(x):
    res = x**2
    return(res)
print(square(3))
print("count number of request = ", square.calls)


@counter
def chet(a):
    if a%2==0:
        print(i, "ok")
    else:
        print(i, "ne ok")
for i in range(1, 10):
    chet(i)

print("count number of request = ", chet.calls)



@separate
def lam_f(n):
    return lambda x: x + n
rez = lam_f(3)
print(rez(3))



@counter
def clock_to_min(number_clock):
    return number_clock*60
data_clock = [1, 3, 5, 10]
numder_min = list(map(clock_to_min, data_clock))
print(numder_min)
print("count number of request = ", clock_to_min.calls)



print("decorated function number of request = ", name_decorated)
print("decorated function separate line = ", separate_line)
print("decorated function enter_data = ", enter_data)


