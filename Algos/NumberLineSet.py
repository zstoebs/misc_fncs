"""
@filename NumberLineSet.py
@author Zach Stoebner
@date 10-27-2019
@details Given a set X of segments on a number line, build a set S from X
s.t. no segment overlaps and |S| is of maximum size.
Prove that this problem has optimal substructure.
"""

x = [(10,15),(3,9),(6,20),(14,17)]

def create_S(segs=list()):

    n = len(segs)
    assert n >= 2

    # sort based on start points
    segs.sort(key=(lambda x: x[0]))
    Ss = list()
    i = 0
    while i < n:

        # if last element and didn't get popped previously then it's safe b/c it doesn't overlap with anything that's in S
        if len(segs) == 1:
            Ss.extend(segs)
        # if there is no overlap b/w s1 and s2,
        # then s1 can be added to S b/c s3's start point must be greater
        # than s2's start point
        elif segs[1][0] > segs[0][1]:
            Ss.append(segs[0])
            segs.pop(0)
        # otherwise s1 and s2 overlap
        else:
            # if s1 encompasses s2 then s1 should be eliminated
            # b/c s3 either starts in s1, starts in s2 which in this case
            # starts in s1, or starts beyond s1 which starts
            # beyond s2 in this case --> if s1 can be in the optimal solution
            # then so can s2, but s2 may also be in an optimal solution that
            # s1 couldn't be in b/c it overlaps some s00 later on
            if segs[1][1] <= segs[0][1]:
                segs.pop(0)
            else:
                segs.pop(1)

        i += 1

    return Ss

### TESTS
print(create_S(x))
x1 = [(1,1),(2,2),(3,3),(4,7),(7,9)]
print(create_S(x1))
x2 = [(10,11),(10,12),(10,13)]
print(create_S(x2))
"""
[(3, 9), (10, 15)]
[(1, 1), (2, 2), (3, 3), (4, 7)]
[(10, 11)]
"""
