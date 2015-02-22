class Point(object):
    '''
    Represents the point on a corrdinate system.
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def get_corrdinates(self):
        return "x:{} , y: {}".format(self.x, self.y)


class RectangleIntersection(object):
    
    def do_overlap(self, l1, r1, l2, r2):
        # If one rectangle is on the left side of other.
        if l1.x > r2.x or l2.x > r1.x:
            return False

        # If one rectangle is on the above of other one.
        if l1.y < r2.y or r1.y > l2.y:
            return False

        return True


def main():
    l1 = Point(0, 10)
    r1 = Point(10, 0)
    l2 = Point(5, 5)
    r2 = Point(15, 0)
    ri = RectangleIntersection()
    if ri.do_overlap(l1, r1, l2, r2):
        print "Rectangles Intersect"
    else:
        print "Do not intersect"

if __name__ == "__main__":
    main()

    
