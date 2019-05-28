# Design

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = [val for vec1d in vec2d if len(vec1d) > 0 for val in vec1d]
        self.idx = 0

    def next(self):
        """
        :rtype: int
        """
        val = self.vec2d[self.idx]
        self.idx += 1
        return val
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.vec2d)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())