class Data:

    # initialize the class instance (blueprint)
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __hash__(self):
        return hash((self.name, self.email, self.password)) # hash the object as a 'whole'
        # First, all the class attributes are inside a tuple (immutable) and then, that tuple is hashed


sensitive_info = Data("Oscar Diaz", "oscar@gmail.com", "password1234")

hashed_info = hash(sensitive_info)
print(hashed_info)