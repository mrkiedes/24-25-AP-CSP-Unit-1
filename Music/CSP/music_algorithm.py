import random
import json
import os

class PityRandom:
    def __init__(self, num_students):
        self.num_students = num_students
        self.history = []
        self.weights = [1] * num_students
        self.load_history()

    def pick_student(self):
        total_weight = sum(self.weights)
        probabilities = [w / total_weight for w in self.weights]
        student = random.choices(range(1, self.num_students + 1), probabilities)[0]

        # Update history and weights
        self.history.append(student)
        if len(self.history) > 10:  # Keep history size manageable
            self.history.pop(0)

        self.update_weights()
        self.save_history()
        return student

    def update_weights(self):
        self.weights = [1] * self.num_students
        for student in self.history:
            if 1 <= student <= self.num_students:
                self.weights[student - 1] *= 0.5  # Decrease weight for recently picked students

    def load_history(self):
        if os.path.exists('history.json'):
            with open('history.json', 'r') as file:
                data = json.load(file)
                self.history = [num for num in data.get('history', []) if 1 <= num <= self.num_students]
                self.update_weights()

    def save_history(self):
        with open('history.json', 'w') as file:
            json.dump({'history': self.history}, file)

# Example usage
num_students = int(input("Enter the number of students in the class: "))
pity_random = PityRandom(num_students)
print(pity_random.pick_student())