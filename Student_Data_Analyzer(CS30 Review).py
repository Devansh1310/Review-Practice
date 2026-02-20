class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(self.name, "-", self.grade)

    def __str__(self):
        return f"{self.name} - {self.grade}"

def linear_search(students, target_name):
    for i in range(len(students)):
        if students[i].name == target_name:
            return students[i]
    return students[-1]

def binary_search(students, target_grade):
    sorted_students = selection_sort(students[:])  # make copy
    
    left = 0
    right = len(sorted_students) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if sorted_students[mid].grade == target_grade:
            return sorted_students[mid]
        elif sorted_students[mid].grade < target_grade:
            left = mid + 1 
        else:
            right = mid - 1
            
    return None

def selection_sort(students):
    n = len(students)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if students[j].grade < students[min_index].grade:
                min_index = j
        students[i], students[min_index] = students[min_index], students[i]
    return students 

def calculate_stats(students):
    grades = [student.grade for student in students]

    avg = sum(grades)/len(grades)
    highest = max(grades)
    lowest = min(grades)

    return avg, highest, lowest

def main():
    students = [
        Student("Alice", 85),
        Student("Bob", 92),
        Student("Charlie", 78),
        Student("David", 88)
    ]

    while True:
        print("\n1. Display All")
        print("2. Search by Name")
        print("3. Search by Grade")
        print("4. Sort by Grade")
        print("5. Show Statistics")
        print("6. Exit")
        print("\n")

        choice = input("Choose: ")
        if choice == "1":
            for i in range(len(students)):
                students[i].display()
        elif choice == "2":
            target_name = input("What's the name?")
            print(linear_search(students, target_name))
        elif choice == "3":
            target_grade = int(input("What's the grade?"))
            print(binary_search(students, target_grade))
        elif choice == "4":
            print(selection_sort(students))
            for student in students:
                student.display()
        elif choice == "5":
            print("Average:", calculate_stats(students)[0])
            print("Highest:", calculate_stats(students)[1])
            print("Lowest:", calculate_stats(students)[2])
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()