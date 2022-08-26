import argparse
import sqlite3


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--list', 
                        help = 'Showing pending tasks', 
                        action= 'store_true'
    )
    parser.add_argument('--add',
                        help = 'Add new task'
    )
    parser.add_argument('--tick', 
                        help = 'Tick the task (changing status)'
    )
    parser.add_argument('--install',
                        help = 'Installation. Clearing database!',
                        action = 'store_true'
    )

    args = parser.parse_args()

    con = sqlite3.connect('todo.db')
    cur = con.cursor()

    if args.install:
        print('Installing...')
        cur.execute('DROP TABLE todos')
        cur.execute('CREATE TABLE todos(id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, is_done BOOLEAN)')
        con.commit()
    if  args.add is not None:
        print('Adding...')
        task = args.add
        cur.execute('INSERT INTO todos(task, is_done) VALUES(?, false)', (task,))
        con.commit()

    if args.tick is not None:
        print('Switching...')
    
    if args.list:
        print('Printing...')

   