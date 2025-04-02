import re

faculty_table_name = "Faculty"
courses_table_name = "Course"

class Faculty:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def create_sql(self):
        return f'INSERT INTO {faculty_table_name} ({self.id}, "{self.name}", NULL, NULL, NULL)'
        
    def __repr__(self):
        return f'Fid: {self.id}\nName: {self.name}\n'

class Course:
    def __init__(self, course_code, crn, name, faculty):
        self.course_code = course_code
        self.crn = crn
        self.name = name
        self.faculty = faculty
        self.duration = 80
        
    def create_sql(self):
        return f'INSERT INTO {courses_table_name} ({self.crn}, {self.course_code}, "{self.faculty}", "{self.name}", {self.duration}, NULL, NULL, False)'
        
    def __repr__(self):
        return f'Course Code: {self.course_code}\nCRN: {self.crn}\nName: {self.name}\nFaculty: {self.faculty}'


def main():
    courses = []
    faculty = []
    fid = 0
    
    grouped_lines = []
    with open("parsed.txt") as f:
        lines = f.readlines()

    for i in range(0, len(lines), 4):
        grouped_lines.append([lines[i], lines[i + 1], lines[i + 2], lines[i + 3]])

    for line in grouped_lines:
        print(line, end="\n\n")

    for course_info in grouped_lines:
        # print(course_info)
        # Extract CRN
        crn = re.findall(r"Class Number: (\d*)", course_info[0])[0]

        # Extract course_number
        number_and_name = re.search(r"Course Info: ICSI (\d*)(.*)", course_info[1])
        course_number = number_and_name.group(1)

        # Extract course_name
        course_name = " ".join(number_and_name.group(2).split(" ")[1:])

        
        # Extract faculty_name
        faculty_name = course_info[2].split(' ')[-1].strip().replace(',', ' ').replace('_', ' ')
        
        # Ignore the "Arranged" name courses
        if faculty_name == "Arranged":
            continue
        
        # Add faculty object if not in table
        new_name = True
        for faculty_member in faculty:
            if faculty_member.name == faculty_name:
                new_name = False
        if new_name:
            faculty.append(Faculty(faculty_name, fid))
            fid += 1
            
        # Create course object
        courses.append(Course(course_number, crn, course_name, faculty[-1].id))
        
    for course in courses:
        print(course)
        print(faculty[course.faculty].name)
        print()
        
    # print(len(courses))
    
    with open('out.sql', "w") as f:
        for course in courses:
            f.write(f'{course.create_sql()}\n\n')
        
        for faculty_member in faculty:
            f.write(f'{faculty_member.create_sql()}\n\n')

if __name__ == "__main__":
    main()


# DEAL WITH TOMORROW
# import re

# text = """Course Description: Introduction to the design and implementation of programming languages, including language features, paradigms and design decisions. Briefly covers functional and logical programming paradigms and reinforces object-oriented concepts. Discusses interpreters, compilers, transpires and virtual machines, including lexical analysis, parsing, semantic analysis, optimization, code generation. Introduction to automata and state machines. Prerequisite(s): grade of C or better required in I CSI 210 and I CSI 213."""

# # Find everything after "Prerequisite(s):"
# prereq_match = re.search(r"Prerequisite\(s\):(.+)", text)

# if prereq_match:
#     prereq_text = prereq_match.group(1)  # Extract only the part after "Prerequisite(s):"

#     # Find all "I CSI" numbers within that section
#     matches = re.findall(r"I CSI (\d+)", prereq_text)

#     print(matches)  # Output: ['210', '213']
