class VirtualClassroomManager:
    def __init__(self):
        self.classrooms = {}
        self.students = {}
        self.assignments = {}

    def add_classroom(self, class_name):
        if class_name not in self.classrooms:
            self.classrooms[class_name] = []
            print(f"Classroom '{class_name}' has been created.")
        else:
            print(f"Classroom '{class_name}' already exists.")

    def add_student(self, student_id, class_name):
        if class_name in self.classrooms:
            if student_id not in self.students:
                self.students[student_id] = class_name
                self.classrooms[class_name].append(student_id)
                print(f"Student '{student_id}' has been enrolled in '{class_name}'.")
            else:
                print(f"Student '{student_id}' is already enrolled in a classroom.")
        else:
            print(f"Classroom '{class_name}' does not exist.")

    def schedule_assignment(self, class_name, assignment_details):
        if class_name in self.classrooms:
            assignment_key = f"{class_name}_{len(self.assignments) + 1}"
            self.assignments[assignment_key] = assignment_details
            print(f"Assignment for '{class_name}' has been scheduled.")
        else:
            print(f"Classroom '{class_name}' does not exist.")

    def submit_assignment(self, student_id, class_name, assignment_details):
        if student_id in self.students and class_name == self.students[student_id]:
            assignment_key = f"{class_name}_{len(self.assignments)}"
            if assignment_key in self.assignments and not self.assignments[assignment_key].get('submitted'):
                self.assignments[assignment_key]['submitted'] = True
                print(f"Assignment submitted by Student '{student_id}' in '{class_name}'.")
            else:
                print("Assignment has already been submitted or does not exist.")
        else:
            print(f"Student '{student_id}' is not enrolled in '{class_name}'.")

    def list_classrooms(self):
        print("List of Classrooms:")
        for classroom in self.classrooms:
            print(f"- {classroom}")

    def list_students(self, class_name):
        if class_name in self.classrooms:
            print(f"List of Students in '{class_name}':")
            for student_id in self.classrooms[class_name]:
                print(f"- {student_id}")
        else:
            print(f"Classroom '{class_name}' does not exist.")

# Main program
manager = VirtualClassroomManager()

# Example usage
manager.add_classroom("Physics101")
manager.add_student("123", "Physics101")
manager.list_classrooms()
manager.list_students("Physics101")
manager.schedule_assignment("Physics101", {"title": "Physics Assignment 1", "due_date": "2023-11-30"})
manager.submit_assignment("123", "Physics101", {"title": "Physics Assignment 1", "due_date": "2023-11-30"})
