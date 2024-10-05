def read_file(file_name: str):
    problem = []
    with open(file_name, 'r') as file:
        file_contents = file.readlines()
        for line in file_contents:
            problem.append(line.split(','))
    for i, line in enumerate(problem):
        problem[i] = list(map(int, line))
    return problem
