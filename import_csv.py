from Course import *


def build_course_objects(input_csv_file):
    """
    Given the input_csv file, returns a list of Course objects to be used to populate the database
    """

    courses = []
    with open(input_csv_file) as f:
        line = f.readline()
        line = f.readline()
        while line != "":
            split_line = line.split(",")
            new_course = Course(crn=split_line[0], course_code=split_line[1])
            if split_line[5] == "FALSE":
                new_course.is_pinned = False
            elif split_line[5] == "TRUE":
                new_course.is_pinned = True
            # If multiple faculty, only store 1 of them, can't handle multiple
            new_course.faculty = split_line[2].split(".")[0]
            if split_line[3] != "None":
                new_course.prereqs = split_line[3].split(".")
            if split_line[4] != "None":
                new_course.coreqs = split_line[4].split(".")
            courses.append(new_course)
            line = f.readline()

    # for course in courses:
    #     print(course)

    return courses


def update_courses_table(courses):
    """
    Given a list of course objects, extract the information to perform update queries to DB
    """
    for course in courses:
        pass


def update_faculty_table(courses):
    pass


def update_teaches_table(courses):
    pass


if __name__ == "__main__":
    courses = build_course_objects("graduate_icsi_spring_2025_in_person_classes.csv")
