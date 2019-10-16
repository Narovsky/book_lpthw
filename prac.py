class A(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class B(A):
    def __new__(cls, *args, **kwargs):
        super().__new__(cls, *args, **kwargs)

a = A('P', 'C')
b = B('abs', 'cas')
print(b)
print(a)
