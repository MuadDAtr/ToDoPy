import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-q', '--quiet',
action ='store_true',
dest = 'quiet',
help = 'Suppress Output'
)

args = parser.parse_args()

print('Quiet mode is %r.' % args.quiet)