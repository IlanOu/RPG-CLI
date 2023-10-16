import os

'''We define our own clean function to clear the screen'''
def clean():
    
    # For macOS and Linux
    if os.name == 'posix':
        os.system('clear')

    # Windows
    elif os.name == 'nt':
        os.system('cls')