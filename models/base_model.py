from peewee import *
from settings import DATABASE_CONFIG2

mysql = MySQLDatabase('library', **DATABASE_CONFIG2)

class BaseModel(Model): # z bibliotekii peevee
    class Meta:
        database = mysql
        legacy_table_names = False