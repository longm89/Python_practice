"""
There are N rooms and you start in room 0.
Each room has a distinct number in 0, 1, 2, ..., N-1,
and each room may have some keys to access the next room.

Formally, each room i has a list of keys rooms[i],
and each key rooms[i][j] is an integer in [0, 1, ..., N-1]
where N = rooms.length.
A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0).

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:
Input: [[1],[2],[3],[]]
Output: true
Explanation:
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.

Example 2:
Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.

"""


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        We use BFS starting from the room 0
        The time complexity is O(V+E) where V is the set of rooms and
        E is the set of keys
        The space complexity is O(V) because we use a list as a queue
        and we keep a visited list to keep track of which room is visited
        """

        queue = []
        visited = [False for i in range(len(rooms))]
        visited[0] = True
        queue.append(0)
        # first_pos in the queue
        first_pos = 0

        while first_pos < len(queue):
            room = queue[first_pos]
            first_pos += 1

            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    queue.append(key)

        for i in range(len(rooms)):
            if not visited[i]:
                return False
        return True
