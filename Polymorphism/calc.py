class calculator{
    int add(int a, int b)
    int add(int a, int b, int c)
}

class calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
    
class calculator:
    def add(self, args):
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
        
class calculator:
    def add(self, a, b):
            return a + b
        elif isinstance(a, int) and isinstance(b, int):
            return float(a)+float(b)
        elif isinstance(a, float) and isinstance(b, float):
            return str(a) + str(b)
        

