class SingletonMeta(type):
    # Dictionary to keep track of the single instance for each class
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # If an instance doesn't exist yet, create it and save it
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        # Return the existing instance
        return cls._instances[cls]

# Usage
class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        print("Initializing connection...")

# Verification
db1 = DatabaseConnection()  # Prints: Initializing connection...
db2 = DatabaseConnection()  # Prints nothing

print(db1 is db2)  # Output: True
