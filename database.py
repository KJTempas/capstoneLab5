from peewee import *
import sqlite3

db = SqliteDatabase('chainsaw.sqlite')

    #model class defines fields in object which map to dbase
class ChainsawJuggling(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

    #link model to dbase
    class Meta:
        database = db

    #to string method
    def __str__(self):
    
        return f'Name: {self.name}, Country: {self.country}, Number of catches: {self.catches}.'


db.connect()
db.create_tables([ChainsawJuggling])

Janne = ChainsawJuggling(name="Janne Mustonen", country = "Finland", catches = 98)
Janne.save()
Ian = ChainsawJuggling(name="Ian Stewart", country="Canada", catches = 94)
Ian.save()
Aaron = ChainsawJuggling(name="Aaron Gregg", country="Canada", catches = 88)
Aaron.save()
Chad = ChainsawJuggling(name="Chad Taylor", country="USA", catches = 78)
Chad.save()


#def search_by_name():
name = input("Enter name of person to search:  ")
result = ChainsawJuggling.select().where(ChainsawJuggling.name == name).limit(1)
#print(result.country, result.catches)
for r in result:
    print(str(r))
    
    
#def update_catches(name):
name = input("Enter the name of the person whose record you want to update: ")
catches = int(input(f'Enter new catch record for {name}: '))
rows_updated = ChainsawJuggling.update(catches = catches).where (ChainsawJuggling.name == name).execute()
if rows_updated:
    print(f'Successfully updated catches for {name}:  ')
else:
    raise ChainError("Problem updating record")


#def delete_record_by_user_name():
name = input("Enter the name of the juggler to delete:  ")
name= name.title()
rows_deleted = ChainsawJuggling.delete().where(ChainsawJuggling.name == name).execute()
if rows_deleted:
    print(f'Record for {name} was deleted')
else:
    raise ChainError("That juggler not on file")

#def add_user():
name = input("Enter the name of the juggler:  ")
name = name.title()
country = input(f'Enter the country where {name} lives:  ')
country = country.title()
catches = int(input(f'Enter the number of catches for {name}: '))
rows_added = ChainsawJuggling.insert(name = 'name', country = 'country', catches = catches).execute()
if rows_added:
    print('Added user')
else:
    raise ChainError('Problem adding  new user')



def ChainError(Exception):
    pass
    


