from App.TestCases import TEST_NAMES, TEST_WEIGHTS, TEST_MAX_CARRIES


class Person:
    def __init__(self, name, max_allowed, mefaked=None):
        self.name = name
        self.max_allowed = max_allowed
        self.mefaked = mefaked

    def get_max_allowed(self):
        return self.max_allowed

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


class Team:
    team = None
    if team is None:
        team = []

    @classmethod
    def sort_people_data(cls, names, weights, max_carries):
        weight_data = list(zip(weights, max_carries))
        max_allowed = [Person.get_max_carry_in_kg(max_allowed=max_allowed, weight=weight) for max_allowed, weight in
                       weight_data]
        for name, max_allowed in zip(names, max_allowed):
            person = Person(name=name, max_allowed=max_allowed)
            cls.team.append(person)
            return cls.team


if __name__ == '__main__':
    Team.sort_people_data(names=TEST_NAMES, weights=TEST_WEIGHTS, max_carries=TEST_MAX_CARRIES)
