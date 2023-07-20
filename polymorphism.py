class Base:
    def intro(self):
        print("Exam")
    def func(self):
        print("Base Class")
class child1(Base):
    def func(self):
        print("Child 1")
class child2(Base):
    def func(self):
        print("Child 2")
obj_Base=Base()
obj_c1=child1()
obj_c2=child2()

obj_Base.intro()
obj_Base.func()

obj_c1.intro()
obj_c2.func()

obj_c1.intro()
obj_c2.func()
