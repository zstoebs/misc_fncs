"""
@filename CheapestTrucks.py
@author Zach Stoebner
@date 10-27-2019
@details Given k trucks that can each haul some weight for some price (price goes up
as hauling capacity increases) and d trailers, each with a unique weight, determine whether all
of the trailers can be hauled from the given trucks and if so the cheapest cost to do the job.
"""

#determine_cost
#Determines if possible and if so returns the cheapest cost
#Complexity: O(klogk + dlogd)
def determine_cost(trucks=list(),trailers=list()):
    k = len(trucks)
    d = len(trailers)

    # pidgeonhole principle
    if k < d:
        return None

    # assuming each of these sorts runs in O(nlogn) time
    trucks.sort(key=(lambda x: x[0]))
    trailers.sort()

    cost = 0

    # for each trailer, find the cheapest truck remaininig that can carry it
    # on each iteration a new trailer is treated as the lightest trailer
    for i in range(d):

        # discard any trucks that cannot carry the current lightest trailer
        while k > 0 and trucks[0][0] < trailers[i]:
            trucks.pop(0)
            k -= 1

        # found one so add to the cost and discard
        cost += trucks[0][1]
        trucks.pop(0)
        k -= 1

        # if too many were useless, then the pidgeonhole principle reoccurs
        if k < (d-(i+1)):
            return None

    return cost

### TESTS
tk1 = [(13,1700),(8,1500),(5,1350),(12,1690),(22,1900),(19,1825),(4,1300),(2,1000)]
tr1 = [12,11,4,15,3]
print(determine_cost(tk1,tr1)) # 7865
tk2 = [(17,1700),(8,1300),(22,1900),(15,1690),(5,1000),(12,1500),(9,1350),(21,1825)]
tr2 = [4,19,21,18]
print(determine_cost(tk2,tr2)) #None
