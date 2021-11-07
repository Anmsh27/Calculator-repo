import os

# exception handler for ModuleNotFound exception
def no_module_error():
    os.system('pip install pygame')

# Runs pip install pygame command in terminal
