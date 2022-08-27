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
        query = cur.execute('SELECT is_done FROM todos WHERE id=?', (args.tick,))
        is_done = query.fetchone()
        print(is_done)
        if is_done is None:
            print('Task doesnt exist')
        elif is_done[0] == 1:
            print('switched to undone')
        elif is_done[0] == 0:
            print('switched to done')

    
    if args.list:
        for t_id, task, is_done in cur.execute('SELECT id, task, is_done FROM todos'):
            print(f'{t_id} \t {task} \t {is_done}')

   