import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', 
                        help = 'Showing tasks to do', 
                        action= 'store_true'
    )
    parser.add_argument('-a',
                        help = 'Add new task'
    )

    args = parser.parse_args()

    print('Add mode is %r.' % args.a)

