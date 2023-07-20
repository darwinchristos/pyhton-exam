class mother:
    mothername=""
    def mother(self):
        print(self.mothername)

class father:
    fathername=""
    def father(self):
        print(self.fathername)

class son(mother,father):
    def parents(self):
        print("Father :",self.fathername)
        print("mother :",self.mothername)
s1=son()
s1.fathername="ROMEO"
s1.mothername="JULIET"
s1.parents()
