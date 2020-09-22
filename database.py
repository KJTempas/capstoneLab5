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
    def__str__(self):
        return 'Name: {self.name}, Country: {self.country}, Number of catches: {catches}.'


db.connect()
db.create_tables([ChainsawJuggling])

Janne = ChainsawJuggling(name="Janne Mustonen", country = "Finland", catches = 98)
Janne.save()
Ian = ChainsawJuggling(name="Ian Steward", country="Canada", catches = 94)
Ian.save()
Aaron = ChainsawJuggling(name="Aaron Gregg", country="Canada", catches = 88)
Aaron.save()
Chad = ChainsawJuggling(name="Chad Taylor", country="USA", catches = 78)
Char.save()


def add_user():
    name = input("Enter the name of the juggler")
    name = name.title()
    country = input("Enter the country where {name} lives")
    country = country.title()
    catches = int(input("Enter the number of catches for {name}"))


def search_by_name():
    name = input("Enter name of person to search")
   results = ChainsawJuggling.select().where(ChainsawJuggling.name ==)
    for r in results:
        print(r)
    
def update_catches(name):
    name = input("Enter the name of the person whose record you want to update")
    catches = int(input("Enter new catch record for {name}"))
    rows_updated = ChainsawJuggling.update(catches = catches).where (ChainsawJuggling.name == name).execute()
    if rows_updated:
        print("Successfully updated catches for {name}")
    else:



def delete_record_by_user_name()
    name = input("Enter the name of the juggler to delete")
    name= name.title()
    rows_deleted = ChainsawJuggling.delete().where(ChainsawJuggling.name == 'name').execute()
    if rows_deleted:
        print("Record for {name} was deleted")
    else:
        raise ChainError('That juggler not on file')



def ChainError:
    pass
    
