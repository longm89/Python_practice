class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        list1 = [int(s) for s in num1[::-1]]
        list2 = [int(s) for s in num2[::-1]]
        inverse_result = [0 for i in range(len(list1)+len(list2))]
        length_of_result = 1
        for i in range(len(list1)):
            temp= [0]*i
            carry_on = 0
            for j in range(len(list2)):
                x = list1[i]*list2[j] + carry_on
                carry_on = x//10
                temp.append(x% 10)
            if carry_on>0:
                temp.append(carry_on)
            carry_on =0
            for j in range(min(length_of_result, len(temp))):
                x = temp[j] + inverse_result[j] + carry_on
                carry_on = x //10
                inverse_result[j] = x %10
            if length_of_result<len(temp):
                for j in range(length_of_result, len(temp)):
                    x = carry_on + temp[j]
                    inverse_result[j] = x %10
                    carry_on = x//10
                    length_of_result = len(temp)
            else:
                for j in range(len(temp), length_of_result):
                    x = carry_on + inverse_result[j]
                    inverse_result[j] = x %10
                    carry_on = x //10
            if carry_on>0:
                inverse_result[length_of_result] = carry_on
                length_of_result +=1
        while length_of_result>1 and inverse_result[length_of_result-1]==0:
            length_of_result -=1
        string_result = "".join([str(s) for s in inverse_result[length_of_result-1::-1]])
        return string_result
