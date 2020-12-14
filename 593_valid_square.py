class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def sq_dist(p1,p2):
            return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
        def perpen(p1,p2,p3):
            return (p2[0]-p1[0])*(p3[0]-p2[0]) + (p2[1]-p1[1])*(p3[1]-p2[1]) == 0
        def check(p1,p2,p3,p4):
            return (sq_dist(p1,p2)==sq_dist(p2,p3)) and (sq_dist(p2,p3)==sq_dist(p3,p4)) and (sq_dist(p3,p4)==sq_dist(p4,p1)) and perpen(p1,p2,p3)
        if p1==p2 and p2==p3 and p3==p4:
                return False
        return check(p1,p2,p3,p4) or check(p1,p2,p4,p3) or check(p1,p3,p2,p4)
        
