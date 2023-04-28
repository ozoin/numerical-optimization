import numpy as np
import math


#===EX1 PROBLEMS | 1 VARIABLEM===
def quartic(x):
    #correct for 0, but converges infinitely
    return x**4 - 3*x**2 + 2*x + 1

def fourth_degree_polynomial(x):
    #correct for point 1. but converges infinitely
    return 2*x**4 + 5*x**3 - 3*x**2 + 7*x - 8

def sixth_degree_polynomial(x):
    #correct for point 1
    return x**6 - 2*x**5 + 3*x**4 + 4*x**3 - 5*x**2 + 6*x - 7
def booth_func(x):
    #correct for point 0, but converges infinetly
    return (x + 2*x**2 - 7)**2 + (2*x + x**2 - 5)**2
def third_degree(x):
    #correct for point 0, but converges infinetly
    return x**3 - 5*x - 9
def cos_fun(x):
    #correct for point 1.
    return np.cos(x)-2*x**3

#===EX5 PROBLEMS | 2 VARIABLES===
def fun_2vars(x):
    #correct for point 0,0
    return 0.5*(x[0] - 4.5)**2 + 2.5*(x[1] - 2.3)**2



def test(x):
    return x**4+5*x**2+2

sixth_degree_polynomial_x0 = [1]
fourth_degree_polynomial_x0 = [1]
quartic_x0 = [1]
booth_func_x0 = [0]
cos_fun_x0 = [1]
third_degree_x0 = [0] 
#====


A = np.asmatrix(np.random.rand(100,3))
b = np.asmatrix(np.random.rand(100,1))
#Defining the Function
def quadratic_problem_iii(x): #x is 3d point e.g [1,1,1], Returns a scalar function value
    point = np.asmatrix(x)
    return np.asscalar(0.5*np.dot((np.dot(A,point.T) - b).T,(np.dot(A,point.T) - b)))