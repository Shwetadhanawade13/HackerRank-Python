if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Get all scores
    scores = []

    for student in students:
        scores.append(student[1])

    # Find second lowest score
    second_lowest = sorted(set(scores))[1]

    # Find names having second lowest score
    names = []

    for student in students:
        if student[1] == second_lowest:
            names.append(student[0])

    # Sort names alphabetically
    names.sort()

    # Print names
    for name in names:
        print(name)