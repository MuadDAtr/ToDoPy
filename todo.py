import argparse
import sqlite3


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--l', 
                        help = 'Showing pending tasks', 
                        action= 'store_true'
    )
    parser.add_argument('--a',
                        help = 'Add new task'
    )
    parser.add_argument('--t', 
                        help = 'Tick the task (changing status)'
    )
    parser.add_argument('--install',
                        help = 'Installation. Clearing database!',
                        action = 'store_true'
    )

    args = parser.parse_args()

    con = sqlite3.connect('todo.db')
    cur = con.cursor()

    if args.install is not None:
        print('Installing...')
        cur.execute('CREATE TABLE todos(id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, is_done BOOLEAN)')
        con.commit()
    if  args.a is not None:
        print('Adding...')

    if args.t is not None:
        print('Switching...')
    
    if args.l:
        print('Printing...')

   