# database_requests.py
#
# Lightweight read‑helpers used by the scheduling algorithm.
# All functions talk directly to MySQL and return plain Python types.

import mysql.connector
from time_conversion import time_str2int


# ---------------------------------------------------------------------------#
#  Utility
# ---------------------------------------------------------------------------#
def _get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="CourseSchedulerDB",
    )


# ---------------------------------------------------------------------------#
#  Public API
# ---------------------------------------------------------------------------#
def get_prereq_list():
    """
    Returns a list[tuple[str,str]] of (prereq_course, main_course)
    """
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT Prereq_Course_Code, Main_Course_Code FROM Prereqs;"
        )
        return list(cur.fetchall())


def load_all_courses():
    """
    Returns a list[tuple] of
    (CRN, Course_Code, is_pinned, duration, start_time, end_time, days)
    with times converted to int minutes and days to list[str] / None.
    """
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT CRN, Course_Code, Is_Pinned, Duration,
                   Start_Time, End_Time, Days
            FROM Courses;
            """
        )
        rows = cur.fetchall()

    converted = []
    for crn, code, pinned, dur, st, et, days in rows:
        converted.append(
            (
                crn,
                code,
                bool(pinned),
                dur,
                time_str2int(str(st)) if st else None,
                time_str2int(str(et)) if et else None,
                list(days) if days else None,
            )
        )
    return converted


def load_teaches():
    """
    Returns dict[str, list[str]]  →  {faculty: [CRN, ...]}
    """
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT Faculty, CRN FROM Teaching;")
        mapping = {}
        for faculty, crn in cur.fetchall():
            mapping.setdefault(faculty, []).append(crn)
        return mapping


def get_coreq_list():
    """
    Returns list[tuple[str,str]] of (CRN1, CRN2)
    """
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT CRN1, CRN2 FROM Coreqs;")
        return list(cur.fetchall())


def load_possible_times():
    """
    Returns a list of (days:list[str], start_time:int) tuples that the
    algorithm can iterate over.
    """
    with _get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_schema = DATABASE()
              AND table_name   = 'PossibleTimes';
            """
        )
        table_exists = cur.fetchone()[0] == 1

        if table_exists:
            cur.execute("SELECT DayPattern, Start_Time FROM PossibleTimes;")
            rows = cur.fetchall()
            schedule_order = []
            for day_pat, start_time in rows:
                days = day_pat.split(".")  # e.g. 'M.W' → ['M','W']
                schedule_order.append((days, time_str2int(str(start_time))))
            return schedule_order

    # ---------- fallback grid ---------- #
    start_time = time_str2int("8:00")
    end_time = time_str2int("19:00")
    increment = 90
    day_patterns = [["M", "W"], ["T", "TH"]]

    grid = []
    for t in range(start_time, end_time + 1, increment):
        for days in day_patterns:
            grid.append((days, t))
    return grid
