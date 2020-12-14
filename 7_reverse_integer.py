class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        sign = x/abs(x)
        x = x/sign
        int_max = 2**31-1
        result = 0
        while (x>0):
            if (int_max - x%10)//10 < result  :
                return 0
            result = result * 10 + x%10
            x = x//10
        return result*sign
