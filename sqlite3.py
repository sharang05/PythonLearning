import sqlite3

def insert(db, row):
	db.execute('insert into test (t1, i1) values (?, ?)', (row['t1'], row['i1']))
	db.commit()

def retrieve(db, t1):
	cursor= db.execute('select * from test where t1 = ?',(t1,))
	return cursor.fetchone()

def update(db, row):
	db.execute('update test set i1 = ? where t1 = ?',(row['i1'], row['t1']))
	db.commit()

def delete(db, t1):
	db.execute('delete from test where t1 = ?', (t1,))
	db.commit()


def disp_row(db):
	cursor = db.execute('select * from test order by t1')
	for row in cursor:
		print(dict(row))

def main():
	db = sqlite3.connect('test.db')
	db.row_factory = sqlite3.Row
	db.execute('drop table if exists test')
	db.execute('create table test (t1 text, i1 int)')

	print('Insert rows')
	insert(db, dict(t1 ='one', i1 = 1))
	insert(db, dict(t1 ='two', i1 =2))
	insert(db, dict(t1 = 'three', i1 =3))
	insert(db, dict(t1 = 'four', i1 =4))
	disp_row(db)

	print('retrive row')
	print(dict(retrieve(db, 'one')), dict(retrieve(db, 'two')))

	print('Update table')
	update(db, dict(t1 ='one', i1 = 100))
	disp_row(db)

	print ('delete row')
	delete(db, 'one')
	delete(db, 'four')
	disp_row(db)


if __name__ == "__main__": main()