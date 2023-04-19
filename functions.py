

def test_function_1var(x):
    return x**2+1
def test_function_2var(x):
    return x[0]**3+3*x[1]+10

def quartic(x):
    return x**4 - 3*x**2 + 2*x + 1

def fifth_degree(x):
    return 2*x**5 - 5*x**4 + 3*x**3 + x**2 - 2*x + 1

def exponential_plus_c(x):
    c = 3
    return math.exp(x) + c

def rational(x):
    return (x**3 - x**2 + 1)/(x - 1)

def third_degree(x):
    return -7*x**2+0.5*x-7

def fun_2vars(x):
    return 0.5*(x[0] - 4.5)**2 + 2.5*(x[1] - 2.3)**2

def cos_fun(x):
    return np.cos(x)-2*x**3