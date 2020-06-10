# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = ""
        self.s_to = ""
        self.e_to = ""
        self.w_to = ""

    def __str__(self):
        return f'Room "{self.name}" '

    def __repr__(self):
        return f'self.name = {self.name}; /n self.description = {self.description}; /n self.n_to = {self.n_to}; /n self.s_to = {self.s_to}; /n self.e_to = {self.e_to}; /n self.w_to = {self.w_to} '