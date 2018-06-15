import sqlite3

def main():
    db= sqlite3.connect('testdb')
    db.row_factory = sqlite3.Row
    db.execute('drop table if exists test')
    db.execute('create table test(name text, age int)')
    db.execute('insert into test(name, age) values (?, ?)', ('sharang', 25))
    db.execute('insert into test(name, age) values (?, ?)', ('vibhor', 26))
    db.execute('insert into test(name, age) values (?, ?)', ('Devan', 1))
    db.execute('insert into test(name, age) values (?, ?)', ('Amol', 65))
    db.commit()
    cursor = db.execute('select * from test')
    for row in cursor:
        print (dict(row))


if __name__ == "__main__": main()