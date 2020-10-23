"""
@author Zach Stoebner
@date 10-23-2020
@descrip Hill climbing -- Steepest ascent and random restart w/ steepest ascent
            Future mods: generalize functions to take:
                            custom neighbord policies and evals,
                            disc and cont obj functions,
                            matplot of obj fnc and solution path
@kw optimization, AI
"""

import numpy as np
import argparse

def neighbors(node,obj_fnc):
    
    nbs = []
    x,y = node
    x_max, y_max = obj_fnc.shape
    nbs += [(x-1,y)] if x > 0 else []
    nbs += [(x+1,y)] if x < x_max else []
    nbs += [(x,y-1)] if y > 0 else []
    nbs += [(x,y+1)] if y < y_max else []
    
    return nbs

# value of node in the obj function
def eval(node,obj_fnc):
    x,y = node
    return obj_fnc[x][y]

def hill_climbing(start_node,obj_fnc):

    curr_node = start_node
    while True:
    
        next_eval = float('-inf')
        next_node = None
        for n in neighbors(curr_node,obj_fnc):
            val = eval(n,obj_fnc)
            if val > next_eval:
                next_node = n
                next_eval = val
        
        curr_eval = eval(curr_node,obj_fnc)
        if next_eval <= curr_eval:
            return curr_node, curr_eval
        
        curr_node = next_node

def random_restart(start_node,obj_fnc):
    x_max, y_max = obj_fnc.shape
    
    best_node = None
    best_eval = None
    curr_start = start_node
    n = 0
    while n < 10:
        node, eval = hill_climbing(curr_start,obj_fnc)
        best_node = node if best_eval is None else best_node
        best_eval = eval if best_eval is None else best_eval
        
        if eval > best_eval:
            best_node = node
            best_eval = eval
        
        n += 1
    
    return best_node,best_eval
    
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Steepest ascent or random restart.')
    parser.add_argument('--steepest_ascent', '-S',action='store_true',
                    help='apply steepest ascent')
    parser.add_argument('--random_restart', '-R',action='store_true',
    help='apply random restart')
    parser.add_argument('--start_x', '-x',type=int,default=0,
    help='starting x')
    parser.add_argument('--start_y', '-y',type=int,default=0,
    help='starting y')
    parser.add_argument('--x_dim',type=int,default=14,
    help='obj fnc x dim')
    parser.add_argument('--y_dim',type=int,default=9,
    help='obj fnc y dim')

    args = parser.parse_args()
    
    x_dim = args.x_dim
    y_dim = args.y_dim
    obj_fnc = np.random.randint(0,x_dim*y_dim + 1,(x_dim,y_dim))
    start_node = (args.start_x,args.start_y)
    
    if args.steepest_ascent:
        print(hill_climbing(start_node,obj_fnc))
    elif args.random_restart:
        print(random_restart(start_node,obj_fnc))
    else:
        print("No strategy specified.")
    
        
