import discord
import sqlite3


def eventopt(guild):
    connection = sqlite3.connect('data/db.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM eventopt WHERE id = {guild.id}")
    result = cursor.fetchone()

    return result

def options(guild):
    connection = sqlite3.connect('data/db.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM options WHERE id = {guild.id}")
    result = cursor.fetchone()

    return result

def user(user):
    connection = sqlite3.connect('data/db.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user.id}")
    result = cursor.fetchone()

    return result    

def apl(user):
    connection = sqlite3.connect('data/db.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM apl WHERE id = {user.id}")
    result = cursor.fetchone()

    return result    

def event(user):
    connection = sqlite3.connect('data/db.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM event WHERE id = {user.id}")
    result = cursor.fetchone()

    return result

def blacklist(user):
    connection = sqlite3.connect('data/db.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM blacklist WHERE id = {user.id}")
    result = cursor.fetchone()

    return result

def send(result):
    connection = sqlite3.connect('data/db.db')
    cursor = connection.cursor()
    print(result)
    cursor.execute(result)
    connection.commit()