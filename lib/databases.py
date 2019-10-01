# -*- coding: utf-8 -*-

from peewee import *

# database = MySQLDatabase('MYX', **{'charset': 'utf8', 'use_unicode': True, 'host': 'localhost',
# 'user': 'MYX', 'password': '123456'})

database = SqliteDatabase('database.db')


class KeyWords(Model):
    id = IntegerField(primary_key=True)
    words = CharField(max_length=255, unique=True)

    class Meta:
        table_name = 'keywords'
        database = database
