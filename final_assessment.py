"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""


class CFGStudent:

    def __init__(self,name,surname,age,email,student_id):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = student_id

    @staticmethod
    def generate_id():
        student_id = random.randint(100, 1000)
        return student_id
        'your code goes here'
        'create a random new id, which is any number between 1,000 and 10,000'
        'return id as a string'
        "Example '8754' "

    def get_id(self):
        def get_id(self, student_id):
            self.student_id = student_id
            print("student id:" + self.student_id)
        'your code goes here'
        'fetch student id'

    def get_fullname(self):
        def get_fullname(self, name, surname):
            self.name = name
            self.surname = surname
            print("full name:" + self.name + self.surname)
        "Expected outcome should be 'Name Surname' "
        'your code goes here'


class NanoStudent(CFGStudent):

    def __init__(self, specialization, course_grades):

        self.specialization =specialization
        self.course_grades = course_grades

    @staticmethod
    def generate_id():
        student_id = random.randint(100, 1000)
        new_id=NANO+student_id
        return new_id
        'your code goes here'
        'create a random new id, which is a word NANO followed by any number between 1,000 and 10,000'
        'return id as a string'
        "Example 'NANO1234' "

    def add_new_grade(self, task_name, grades):
        self.task_name=task_name
        self.grades=grades
        self.course_grades={}
        self.course_grades.append(task_name)
        self.course_grades.setdefault(grades)



        'your code goes here'
        'update course_grades container'
        "Example: pass in a task name and its grade, so that both are added to course_grades"

    def get_course_grades(self):

         #course_grades.get('key')
        # we can pass task name which is a key to get method and it result grades as value
        #print("for course" +str(key) " grade is"+str(value))



############################################

# Example run

s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}



"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""

def even_fibnocci_sum(limit):
    a,b=0,1
    list=[0]
    even_sum = 0
    for i in range(limit-2):
      sum=a+b
      a,b=b,sum
      if sum%2==0:
        list.append(sum)
    for i in list:
        even_sum=even_sum+i
    print(even_sum)

##### TESTS ####

print(even_fibonacci_sum(10))  # should be 44
print(even_fibonacci_sum(15))  # should be 188
print(even_fibonacci_sum(1))   # should be 0





"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 
"""



#### TESTS ####


def is_valid_subsequence(array1, sequence1):

    array1 = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence1 = [1, 6, -1, -2]
    list2=[]
    for i in sequence1:
        for j in array1:
            if i==j:

               array1.pop(j)
               list2.append(j)
        i=i+1

    if list2==sequence1:
        print("true")
    else:
        print("false")
print(is_valid_subsequence(array1 = [5,1,22,25,6,-1,8,10],sequence1 = [25]))


array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

print(is_valid_subsequence(array1, sequence1))  # FALSE


array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE



"""
TASK 4

WRITTEN ASSIGNMENT

Write a review on how 'class Employee' can be improved.
(See PDF document with the code example)
"""


1. In the __init__ method , self.active status=is_active can be changed as self.is_active=is_active . Since, the variable
 in the 'init' constructor has name is_active
2. self.id can be changed to self.id_ since the variable in the 'init' has name id_ and we need to assign value to variable in the
'init' constructor through self.id_=id_
3.
In the update_department method , the variable assignment should be made self.department_name=department_name , since we
have already named method parameter as department_name in the method

4. in the method update_status, change variable assignment as self.new_is_active =new_is_active

5. In method save_employee, change self.active_status to self.is_active and self.id to self.id_

6.In method remove_employee, change self.id to self.id_

7. Inn method print report, change self.id to self.id_ and self.active_status to self.is_active and self.path=path




