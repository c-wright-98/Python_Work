class student:

    def __init__(self, name:str, age:int, studentclass='student'):
        self.name = name
        self.age = age
        self.studentclass = studentclass
        self.test_score = []

    def add_test_score(self):
        while len(self.test_score) < 3:
            score = int(input('Enter student test score: '))
            self.test_score.append(score)

    def get_average_test_score(self):
        if not self.test_score:
            print("No test scores available.")
            return

        average_score = sum(self.test_score) / len(self.test_score)
        print(f"{self.name}'s average test score is: {average_score}")


student1 = student('John', 18)
student2 = student('Emily', 21)

student1.add_test_score()
student1.get_average_test_score()

student2.add_test_score()
student2.get_average_test_score()
