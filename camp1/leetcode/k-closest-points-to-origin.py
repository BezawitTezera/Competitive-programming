class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def mergedsort(points):
            if len(points) > 1:
                left = points[:len(points)//2]
                right = points[len(points)//2:]

                mergedsort(left)
                mergedsort(right)

                i = 0
                j = 0
                x = 0
                while i < len(left) and j < len(right):
                    value1X = pow(left[i][0], 2)
                    value1Y = pow(left[i][1], 2)
                    value1 = pow(value1X + value1Y, 1/2)
                    value2X = pow(right[j][0], 2)
                    value2Y = pow(right[j][1], 2)
                    value2 = pow(value2X + value2Y, 1/2)

                    if value2 < value1:
                        points[x] = right[j]
                        j += 1
                    else:
                        points[x] = left[i]
                        i += 1

                    x += 1

                while i < len(left):
                    points[x] = left[i]
                    i += 1
                    x += 1

                while j < len(right):
                    points[x] = right[j]
                    j += 1
                    x += 1

        mergedsort(points)
        return points[:k]
