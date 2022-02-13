import os, sys, datetime

def get_time():
    parser = datetime.datetime.now()
    extension = ".txt"
    current_diary_time = parser.strftime("%d.%m.%Y") + extension
    return current_diary_time

call = get_time()

try:
    for line in sys.stdin:
        sys.stdout = open(call, "a")
        print(line.rstrip())
except KeyboardInterrupt:
    sys.stdout = sys.stderr
    print("Bye")