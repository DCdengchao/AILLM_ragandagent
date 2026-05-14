
class Test(object):
    def __init__(self,name):
        self.name = name
    
    def __or__(self, other):
        return Mysequence(self,other)
    
    def __str__(self):
        return self.name
    
class Mysequence(object):
    def __init__(self,*args):
        self.sequence = []
        for arg in args:
            self.sequence.append(arg)
    
    def __or__(self, value):
        self.sequence.append(value)
        return self

    def run(self):
        for i in self.sequence:
            print(i)

if __name__ == "__main__":
    a = Test("a")
    b = Test("b")
    c = Test("c")
    d = Test("d")
    e = Test("e")
    f = Test("f")

    myseq = a | b | c | d | e | f
    myseq.run()
    print(type(myseq))