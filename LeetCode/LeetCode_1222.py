"""
1222. Queens That Can Attack the King (medium)

1) Approach from queen's position
2) Add queen's position if it is possible to attack king
3) Update queen's position if the closer queen's position is found
"""


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:

        direction = [0] * 8

        def distance(a, b):  # Get the manhatan distance between queen and king.
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        def check_direction(k, q):  # Check the valid case of queen's position to attack king

            row_diff = k[0] - q[0]
            col_diff = k[1] - q[1]

            if row_diff > 0 and col_diff > 0 and row_diff == col_diff:
                return 0
            elif row_diff > 0 and col_diff == 0:
                return 1
            elif row_diff > 0 and col_diff < 0 and row_diff == -col_diff:
                return 2
            elif row_diff == 0 and col_diff < 0:
                return 3
            elif row_diff < 0 and col_diff < 0 and row_diff == col_diff:
                return 4
            elif row_diff < 0 and col_diff == 0:
                return 5
            elif row_diff < 0 and col_diff > 0 and row_diff == -col_diff:
                return 6
            elif row_diff == 0 and col_diff > 0:
                return 7
            else:
                return 8

        for queen in queens:
            d = check_direction(king, queen)  # Check the direction of queen to king
            if d < 8:
                if direction[d] == 0:
                    direction[d] = queen
                else:
                    curr_dist = distance(king, direction[d])
                    new_dist = distance(king, queen)

                    if curr_dist > new_dist:
                        direction[d] = queen
        sol = [c for c in direction if c != 0]
        return sol