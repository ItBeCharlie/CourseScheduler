"""
Input: Array of tuples from the prereq table in the form
[prereq_course, main_course]

Output: Hashmap containing the main_course as the key,
and the list of it's prereqs as the value.
"""


def generate_graph(prereq_list):
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


"""
Input: A hashmap graph of courses and their prereqs

Output: A reversed order traversal where the items in the prereq list valeus are now the keys
"""


def reverse_graph(input_graph):
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


"""
Input: A hashmap graph of courses and their prereqs

Output: A debug print showing the connections
"""


def debug_print_graph(graph):
    for main_course, prereq_list in graph.items():
        print(main_course, prereq_list)


def test_graph():
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

    graph = generate_graph(test_prereq_list)
    debug_print_graph(graph)
    print()
    reversed_graph = reverse_graph(graph)
    debug_print_graph(reversed_graph)


def main():
    test_graph()


if __name__ == "__main__":
    main()
