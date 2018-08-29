#!/usr/bin/env python3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc_slope(self, p2):
        return (self.y - p2.y) / (self.x - p2.x)

    def print_self(self):
        print("Point is at ({},{})".format(self.x, self.y))
        
class Line:
    def __init__(self, p1, p2):
        self.start = p1
        self.end = p2
        self.m = self.calc_slope()
        self.b = self.calc_yint()
        
    def calc_slope(self):
        return self.start.calc_slope(self.end)

    def calc_yint(self):
        return self.start.y - self.m * self.start.x

    def is_point_on_line(self, p):        
        if (self.end.x >= self.start.x):
            lower_x = self.start.x
            upper_x = self.end.x
        else:
            lower_x = self.end.x
            upper_x = self.start.x

        if (self.end.y >= self.start.y):
            lower_y = self.start.y
            upper_y = self.end.y
        else:
            lower_y = self.end.y
            upper_y = self.start.y
        
        if (p.x >= lower_x and
            p.x <= upper_x and
            p.y >= lower_y and
            p.y <= upper_y):
            return True
            
        return False
    
def prob3(line1, line2):
    """ Returns the point of intersection if line1 intersects line2 or None if it doesn't """
    if (line1.m == line2.m and line1.b == line2.b):
        print('Same slope and y-intercept, two lines are part of the same line')
        return None
    elif (line1.m == line2.m and line1.b != line2.b):
        print('Same slope, diff y-intercept, two lines are parallel')
        return None

    # Find point of intersection
    x_int = (line2.b - line1.b) / (line1.m - line2.m)
    y_int = line2.m * x_int + line2.b
    p_int = Point(x_int, y_int)

    if (line1.is_point_on_line(p_int) and line2.is_point_on_line(p_int)):
        print("Lines intersect at ({},{})".format(p_int.x, p_int.y))
        return p_int
    else:
        print("Lines do not intersect")
        return None
        
    
def main():
    # p1 = Point(-2.8, 1)
    # p2 = Point(1.03,-2)
    p1 = Point(3.5, 2.46)
    p2 = Point(5.62, 4.4104)

    line1 = Line(p1, p2)
    print('Slope :{0:.4f}, Y-int :{1:.4f}'.format(line1.m, line1.b))

    p3 = Point(3.3, 2.78)
    p4 = Point(4, 2)
    line2 = Line(p3, p4)
    print('Slope :{0:.4f}, Y-int :{1:.4f}'.format(line2.m, line2.b))
    prob3(line1, line2)
    
    
if __name__ == '__main__':
    main()
