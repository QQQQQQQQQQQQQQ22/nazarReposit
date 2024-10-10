class computer_course: #батьківський клас
    def __init__(self, course_name, duration):
        self.__course_name = course_name
        self.__duration = duration
    def my_course(self):
        print(self.__course_name,self.__duration,sep=" | ")
    def get_course_name(self):
        return self.__course_name
    def get_duration(self):
        return self.__duration
    def set_duration(self,duration):
        self.__duration = duration
    @staticmethod
    def List_of_course_name():
        print(["python for litle","c++ for teapots","Python cours for master"],sep=" | ")
class computer_course_standart(computer_course): #дочірній
    def __init__(self,course_name, duration, instructor,cost):
        super().__init__(course_name, duration)
        self.instructor = instructor
        self.cost = cost
    def change_instructor(self,instructor):
        self.instructor = instructor
    def my_course(self):
        print(self.get_course_name(), self.get_duration(), self.instructor,self.cost,sep=" | ")
class computer_course_premium(computer_course_standart): #дочірній дочірного
    def __init__(self,course_name, duration, instructor,cost,flexible_schedule):
        super().__init__(course_name, duration,instructor,cost)
        self.flexible_schedule = flexible_schedule
    def my_course(self):
        print(self.get_course_name(), self.get_duration(), self.instructor,self.cost,self.flexible_schedule,sep=" | ")
def Print_your_coursr(course):
    course.my_course()
    

    
print("Виберіть курс\n1.Безплатний\n2.Звичайний\n3.Преміум\n4.Вихід\n")
course_choise = False
while course_choise != True:
    n = int(input())
    if n == 1:
        course = computer_course(input("Введіть назву курсу: "), input("Введіть складність курсу: "))
        break
    elif n == 2:
        course = computer_course_standart(input("Введіть назву курсу: "), input("Введіть складність курсу: "), input("Введіть ім'я інструктора курсу: "), input("Введіть ціну курсу: "))
        break
    elif n == 3:
        course = computer_course_premium(input("Введіть назву курсу: "), input("Введіть складність курсу: "), input("Введіть ім'я інструктора курсу: "), input("Введіть ціну курсу: "), input("Введіть графік курсу: "))
        break
    elif n == 4:
        break

while 1 != 0:
    print("\n\nДодаткові опції:\n1.Твій курс\n2.Список курсів")
    n = int(input())
    if n == 1:
        print(Print_your_coursr(course))
    elif n == 2:
        course.List_of_course_name()
    else:
        break
