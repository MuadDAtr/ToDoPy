import argparse
import sqlite


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
    parser.add_argument('--i',
                        help = 'installation'
    )

    args = parser.parse_args()

   
    if  args.a is not None:
        print('Adding...')

    if args.t is not None:
        print('Switching...')
    
    if args.l is not None:
        print('Printing...')