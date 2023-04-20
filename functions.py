

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
    return x**3 - 5*x - 9

def fun_2vars(x):
    return 0.5*(x[0] - 4.5)**2 + 2.5*(x[1] - 2.3)**2

def cos_fun(x):
    return np.cos(x)-2*x**3

def cos_exp(x):
    return 3*math.cos(x) - math.exp(x)


A = np.asmatrix(np.random.rand(100,3))
b = np.asmatrix(np.random.rand(100,1))
#Defining the Function
def quadratic_problem_iii(x): #x is 3d point e.g [1,1,1], Returns a scalar function value
    point = np.asmatrix(x)
    return np.asscalar(0.5*np.dot((np.dot(A,point.T) - b).T,(np.dot(A,point.T) - b)))