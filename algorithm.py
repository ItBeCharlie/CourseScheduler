from database_requests import *


# Object to store only the critical course information
class Course:
    def __init__(self, crn, course_code, is_pinned):
        self.crn = crn
        self.course_code = course_code
        self.conflict_numbers = []
        self.is_pinned = is_pinned

    def __repr__(self):
        # return f"(CRN: {self.crn} Course_Code: {self.course_code} Pinned: {self.is_pinned})"
        return f"{self.crn}, {self.conflict_numbers}\n"


def generate_graph(prereq_list):
    """
    Input: Array of tuples from the prereq table in the form
    [prereq_course, main_course]

    Output: Hashmap containing the main_course as the key,
    and the list of it's prereqs as the value.
    """
    # Define output graph
    graph = {}
    for row in prereq_list:
        # Unpack the tuple
        prereq_course, main_course = row
        # Make sure the initial value is set for a new main course
        if main_course not in graph:
            graph[main_course] = []
        # Add the prereq course into the graph
        graph[main_course].append(prereq_course)
    return graph


def reverse_graph(input_graph):
    """
    Input: A hashmap graph of courses and their prereqs

    Output: A reversed order traversal where the items in the prereq list valeus are now the keys
    """
    graph = {}
    for main_course, prereq_list in input_graph.items():
        # Iterate over the prereq courses as our new keys
        for prereq_course in prereq_list:
            # Set the initial value of the prereq_course list
            if prereq_course not in graph:
                graph[prereq_course] = []
            # Add the main_course to the reversed list
            graph[prereq_course].append(main_course)
    return graph


def find_roots(graph):
    """
    Input: A hashmap graph of courses

    Output: The roots of the graph (courses with no incoming edges)
    """
    # Determine if incoming edge has been seen before, initialize to False
    seen_incoming = {}
    for node in graph:
        seen_incoming[node] = False

    # For every node, set all future nodes to having an incoming node
    for node in graph:
        for neighbor in graph[node]:
            seen_incoming[neighbor] = True

    roots = []
    for node, seen in seen_incoming.items():
        if not seen:
            roots.append(node)
    return roots


def calculate_depths(graph):
    """
    Input: A hashmap graph of courses and their prereqs

    Output: A hashmap containing a depth as the key and a list of courses at that depth as the value. A courses depth is determined by the minimum value found
    """
    # Keeps track of each course and the current depth of that course
    course_depth_pairs = {}
    # Queue used for DFS traversal
    queue = []
    # Roots for initializing all DFS's
    roots = find_roots(graph)
    for root in roots:
        # Initialize the DFS
        queue.append(root)
        # Initialize root depth to 0
        course_depth_pairs[queue[0]] = 0
        # Continually iterate over nodes until stack is empty, then move on to next root
        while len(queue) != 0:
            # Store the current top of stack
            current_node = queue[0]
            # Ensure the node is not a leaf node
            if current_node in graph:
                # Iterate over all future nodes, setting the depth to minimum of parent depth + 1 and their current depth
                for child_node in graph[current_node]:
                    # Update depth of next item in stack
                    if child_node not in course_depth_pairs:
                        course_depth_pairs[child_node] = (
                            course_depth_pairs[current_node] + 1
                        )
                    else:
                        course_depth_pairs[child_node] = min(
                            course_depth_pairs[current_node] + 1,
                            course_depth_pairs[child_node],
                        )
                    # Add child to queue
                    queue.append(child_node)
            # Remove current_node from queue
            queue.pop(0)

    # Based on course_depth_pairs, group all courses of same depth in lists stored in hashmap
    output = {}
    for course, depth in course_depth_pairs.items():
        # Initialize output list
        if depth not in output:
            output[depth] = []
        output[depth].append(course)
    return output


def debug_print_graph(graph):
    """
    Input: A hashmap graph of courses and their prereqs

    Output: A debug print showing the connections
    """
    for main_course, prereq_list in graph.items():
        print(main_course, prereq_list)


def get_course_map():
    """
    Input: None

    Output: Two Hashmaps. The first containing course codes as keys and a list of course objects who all share that course code as values.
    The second containing crns as keys and a single course object as the values.
    """
    # Load all course tuples from database
    all_courses = load_all_courses()
    # Output hashmaps
    code_map = {}
    crn_map = {}
    for course in all_courses:
        course_object = Course(
            crn=course[0], course_code=course[1], is_pinned=course[2]
        )
        # Add object to code map
        if course_object.course_code not in code_map:
            code_map[course_object.course_code] = []
        code_map[course_object.course_code].append(course_object)
        # Add object to crn map
        crn_map[course_object.crn] = course_object
    return code_map, crn_map


def generate_conflict_numbers():
    # Initialize conflict number counter
    current_conflict_number = 0
    # Load in all courses and create a hashmap mapping from course_code to list of Course objects with crn's corresponding to that code
    code_object_map, crn_object_map = get_course_map()
    # Get the prereq information for generating graphs
    prereq_list = get_prereq_list()
    # Generate the graphs for both directions
    backward_graph = generate_graph(prereq_list)
    forward_graph = reverse_graph(backward_graph)
    # Get the depths for the forwards and backwards graph traversals
    backward_depths = calculate_depths(backward_graph)
    forward_depths = calculate_depths(forward_graph)

    # STEP 1 PART 1: DEPTH TRAVERSAL

    # Iterate over backwards depths and add conflict number to all courses with the same depth
    for depth, courses in backward_depths.items():
        for course in courses:
            # Get all courses with this course code from the mapping
            same_code_courses = code_object_map[course]
            for same_code_course_object in same_code_courses:
                # Give the course the current conflict number
                same_code_course_object.conflict_numbers.append(current_conflict_number)
        # Increment the global conflict number counter
        current_conflict_number += 1
    # Iterate over forward depths and add conflict number to all courses with the same depth
    for depth, courses in forward_depths.items():
        for course in courses:
            # Get all courses with this course code from the mapping
            same_code_courses = code_object_map[course]
            for same_code_course_object in same_code_courses:
                # Give the course the current conflict number
                same_code_course_object.conflict_numbers.append(current_conflict_number)
        # Increment the global conflict number counter
        current_conflict_number += 1

    # STEP 1 PART 3: FACULTY GROUPING

    faculty_groups = load_teaches()
    # Data is preformatted for faculty, simply add entire list to same group
    for faculty, courses in faculty_groups.items():
        for course in courses:
            crn_object_map[course].conflict_numbers.append(current_conflict_number)
        current_conflict_number += 1

    print(crn_object_map)


if __name__ == "__main__":
    # main()
    generate_conflict_numbers()
