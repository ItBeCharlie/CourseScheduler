# import_csv.py
#
# One‑shot CSV → MySQL seeding utility.
#
# Tables created earlier in phpMyAdmin:
#   Courses(CRN PK,  Course_Code, Is_Pinned, Duration,
#           Start_Time, End_Time, Days, Faculty)
#   Prereqs(Main_Course_Code, Prereq_Course_Code)          PK(main, prereq)
#   Coreqs(CRN1, CRN2)                                     PK(CRN1, CRN2)
#   Teaching(Faculty, CRN)                                 PK(Faculty, CRN)

import csv
import sys
from typing import List

import mysql.connector
from Course import Course


# ---------------------------------------------------------------------------#
#  Utility
# ---------------------------------------------------------------------------#
def _get_connection():
    """Return a fresh MySQL connection using XAMPP defaults."""
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="CourseSchedulerDB",
    )


# ---------------------------------------------------------------------------#
#  Phase 1 – turn CSV rows into Course objects
# ---------------------------------------------------------------------------#
def build_course_objects(input_csv_file: str) -> List[Course]:
    """Parse the registrar CSV and return Course objects."""
    courses: List[Course] = []

    with open(input_csv_file, newline="") as fh:
        reader = csv.reader(fh)
        next(reader)  # skip header
        for row in reader:
            crn, code, faculty_raw, prereqs_raw, coreqs_raw, pinned = row[:6]

            c = Course(crn=crn, course_code=code)

            # Boolean pinned flag
            c.is_pinned = pinned.strip().upper() == "TRUE"

            # keep first faculty name if several are concatenated with '.'
            c.faculty = faculty_raw.split(".")[0]

            # lists of strings (may be empty)
            if prereqs_raw != "None":
                c.prereqs = prereqs_raw.split(".")
            if coreqs_raw != "None":
                c.coreqs = coreqs_raw.split(".")

            courses.append(c)

    return courses


# ---------------------------------------------------------------------------#
#  Phase 2 – writers for each table
# ---------------------------------------------------------------------------#
def update_courses_table(courses: List[Course]) -> None:
    conn = _get_connection()
    cur = conn.cursor()

    sql = """
        INSERT INTO Courses
            (CRN, Course_Code, Is_Pinned, Duration,
             Start_Time, End_Time, Days, Faculty)
        VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            Course_Code = VALUES(Course_Code),
            Is_Pinned   = VALUES(Is_Pinned),
            Duration    = VALUES(Duration),
            Start_Time  = VALUES(Start_Time),
            End_Time    = VALUES(End_Time),
            Days        = VALUES(Days),
            Faculty     = VALUES(Faculty);
    """

    for c in courses:
        cur.execute(
            sql,
            (
                c.crn,
                c.course_code,
                c.is_pinned,
                c.duration,
                c.start_time,
                c.end_time,
                "".join(c.days) if c.days else None,
                c.faculty,
            ),
        )

    conn.commit()
    cur.close()
    conn.close()


def update_prereqs_table(courses: List[Course]) -> None:
    conn = _get_connection()
    cur = conn.cursor()

    sql = """
        INSERT IGNORE INTO Prereqs
            (Main_Course_Code, Prereq_Course_Code)
        VALUES (%s, %s);
    """

    for c in courses:
        for prereq in c.prereqs:
            cur.execute(sql, (c.course_code, prereq))

    conn.commit()
    cur.close()
    conn.close()


def update_coreqs_table(courses: List[Course]) -> None:
    conn = _get_connection()
    cur = conn.cursor()

    sql = """
        INSERT IGNORE INTO Coreqs
            (CRN1, CRN2)
        VALUES (%s, %s);
    """

    for c in courses:
        for coreq_crn in c.coreqs:
            # store only one direction; PK prevents duplicates
            cur.execute(sql, (c.crn, coreq_crn))

    conn.commit()
    cur.close()
    conn.close()


def update_teaches_table(courses: List[Course]) -> None:
    conn = _get_connection()
    cur = conn.cursor()

    sql = """
        INSERT IGNORE INTO Teaching
            (Faculty, CRN)
        VALUES (%s, %s);
    """

    for c in courses:
        cur.execute(sql, (c.faculty, c.crn))

    conn.commit()
    cur.close()
    conn.close()


# ---------------------------------------------------------------------------#
#  CLI entry‑point
# ---------------------------------------------------------------------------#
def main(csv_path: str) -> None:
    courses = build_course_objects(csv_path)

    update_courses_table(courses)
    update_prereqs_table(courses)
    update_coreqs_table(courses)
    update_teaches_table(courses)

    print("Database seeded from", csv_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:  python import_csv.py <csv_path>")
        sys.exit(1)
    main(sys.argv[1])
