def depthFirstSearch(problem):

    # Recursive DFS implementation
    def DFS(triple,path=[],disc=[]):
        """
        Procedure:
        1. Visit the state and push to path
        2. Check if it's the goal state and return if so
        3. For each unvisited successor, recurse
        4. If the result of the recursion is not False, then return solution
        5. Otherwise, return False if dead end
        """
        
        nonlocal problem

        # visit this state
        state, act, cost = triple
        path += [act] if act else []

        # if goal state, return the path
        if problem.isGoalState(state):
            return path

        if not state in disc:

            disc += [state]

            # loop successors for goal state
            for suc in problem.getSuccessors(state):
                root_path = path[:]
                result = DFS(suc,root_path,disc)
                if result:
                    return result

        # dead end
        return False

    start_state = problem.getStartState()
    triple = (start_state,False,0)

    # return a list of the actions in the order of the path
    return DFS(triple)
