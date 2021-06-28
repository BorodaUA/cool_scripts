import random
from task_3_triangles_sorting.task_3 import Triangle


def test_create_triangle_valid_data():
    '''
    Test create Triangle instance with valid data
    '''
    triangle_name = 'abc' * random.randint(3, 8)
    triangle_side_a = float(random.randint(25, 30))
    triangle_side_b = float(random.randint(25, 30))
    triangle_side_c = float(random.randint(10, 20))
    #
    test_instance = Triangle(
        triangle_name,
        triangle_side_a,
        triangle_side_b,
        triangle_side_c
    )
    #
    assert triangle_name == test_instance.triangle_name
    assert triangle_side_a == test_instance.side_a
    assert triangle_side_b == test_instance.side_b
    assert triangle_side_c == test_instance.side_c


def test_compare_triangle_areas():
    '''
    Test create 2 Triangle instances with valid data
    and compare triangles areas, triangle_1 >= triangle_2
    '''
    triangle_1_name = 'abc' * random.randint(3, 8)
    triangle_1_side_a = float(random.randint(25, 30))
    triangle_1_side_b = float(random.randint(25, 30))
    triangle_1_side_c = float(random.randint(10, 20))
    #
    triangle_2_name = 'defg' * random.randint(3, 8)
    triangle_2_side_a = float(random.randint(15, 20))
    triangle_2_side_b = float(random.randint(15, 20))
    triangle_2_side_c = float(random.randint(5, 10))
    #
    test_instance_1 = Triangle(
        triangle_1_name,
        triangle_1_side_a,
        triangle_1_side_b,
        triangle_1_side_c
    )
    test_instance_2 = Triangle(
        triangle_2_name,
        triangle_2_side_a,
        triangle_2_side_b,
        triangle_2_side_c
    )
    #
    assert (
        test_instance_1.triangle_area >= test_instance_2.triangle_area
    )
