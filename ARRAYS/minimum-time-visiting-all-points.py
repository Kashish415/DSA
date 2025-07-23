# https://leetcode.com/problems/minimum-time-visiting-all-points/submissions/1707878196/?envType=problem-list-v2&envId=array

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        result = 0
        x1,y1 = points.pop()           # get the first point 
        while points:
            x2,y2 = points.pop()       # get second point 
            result += max(abs(y2-y1),abs(x2-x1))   # ==> gives min time
            x1,y1 =  x2,y2  # moving furthur in the list

        return result 
