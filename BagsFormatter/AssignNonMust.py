import pandas as pd

from BagsFormatter.Consts import PATH, RESOURCES, UPDATED_ITEMS_FILE, PandasConsts, TypesConsts
from BagsFormatter.TestCases import test_team


class AssignNonMust:

    def __init__(self, team):
        self.team = team
        self.df = self.set_df()

    def set_df(self):
        self.df = pd.read_csv(f"{PATH}{RESOURCES}{UPDATED_ITEMS_FILE}",
                              dtype={PandasConsts.ITEM: TypesConsts.STRING,
                                     'Weight': TypesConsts.FLOAT,
                                     'Bags': TypesConsts.STRING,
                                     PandasConsts.QUANTITY: TypesConsts.INT,
                                     PandasConsts.MUST_QUANTITY: TypesConsts.INT
                                     },
                              )
        return self.df

    @classmethod
    def assign_bag_to_person(cls, team):
        """
        this method receives names and weights of all the people in the team.
        it return a dictionary where the team members are sorted with how much they can carry.
        """


if __name__ == '__main__':
    AssignNonMust.assign_bag_to_person(team=test_team)
