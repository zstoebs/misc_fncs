"""
@author Zach Stoebner
@date 10-23-2020
@descrip very, very basic grad descent
"""

import numpy as np

### q3 - gradient descent
def compute_grad(x,y):
    return 2*(x-y) + y, x-2*(x-y)
    
def grad_descent(x,y,x_grad,y_grad,lr):
    return x - lr*x_grad, y - lr*y_grad

def run_gd(start_x,start_y,fnc,iters,lr=0.05):
    n = 0
    x,y = start_x, start_y
    while n <= iters:
        print("Step %d" % (n), fnc(x,y))
        x_grad, y_grad = compute_grad(x,y)
        x,y = grad_descent(x,y,x_grad,y_grad,lr)
        n += 1

if __name__ == "__main__":
    f = lambda x,y : (x-y)**2 + x*y
    run_gd(2,3,f,20,0.1)
