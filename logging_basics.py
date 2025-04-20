import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO)

# Create a logger
log = logging.getLogger(__name__)

def greet(name):
    log.info(f"Greeting user: {name}")
    return f"Hello, {name}!"

def main():
    user = "Alice"
    greeting = greet(user)
    print(greeting)

if __name__ == "__main__":
    main()
