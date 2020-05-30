class Person:
    def __init__(self, name, max_allowed, mefaked=False):
        self.name = name
        self._max_allowed = max_allowed
        self._mefaked = mefaked

    bag = None

    @property
    def max_allowed(self):
        return self._max_allowed

    @max_allowed.setter
    def max_allowed(self, value):
        self._max_allowed = value

    @property
    def mefaked(self):
        return self._mefaked

    @mefaked.setter
    def mefaked(self, value):
        self._mefaked = value

    @staticmethod
    def get_max_carry_in_kg(max_allowed, weight):
        """
        This function receives the percentage of body weight warrior is allowed to carry and is body weight
        and returns the maximum weight he can carry.
        """
        max_weight_allowed = (max_allowed * weight) / 100.0
        return max_weight_allowed

    def check_against_max_carry(self):
        """
        Check that with every added item to what this person carries he's not passing his max allowed.
        """
