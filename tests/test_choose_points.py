import pytest
from hypothesis import given, assume, strategies as st
from pypackmol.check_points import points_in_box


@pytest.mark.parametrize(
    "box_x,box_y,box_z,point_coords,inside_answer",
    [
        [[0, 10], [0, 10], [0, 10], [1, 1, 1], True],
        [[0, 10], [0, 10], [0, 10], [-1, 1, 1], False],
        [[0, 10], [0, 10], [0, 10], [1, -1, 1], False],
        [[0, 10], [0, 10], [0, 10], [1, 1, -1], False],
        [[0, 10], [0, 10], [0, 10], [1, 1, 0], False],
        [[0, 10], [0, 10], [0, 10], [1, 0, 1], False],
        [[0, 10], [0, 10], [0, 10], [0, 1, 1], False],
        [[0, 10], [0, 10], [0, 10], [5, 5, 5], True],
    ],
)
def test_points_in_box(box_x, box_y, box_z, point_coords, inside_answer):
    assert points_in_box(box_x, box_y, box_z, point_coords) == inside_answer


def check_floats_different(float_list):
    return round(float_list[0], 3) != round(float_list[1], 3)


@st.composite
def inside_box(draw):

    x_lims = draw(
        st.lists(st.floats(-200, 200), min_size=2, max_size=2, unique=True).filter(
            lambda x: check_floats_different(x)
        )
    )
    y_lims = draw(
        st.lists(st.floats(-200, 200), min_size=2, max_size=2, unique=True).filter(
            lambda x: check_floats_different(x)
        )
    )
    z_lims = draw(
        st.lists(st.floats(-200, 200), min_size=2, max_size=2, unique=True).filter(
            lambda x: check_floats_different(x)
        )
    )
    point_location = draw(
        st.tuples(
            st.floats(
                min_value=min(x_lims),
                max_value=max(x_lims),
                exclude_min=True,
                exclude_max=True,
            ),
            st.floats(
                min_value=min(y_lims),
                max_value=max(y_lims),
                exclude_min=True,
                exclude_max=True,
            ),
            st.floats(
                min_value=min(z_lims),
                max_value=max(z_lims),
                exclude_min=True,
                exclude_max=True,
            ),
        )
    )
    return (x_lims, y_lims, z_lims, point_location)


@given(inside_box())
def test_points_in_box_hypothesis(function_params):
    assert points_in_box(*function_params)
