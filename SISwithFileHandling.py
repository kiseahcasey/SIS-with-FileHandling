import csv

class StudentSystem:
    def __init__(self):
        #dictionary
        self.students = {}

    #methods
    def add_student(self, student_id, name, age, *grades):
        """Add a new student (tuple demo for ID and name)."""
        student_tuple = (student_id, name)
        self.students[student_id] = {
            "name": name,
            "age": age,
            "grades": list(grades)
        }
        print(f"Added student {student_tuple}.")

    def display_students(self, from_file=False, filename="students.csv"):
        """Display all students (loop, nested loop, slicing demo)."""
        if from_file:
            try:
                with open(filename, mode="r") as f:
                    reader = csv.reader(f)
                    print("\n===== Students from File =====")
                    for row in reader:
                        print(row)
                return
            except FileNotFoundError:
                print("No saved file found.")
                return

        if not self.students:
            print("No students available.")
            return

        print("\n===== Students in Memory =====")
        for sid, info in self.students.items():  #for loop
            print(f"ID: {sid}, Name: {info['name']}, Age: {info['age']}")
            print("Grades:", end=" ")
            for g in info['grades']:  #nested loop
                print(g, end=" ")
            print()

        keys_list = list(self.students.keys())
        print("\nSlicing demo (first 2 students):", keys_list[:2])

    def update_student(self, student_id, new_name=None, new_age=None, new_grades=None):
        """Update student info (pass by reference demo)."""
        if student_id in self.students:
            if new_name:
                self.students[student_id]["name"] = new_name
            if new_age:
                self.students[student_id]["age"] = new_age
            if new_grades is not None:
                self.students[student_id]["grades"][:] = new_grades
            print(f"Student {student_id} updated.")
        else:
            print("Student not found.")

    def delete_student(self, student_id):
        """Delete student record."""
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student {student_id} deleted.")
        else:
            print("Student not found.")

    def save_to_file(self, filename="students.csv"):
        """Save students to CSV file."""
        with open(filename, mode="w", newline="") as f:
            writer = csv.writer(f)
            for sid, info in self.students.items():
                writer.writerow([sid, info["name"], info["age"], *info["grades"]])
        print(f"Data saved to {filename}")

    def load_from_file(self, filename="students.csv"):
        """Load students from CSV file."""
        try:
            with open(filename, mode="r") as f:
                reader = csv.reader(f)
                for row in reader:
                    sid, name, age, *grades = row
                    self.students[sid] = {
                        "name": name,
                        "age": int(age),
                        "grades": list(map(int, grades))
                    }
            print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print("No file to load.")


#main program
if __name__ == "__main__":
    system = StudentSystem()

    #para ma-calculate yung ave grade
    average = lambda grades: sum(grades) / len(grades) if grades else 0

    while True:
        print("\n===== Student Information System ====="
              "\n1. Add Student"
              "\n2. Display Students"
              "\n3. Update Student"
              "\n4. Delete Student"
              "\n5. Save to File"
              "\n6. Load from File"
              "\n7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grades_input = input("Enter grades separated by space: ").split()
            grades = list(map(int, grades_input))
            system.add_student(student_id, name, age, *grades)

        elif choice == "2":
            sub_choice = input("Display from (1) memory or (2) file? ")
            if sub_choice == "1":
                system.display_students()
            elif sub_choice == "2":
                system.display_students(from_file=True)
            else:
                print("Invalid option, continue...")
                continue

        elif choice == "3":
            student_id = input("Enter student ID to update: ")
            new_name = input("Enter new name (leave blank to skip): ")
            new_age = input("Enter new age (leave blank to skip): ")
            new_age = int(new_age) if new_age else None
            grades_input = input("Enter new grades (leave blank to skip): ").split()
            new_grades = list(map(int, grades_input)) if grades_input else None
            system.update_student(student_id, new_name or None, new_age, new_grades)

        elif choice == "4":
            student_id = input("Enter student ID to delete: ")
            system.delete_student(student_id)

        elif choice == "5":
            system.save_to_file()

        elif choice == "6":
            system.load_from_file()

        elif choice == "7":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice, try again.")
