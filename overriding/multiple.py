class class1:
    def w(self):
        print("class1 method")

class class2(class1):
    def w(self):
        print("class2 method")

class class3(class1):
    def w(self):
        print("class3 method")

class class4(class2, class3):
    pass

obj = class4()
obj.w()