class Person:
    def __init__(self, max_allowed, weight, mefaked=None):
        self.max_allowed = max_allowed
        self.weight = weight
        self.mefaked = mefaked

    def get_max_allowed(self):
        return self.max_allowed

    def get_weight(self):
        return self.weight
