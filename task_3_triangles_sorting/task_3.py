class Triangle:
    """
    A triangle class
    """

    def __init__(self, triangle_name, side_a, side_b, side_c):
        """
        Initialization of an instance of the Triangle with
        a triangle name and 3 sides
        """
        self.triangle_name = triangle_name
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def triangle_area(self):
        '''
        A method that calculates a triangle area by Heron's formula
        '''
        p = (self.side_a + self.side_b + self.side_c) / 2
        result = (
            p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)
        ) ** 0.5
        return round(result, 2)


class TrianglesSorter:
    """
    A TrianglesSorter class
    """

    WELCOME_MSG = (
        '\n*** Welcome to the Triangles Sorter *** \n'
        'Follow the program instruction to create triangles\n'
        'and get the output of triangles list sorted by its area \n'
        'You can quit at any moment by typing command: q'
    )
    ADD_TRIANGLE_MSG = (
        '\nTo add a triangle please provide following data: \n'
        '<Triangle name>, <length of the side>, <length of the side>, '
        '<length of the side> \n'
        'Example: isosceles, 5, 10, 10 \n'
        'Example: equilateral, 10, 10, 10 : '
    )
    ADD_TRIANGLE_QUESTION = (
        '\nWould you like to create a triangle?\n'
        'Please type: y/yes or n/no '
    )
    QUIT_MSG = "Quitting..."
    WRONG_USER_INPUT_MSG = (
        "\nSorry could not recognize this command, please try again."
    )
    INVALID_TRIANGLE_PARAMS = (
        '\nTriangle with such parameters can not be created, please try again.'
    )
    TRIANGLE_LIST_DECOR = '============= Triangles list: ==============='

    @classmethod
    def input_triangle_handler(cls, message, error_msg):
        """
        A helper method, that return valid user's input or
        an error message
        """
        while True:
            user_input = input(message)
            if isinstance(user_input, str):
                if user_input.lower() == "q":
                    return False
                #
                user_input = ''.join(
                    [c for c in user_input if c not in ['\t', '\n']]
                ).split(',')
                #
                if len(user_input) != 4:
                    print(error_msg)
                    continue
                #
                result = []
                result.append(user_input[0])
                for p in user_input[1:]:
                    try:
                        p = float(p)
                    except ValueError:
                        print(error_msg)
                        continue
                    result.append(p)
                #
                a = result[1]
                b = result[2]
                c = result[3]
                if a + b <= c or b + c <= a or c + a <= b:
                    print(TrianglesSorter.INVALID_TRIANGLE_PARAMS)
                    continue
                return result

    @classmethod
    def input_start_handler(cls, message, error_msg):
        """
        A helper method, that return valid user's input or
        an error message
        """
        while True:
            what = input(message)
            if isinstance(what, str):
                if what.lower() == "q":
                    return False
                if what.lower() == "y" or what.lower() == "yes":
                    return True
                elif what.lower() == 'n' or what.lower() == 'no':
                    return False
                print(error_msg)
                continue

    def run(self):
        """
        A run method responsible for asking user input and
        outputting sorted triangles based on user's input
        """
        triangles_list = []
        while True:
            print(TrianglesSorter.WELCOME_MSG)
            #
            if len(triangles_list) == 0:
                user_input = TrianglesSorter.input_start_handler(
                    message=TrianglesSorter.ADD_TRIANGLE_QUESTION,
                    error_msg=TrianglesSorter.WRONG_USER_INPUT_MSG
                )
                if user_input is False:
                    print(TrianglesSorter.QUIT_MSG)
                    break
            #
            user_input = TrianglesSorter.input_triangle_handler(
                message=TrianglesSorter.ADD_TRIANGLE_MSG,
                error_msg=TrianglesSorter.WRONG_USER_INPUT_MSG
            )
            if user_input is False:
                print(TrianglesSorter.QUIT_MSG)
                break
            #
            triangle = Triangle(
                triangle_name=user_input[0],
                side_a=user_input[1],
                side_b=user_input[2],
                side_c=user_input[3]
            )
            #
            triangles_list.append(
                {
                    "triangle_name": triangle.triangle_name,
                    "triangle_area": triangle.triangle_area
                }
            )
            #
            user_input = TrianglesSorter.input_start_handler(
                message=TrianglesSorter.ADD_TRIANGLE_QUESTION,
                error_msg=TrianglesSorter.WRONG_USER_INPUT_MSG
            )
            if user_input is False:
                print(TrianglesSorter.TRIANGLE_LIST_DECOR)
                #
                sorted_triangles = sorted(
                    triangles_list,
                    key=lambda x: x['triangle_area'],
                    reverse=True
                )
                #
                for n in range(len(sorted_triangles)):
                    triangle = sorted_triangles[n]
                    print(
                        f'{n + 1}.[{triangle["triangle_name"]}]: '
                        f'{triangle["triangle_area"]} cm'
                        )
                break


if __name__ == "__main__":
    game = TrianglesSorter()
    game.run()
