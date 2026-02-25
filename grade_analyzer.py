# Task 1 — Process the Scores
def process_scores(students):
    averages = {}

    for name in students:
        scores = students[name]
        avg = round(sum(scores) / len(scores), 2)
        averages[name] = avg

    return averages


# Task 2 — Classify the Grades
def classify_grades(averages):
    A_threshold = 90
    B_threshold = 75
    C_threshold = 60

    classified = {}

    for name in averages:
        avg = averages[name]

        if avg >= A_threshold:
            grade = "A"
        elif avg >= B_threshold:
            grade = "B"
        elif avg >= C_threshold:
            grade = "C"
        else:
            grade = "F"

        classified[name] = (avg, grade)

    return classified


# Task 3 — Generate the Report
def generate_report(classified, passing_avg=70):
    print("===== Student Grade Report =====")

    total_students = len(classified)
    passed = 0
    failed = 0

    for name in classified:
        avg, grade = classified[name]

        if avg >= passing_avg:
            status = "PASS"
            passed += 1
        else:
            status = "FAIL"
            failed += 1

        print(f"{name:<10} | Avg: {avg:.2f} | Grade: {grade} | Status: {status}")

    failed = total_students - passed

    print("================================")
    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")

    return passed


# Main block
if __name__ == "__main__":
    students = {
        "Alice": [85, 90, 84],
        "Bob": [60, 65, 62],
        "Clara": [95, 97, 97]
    }

    averages = process_scores(students)
    classified = classify_grades(averages)
    generate_report(classified)
