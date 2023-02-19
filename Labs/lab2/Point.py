class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y


    def __lt__(self,object1):
        return self.dist_from_origin() < object1.dist_from_origin()


    def __gt__(self,object1):
        return self.dist_from_origin() > object1.dist_from_origin()

    def __eq__(self,object1):
        return self.dist_from_origin() == object1.dist_from_origin()


    def dist_from_origin(self):
        return ((self.x - 0)**2+(self.y - 0)**2)**0.5
    
    def __str__(self):
        return f'Point({self.x}, {self.y})'
# ^^^Implement class and functionality above (remember to include docstrings!)
# vvvImplement tests below

if __name__ == '__main__':
    # All tests should use `assert`, not `print`
    
    ##### test init #####
    # assert correct x
    # assert correct y
    p1 = Point(3, 4)
    assert p1.x == 3
    assert p1.y == 4
    ##### test lt #####
    p2= Point(3,4)
    p1= Point(0,0)
    assert (p1 < p2)
    assert (not p1 < p2)
    # Expected True (e.g `p1 < p2`)
    # Expected False (e.g. `not p1 < p2`)

    ##### test gt #####
    # Expected True (e.g `p1 > p2`)
    # Expected False (e.g. `not p1 > p2`)
    p1 = Point(3, 4)
    p2= Point(0,0)
    assert (p1 > p2)
    assert not (p1 > p2)
    ##### test eq #####
    # Expected True (e.g `p1 == p2`)
    # Expected False (e.g. `not p1 == p2`)
    p1 =  Point(3,3)
    p2 =  Point(3,3)
    assert (p1 == p2)
    assert (not p1 == p2)

    
    ##### test str #####
    p1 = Point(3,4)
    expect_string = 'Point(3, 4)'
    assert expect_string == str(p1)
    #assert str(some_point) == expected_string

    ##### test dist_from_origin() #####
    p1 = Point(3,4)
    expect_dist = 5.0
    assert expect_dist == p1.dist_from_origin()