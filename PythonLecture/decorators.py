def announce(f):
    def wrapper():
        print("About t0 run the function...")
        f()
        print("Done with the function.")
    return wrapper    

@announce
def hello():
    print("Hello, World!")

hello()