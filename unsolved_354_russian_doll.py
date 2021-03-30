"""
You are given a 2D array of integers envelopes where
envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both
the width and height of one envelope is greater than
the width and height of the other envelope.

Return the maximum number of envelopes can you
Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.


Example 1:
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll
is 3 ([2,3] => [5,4] => [6,7]).

Example 2:
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
"""
