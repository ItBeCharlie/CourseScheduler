from time_conversion import *
from import_csv import *


def get_prereq_list():
    """
    Input: None

    Output: The result of the database query to get all of the prereq information, formatted as a list of tuples (prereq_course, main_course)

    Data should be returned in the form of a list of tuples, with each tuple having the following data:
    (Prereq_Course_Code, Main_Course_Code)
    """
    # TODO: get_prereq_list will perform the SQL query to get the proper list
    test_courses = build_course_objects(
        "graduate_icsi_spring_2025_in_person_classes.csv"
    )
    test_prereq_list = []
    for course in test_courses:
        for prereq in course.prereqs:
            test_prereq_list.append((prereq, course.course_code))

    # test_prereq_list = [
    #     ("111", "222"),
    #     ("222", "444"),
    #     ("333", "444"),
    #     ("333", "999"),
    #     ("444", "555"),
    #     ("444", "666"),
    #     ("555", "777"),
    #     ("555", "888"),
    #     ("666", "888"),
    # ]
    # print(test_prereq_list)
    return test_prereq_list


def load_all_courses():
    """
    Input: None

    Output: Result from query that will load all course information and store in course objects

    Data should be returned in the form of a list of tuples, with each tuple having the following data:
    (CRN, Course_Code, is_Pinned, duration, start_time, end_time, days)
    """
    # TODO: Connect this to the database, currently holding temp information
    test_courses = build_course_objects(
        "graduate_icsi_spring_2025_in_person_classes.csv"
    )
    test_courses_list = []
    for course in test_courses:
        test_courses_list.append(
            (
                course.crn,
                course.course_code,
                course.is_pinned,
                course.duration,
                course.start_time,
                course.end_time,
                course.days,
            )
        )
    # test_courses_list = [
    #     ("1111", "111", False, 80, None, None, None),
    #     ("2222", "222", False, 80, None, None, None),
    #     ("2002", "222", False, 170, None, None, None),
    #     ("2112", "222", False, 80, None, None, None),
    #     ("3003", "333", False, 170, None, None, None),
    #     ("3333", "333", False, 80, None, None, None),
    #     ("4444", "444", False, 80, None, None, None),
    #     ("5555", "555", False, 80, None, None, None),
    #     ("6666", "666", True, 80, "9:30", "10:50", ["M", "W"]),
    #     ("7777", "777", False, 80, None, None, None),
    #     ("7007", "777", False, 170, None, None, None),
    #     ("8888", "888", True, 80, "8:00", "9:20", ["T", "TH"]),
    #     ("9999", "999", False, 80, None, None, None),
    # ]
    return test_courses_list


def load_teaches():
    """
    Input: None

    Output: Result from the query that pulls all data from the teaches table, linking courses to the faculty teaching them.
    Returns a hashmap with a faculty member as the key and a list of CRN's as the value

    Data should be returned in the form of a hashmap where the keys are Faculty ID's and the values are lists of the CRN's they teach
    """
    # TODO: Connect this to the database, currently holding temp information
    test_courses = build_course_objects(
        "graduate_icsi_spring_2025_in_person_classes.csv"
    )
    test_teaches = {}
    for course in test_courses:
        if course.faculty not in test_teaches:
            test_teaches[course.faculty] = []
        test_teaches[course.faculty].append(course.crn)
    # test_teaches = {
    #     "A": ["1111", "2222"],
    #     "B": ["2002", "9999", "6666"],
    #     "C": ["3333", "5555"],
    #     "D": ["4444", "7777", "2112"],
    #     "E": ["8888", "7007"],
    #     "F": ["3003"],
    # }
    return test_teaches


def get_coreq_list():
    """
    Input: None

    Output: The result of the database query to get all of the coreq information, formatted as a list of tuples (course1, course2)

    Data should be returned in the form of a list of tuples, with each tuple having the following data:
    (Coreq_CRN1, Coreq_CRN2)
    """
    # TODO: get_prereq_list will perform the SQL query to get the proper list
    test_courses = build_course_objects(
        "graduate_icsi_spring_2025_in_person_classes.csv"
    )
    test_coreqs = []
    for course in test_courses:
        for coreq in course.coreqs:
            test_coreqs.append((coreq, course.crn))
    # test_coreqs = [
    #     ("2222", "2002"),
    #     ("2112", "2002"),
    #     ("2222", "2112"),
    #     ("3333", "3003"),
    #     ("7777", "7007"),
    # ]
    return test_coreqs


def load_possible_times():
    """
    Input: None

    Output: Will load config information about what times and days are valid for courses
    """
    # TODO: Hook up to DB
    start_time = time_str2int("8:00")
    end_time = time_str2int("19:00")
    increment = 90

    test_days = [["M", "W"], ["T", "TH"]]
    test_times = []
    for time in range(start_time, end_time + 1, increment):
        test_times.append(time)

    schedule_order = []

    for time in test_times:
        for days in test_days:
            schedule_order.append((days, time))

    # print(schedule_order)

    return schedule_order
