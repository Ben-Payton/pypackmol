import pytest

from pypackmol.check_points import points_in_box

@pytest.mark.parametrize("box_x,box_y,box_z,point_coords,inside_answer",
                         ([(0,10),(0,10),(0,10),(1,1,1),True],
                          [(0,10),(0,10),(0,10),(-1,1,1),False],
                          [(0,10),(0,10),(0,10),(1,-1,1),False],
                          [(0,10),(0,10),(0,10),(1,1,-1),False]
                          [(0,10),(0,10),(0,10),(1,1,0),False],
                          [(0,10),(0,10),(0,10),(1,0,1),False]
                          [(0,10),(0,10),(0,10),(0,1,1),False]
                          [(0,10),(0,10),(0,10),(5,5,5),True],
                          ))
def test_points_in_box(box_x,box_y,box_z,point_coords,inside_answer):
    assert points_in_box(box_x,box_y,box_z,point_coords) == inside_answer
