import sys
import io
import random
from task_3_triangles_sorting.task_3 import TrianglesSorter, Triangle


def test_add_triangle_cli_valid_parameters(monkeypatch, capsys):
    '''
    Test add triangle with valid parameters
    '''
    add_triangle = 'y'
    triangle_name = 'abc' * random.randint(3, 8)
    triangle_side_a = str(random.randint(25, 30))
    triangle_side_b = str(random.randint(25, 30))
    triangle_side_c = str(random.randint(10, 20))
    triangle = (
        f'{triangle_name}, {triangle_side_a}, '
        f'{triangle_side_b}, {triangle_side_c}'
    )
    add_another_triangle = 'n'
    #
    input_values = '\n'.join(
        [
            add_triangle,
            triangle,
            add_another_triangle
        ]
    )
    #
    test_triangle = Triangle(
        triangle_name,
        float(triangle_side_a),
        float(triangle_side_b),
        float(triangle_side_c)
    )
    #
    monkeypatch.setattr(sys, 'stdin', io.StringIO(input_values))
    #
    tr_sorter = TrianglesSorter()
    tr_sorter.run()
    #
    cli_out, cli_error = capsys.readouterr()
    #
    expected_result = (
            '\n*** Welcome to the Triangles Sorter *** \n'
            'Follow the program instruction to create triangles\n'
            'and get the output of triangles list sorted by its area \n'
            'You can quit at any moment by typing command: q\n\n'
            'Would you like to create a triangle?\n'
            'Please type: y/yes or n/no \n'
            'To add a triangle please provide following data: \n'
            '<Triangle name>, <length of the side>, <length of the side>, '
            '<length of the side> \nExample: isosceles, 5, 10, 10 \n'
            'Example: equilateral, 10, 10, 10 : \n'
            'Would you like to create a triangle?\n'
            'Please type: y/yes or n/no '
            '============= Triangles list: ===============\n'
            f'1.[{triangle_name}]: {test_triangle.triangle_area} cm\n'
        )
    assert '' == cli_error
    assert expected_result == cli_out
