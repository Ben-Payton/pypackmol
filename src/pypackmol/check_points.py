

def points_in_box(box_x:tuple[float,float],box_y:tuple[float,float],box_z:tuple[float,float],point_coords:tuple[float,float,float]) -> bool:
    """Checks if a point is within a certain box.

    Args:
        box_x (tuple[float,float]): The box x limits.
        box_y (tuple[float,float]): The box y limits.
        box_z (tuple[float,float]): The box z limits.
        point_coords (tuple[float,float,float]): The coordinates of the point to test.

    Returns:
        bool: True if the point is inside the box, False otherwise.
    """
    x_check  = point_coords[0] > min(box_x) and point_coords[0] < max(box_x)
    
    y_check  = point_coords[1] > min(box_y) and point_coords[1] < max(box_y)
    
    z_check  = point_coords[2] > min(box_z) and point_coords[2] < max(box_z) 

    return x_check and y_check and z_check
