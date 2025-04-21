def get_prereq_list():
    """
    Input: None

    Output: The result of the database query to get all of the prereq information, formatted as a list of tuples (prereq_course, main_course)

    Data should be returned in the form of a list of tuples, with each tuple having the following data:
    (Prereq_Course_Code, Main_Course_Code)
    """
    # TODO: get_prereq_list will perform the SQL query to get the proper list

    test_prereq_list = [
        ("111", "222"),
        ("222", "444"),
        ("333", "444"),
        ("333", "999"),
        ("444", "555"),
        ("444", "666"),
        ("555", "777"),
        ("555", "888"),
        ("666", "888"),
    ]
    return test_prereq_list


def load_all_courses():
    """
    Input: None

    Output: Result from query that will load all course information and store in course objects

    Data should be returned in the form of a list of tuples, with each tuple having the following data:
    (CRN, Course_Code, is_Pinned, start_time, end_time, duration)
    """
    # TODO: Connect this to the database, currently holding temp information
    test_courses_list = [
        ("1111", "111", False),
        ("2222", "222", False),
        ("2002", "222", False),
        ("2112", "222", False),
        ("3003", "333", False),
        ("3333", "333", False),
        ("4444", "444", False),
        ("5555", "555", False),
        ("6666", "666", True),
        ("7777", "777", False),
        ("7007", "777", False),
        ("8888", "888", True),
        ("9999", "999", False),
    ]
    return test_courses_list


def load_teaches():
    """
    Input: None

    Output: Result from the query that pulls all data from the teaches table, linking courses to the faculty teaching them.
    Returns a hashmap with a faculty member as the key and a list of CRN's as the value

    Data should be returned in the form of a hashmap where the keys are Faculty ID's and the values are lists of the CRN's they teach
    """
    # TODO: Connect this to the database, currently holding temp information
    test_teaches = {
        "A": ["1111", "2222"],
        "B": ["2002", "9999", "6666"],
        "C": ["3333", "5555"],
        "D": ["4444", "7777", "2112"],
        "E": ["8888", "7007"],
        "F": ["3003"],
    }
    return test_teaches


def get_coreq_list():
    """
    Input: None

    Output: The result of the database query to get all of the coreq information, formatted as a list of tuples (course1, course2)

    Data should be returned in the form of a list of tuples, with each tuple having the following data:
    (Coreq_CRN1, Coreq_CRN2)
    """
    # TODO: get_prereq_list will perform the SQL query to get the proper list

    test_coreqs = [
        ("2222", "2002"),
        ("2112", "2002"),
        ("2222", "2112"),
        ("3333", "3003"),
        ("7777", "7007"),
    ]
    return test_coreqs
