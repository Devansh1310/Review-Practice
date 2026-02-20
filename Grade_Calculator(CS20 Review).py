def get_grades():
    grades = []

    while True:
        user_input = input("Enter the student grade: ")

        if user_input.lower() == "done":
            break

        try:
            grade = int(user_input)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Enter a valid number between 0 and 100.")
        except ValueError:
            print("Invalid input.")

    return grades

def calculate_statistics(grades):
    avg = sum(grades)/len(grades)

    highest = max(grades)
    lowest = min(grades)
    
    return avg, highest, lowest

def assign_letter(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def main():
    grades = get_grades()
    avg, max, min = calculate_statistics(grades)
    print("Class Average: " + str(avg))
    print("Overall Performace: " + assign_letter(avg))
    print("Highest Grade: " + str(max))
    print("Lowest Grade: " + str(min))

if __name__ == "__main__":
    main()