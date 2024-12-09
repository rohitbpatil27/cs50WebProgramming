def announce(f):
    def wrapper():
        print("Start the function...")
        f()
        print("End the function....")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()