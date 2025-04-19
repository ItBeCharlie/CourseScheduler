def get_prereq_list():
    """
    Input: None

    Output: The result of the database query to get all of the prereq information, formatted as a list of tuples (prereq_course, main_course)
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
    """
    # TODO: Connect this to the database, currently holding temp information
    test_courses_list = [
        ("1111", "111", False),
        ("2222", "222", False),
        ("2002", "222", False),
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
    """
    # TODO: Connect this to the database, currently holding temp information
    test_teaches = {
        "A": ["1111", "2222"],
        "B": ["2002", "9999", "6666"],
        "C": ["3333", "5555"],
        "D": ["4444", "7777"],
        "E": ["8888", "7007"],
        "F": ["3003"],
    }
    return test_teaches
