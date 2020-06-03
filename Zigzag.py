import time, sys
indent = 0                  # How many spaces to indent
indentIncreasing = True     # Whether the indentation is increasing or not

try:
    while True:                          # The main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)                  # Pause for 1/10 of a second
        if indentIncreasing:
            indent += 1                  # Increase the number of spaces
            if indent == 20:
                indentIncreasing = False # Change direction
        else:
            indent -= 1                  # Decrease number of spaces
            if indent == 0:
                indentIncreasing = True  # Change direction
except KeyboardInterrupt:
    sys.exit()
