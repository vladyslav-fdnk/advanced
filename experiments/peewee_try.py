from datetime import date
from peewee import *


db = SqliteDatabase('pet_owners.db')

class BaseModel(Model):
    """All models inherit this to share the database connection."""
    class Meta:
        database = db

class Person(BaseModel):
    name = CharField(max_length=100)
    birthday = DateField()

    class Meta:
        database = db

    def __str__(self):
        return f'Person- {self.name} BDay- {self.birthday}'


class Pet(BaseModel):
    owner = ForeignKeyField(Person, backref='pets')
    nickname = CharField(max_length=100)
    animal_type = CharField(max_length=100)

    def __str__(self):
        return f'Pet- {self.nickname} Animal Type- {self.animal_type}'

if __name__ == '__main__':
    db.connect()
    db.create_tables([Person, Pet])

    bob = Person(name='Bob', birthday=date(1999, 1, 1))
    print(bob)
    print(bob.name)
    print(bob.birthday)

    # bob.save()
    # Person.create(name='Anton', birthday=date(2000, 11, 23))
    # Person.create(name='Petro', birthday=date(2010, 12, 12))
    # Person.create(name='Emil', birthday=date(1990, 9, 2))

    # anton= Person.get(Person.name=='Anton')
    # bob = Person.get(Person.name == 'Bob')
    #
    # bobik=Pet.create(owner_id=anton.id, nickname='Bobik', animal_type='Dog')
    # kitty = Pet.create(owner=bob,nickname='Kitty',animal_type='Cat')


