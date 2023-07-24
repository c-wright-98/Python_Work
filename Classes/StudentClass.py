class student:
    '''
    Student class:
    The initial attributes of the student class are the students name which is a string,
    student's age which is an integer and the student's class which is defaulted to student
    it also includes the student's empty test score list.

    The class has two functions
    '''
    def __init__(self, name:str, age:int, studentclass='student'):
        '''
        This is the initialised attributes of the student class and includes:
        the student's name as a string,
        age as an int and student,
        studentclass defaulted to student
        it also includes the student's empty test score list
        '''
        self.name = name
        self.age = age
        self.studentclass = studentclass
        self.test_score = []

    def add_test_score(self):
        '''
        add_test_score: This function prompts the user to input three test scores and adds them to the empty test_score list
        '''
        while len(self.test_score) < 3:
            score = int(input('Enter student test score: '))
            self.test_score.append(score)

    def get_average_test_score(self):
        '''
        get_average_test_score: This function returns the average test score from the entered test scores stored in the test_score list.
        '''
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
