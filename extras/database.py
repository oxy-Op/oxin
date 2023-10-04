import sqlite3
from .directory import Path
from datetime import datetime

date = datetime.utcnow()
now = date.strftime('%H:%M:%S')

print("[{}] Loading database...".format(now))
db = sqlite3.connect(Path.DataBasePath())
print("[{}] Connected to database".format(now))
cursor = db.cursor()
print('[{}] Connected with cursor'.format(now))


def execute(command:str):
    return db.execute(str(command))    

async def commit():
    return await db.commit()

def save():
    return db.commit()

def close():
    return db.close()

def items(command):
    for item in str(command):
        return item



