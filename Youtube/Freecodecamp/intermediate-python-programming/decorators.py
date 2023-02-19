def start_end_docorator(func):
    
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

@start_end_docorator #print_name is passed as a parameter to start_end_function
def print_name():
    print("Harsh")

print_name()