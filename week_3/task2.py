students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]
def validate_score(score):
    return 0 <= score <= 100
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
def calculate_average(students):
    total = 0
    count = 0

    for student in students:
        score = student["score"]

        if validate_score(score):
            total += score
            count += 1

    if count == 0:
        return 0

    return total / count
def find_highest_lowest(students):
    valid_scores = []

    for student in students:
        score = student["score"]

        if validate_score(score):
            valid_scores.append(score)

    if len(valid_scores) == 0:
        return None, None

    highest = valid_scores[0]
    lowest = valid_scores[0]

    for score in valid_scores:
        if score > highest:
            highest = score

        if score < lowest:
            lowest = score

    return highest, lowest
def count_passed_failed(students):
    passed = 0
    failed = 0

    for student in students:
        score = student["score"]

        if not validate_score(score):
            continue

        if score >= 50:
            passed += 1
        else:
            failed += 1

    return passed, failed
def students_above_average(students):
    average = calculate_average(students)
    result = []

    for student in students:
        score = student["score"]

        if validate_score(score) and score > average:
            result.append(student["name"])

    return result
def generate_report(students):
    valid_students = []

    for student in students:
        if validate_score(student["score"]):
            valid_students.append(student)

    if len(valid_students) == 0:
        print("No valid student scores found.")
        return

    average = calculate_average(valid_students)
    highest, lowest = find_highest_lowest(valid_students)
    passed, failed = count_passed_failed(valid_students)

    print("===== STUDENT PERFORMANCE REPORT =====")

    for student in valid_students:
        name = student["name"]
        score = student["score"]
        grade = calculate_grade(score)

        if score >= 50:
            status = "Pass"
        else:
            status = "Fail"

        print(
            name,
            "| Score:", score,
            "| Grade:", grade,
            "| Status:", status
        )

    print("--------------------------------------")
    print("Class Average:", round(average, 2))
    print("Highest Score:", highest)
    print("Lowest Score:", lowest)
    print("Passed Students:", passed)
    print("Failed Students:", failed)
    print("Above Class Average:", students_above_average(valid_students))

generate_report(students)