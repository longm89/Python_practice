class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        def start_end(element):
            return element[0]

        intervals.sort(key = start_end)
        if not intervals:
            return [[]]
        start,stop = intervals[0][0], intervals[0][1]
        result = []
        for i in range(1,len(intervals)):
            if intervals[i][0]<=stop:
                stop = max(stop,intervals[i][1])
            else:
                result.append([start,stop])
                start,stop = intervals[i][0], intervals[i][1]
        result.append([start,stop])
        return result
    
