class exam :
    def __init__(self,name):
        self.name=name
        print("Constructor")
    def func1(self):
        print("Exam!!",self.name)
pro=exam('python')
pro.func1()
