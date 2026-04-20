from tkinter.scrolledtext import example

phonebook=[
    ('alex','+48005492211'),
    ('Alice','+48005492212'),
    ('Ser','+48005492213'),
    ('mob','+48005492214'),
]

def find(input_name:str) -> str | None:
    for name, phone in phonebook:
        if name==input_name:
            return phone
    return None


def primitive_hash(text:str) -> int:
    total=0
    for char in text:
        total+=ord(char)
    return total

print(primitive_hash('alex'))
print(primitive_hash('Vlad'))
print('*'*100)

def less_primitive_hash(text:str) -> int:
    total=0
    for char in text:
        total+=ord(char)+total*31
    return total

print(less_primitive_hash('Vlad'))
print(less_primitive_hash('dalV'))
print('*'*100)

print(hash('Vlad'))
print(hash(42))
print(hash(3.14))
print(hash(None))
print(hash(True))
print(hash((1,2,3)))

import hashlib

email= 'example@email.com'
password = 'qwerty'
secret_key= 'vary-secret-key'

print('*'*100)

pass_hash = hashlib.md5(password.encode()).hexdigest()
password_hash = hashlib.sha256((password + secret_key).encode()).hexdigest()
print(pass_hash)
print(password_hash)
print(password_hash==pass_hash)
# print('*'*100)

class HashTable:
    def __init__(self,size: int=8,):
        self.size=size
        self.buckets : list=[[] for _ in range(self.size)]

    def _index(self,key: str) -> int:
        return hash(key) % self.size


    def put(self,key:str,value:int) -> None:
        index=self._index(key)
        bucket=self.buckets[index]
        for i,(k, _) in enumerate(bucket):
            if k ==key:
                bucket[i]=(key,value)
                return

        # bucket[i]=(key,value)

    def get(self,key:str,default= None) -> int | None:
        for k,value in self.buckets[self._index(key)]:
            if k==key:
                return value
        return default

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} {self.buckets}'

hash_table = HashTable()
hash_table.put('Alex','+123456781')
hash_table.put('Bob','+123456782')
hash_table.put('Aloha','+123456783')
hash_table.put('Alice','+123456784')



# 3*(x+y)

#           *
#          / \
#         3   +
#            / \
#           x   y

class Expression:
    pass

class Constant(Expression):
    def __init__(self,value):
        self.value = value

    def eval(self,env):
        return self.value

    def __repr__(self):
        return f'{self.__class__.__name__} {self.value}'

class Variable(Expression):
    def __init__(self,name):
        self.name = name

    def eval(self,env):
        return env[self.name]

    def __repr__(self):
        return f'{self.__class__.__name__} {self.name}'

class Plus(Expression):
    def __init__(self,left,right):
        self.left = left
        self.right = right

    def eval(self,env):
        return self.left.eval(env) + self.right.eval(env)

    def __repr__(self):
        return f'{self.__class__.__name__} {self.left} {self.right}'

class Multiply(Expression):
    def __init__(self,left,right):
        self.left = left
        self.right = right

    def eval(self,env):
        return self.left.eval(env) * self.right.eval(env)

    def __repr__(self):
        return f'{self.__class__.__name__} {self.left} {self.right}'


variables= {'x':5,'y':3}

# 3*(x+y)
expression_1= Multiply(Constant(3), Plus(Variable('x'),Variable('y')))
print(expression_1)
print(expression_1.eval(variables))
print('*'*100)
# 3*x+y
expression_2= Multiply(Constant(3), (Variable('x'),Variable('y')))
print(expression_2)
print(expression_2.eval(variables))