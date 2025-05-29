class Data:

    # initialize the class instance (blueprint)
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __hash__(self):
        return hash((self.name, self.email, self.password)) # hash the