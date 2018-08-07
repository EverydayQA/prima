

class Child:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __check(self):
        if self.age > 10:
            "insert into db both age and name"
        else:
            print(self.age)

    def call(self, flag):
        if flag:
            self.__check()
