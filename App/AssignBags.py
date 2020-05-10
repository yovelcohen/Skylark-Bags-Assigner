import pandas as pd

from App.Consts import RESOURCES, BAGS, BagsStringLength, DfConsts, UPDATED_ITEMS_FILE, PATH, BAGS_NAMES
from App.TestCases import TEST_NAMES, TEST_WEIGHTS, TEST_MAX_CARRIES
from App.Utils import create_team, sort_ordered_dict

pd.set_option("max_columns", 15)
pd.set_option("max_rows", 1000)


class AssignBags:
    df = pd.read_csv(f'{PATH}{RESOURCES}{UPDATED_ITEMS_FILE}')
    team = None
    bags = None
    categories = None
    if bags is None:
        bags = {}

    @classmethod
    def set_team(cls):
        cls.team = create_team(names=TEST_NAMES, weights=TEST_WEIGHTS, max_carries=TEST_MAX_CARRIES)
        return cls.team

    @classmethod
    def divide_df_to_categories(cls):
        """
        :returns cls.categories: the DataFrame showing the item's name weight and if it's a must divided into
        categories.
        """
        cls.categories = cls.df.groupby(DfConsts.CATEGORY)[[DfConsts.ITEM, DfConsts.WEIGHT, DfConsts.MUST]]
        return cls.categories

    @classmethod
    def assign_items_to_bags(cls):
        for item in BAGS_NAMES:
            mask = cls.df[DfConsts.BAGS].str.contains(item)
            cls.df.loc[mask, DfConsts.ASSIGNED_BAG] = item

    @classmethod
    def divide_df_into_bags(cls, bags_names) -> dict:
        """
        :param bags_names: list of the bags names to group by.
        :return: cls.bags: dictionary containing nested
        dictionary for every bag's assigned must items, to this dictionaries we'll add the rest of items.
        """

        bags = cls.df.groupby(DfConsts.ASSIGNED_BAG)[[DfConsts.ITEM, DfConsts.WEIGHT]]
        planes_bag = bags.get_group(BAGS[BagsStringLength.PLANES_LEN])
        pods_bag = bags.get_group(BAGS[BagsStringLength.PODS_LEN])
        ground_sys_bag = bags.get_group(BAGS[BagsStringLength.GROUND_SYSTEM_LEN])
        low_bag = bags.get_group(BAGS[BagsStringLength.LOW_BAG])
        mefaked_low = bags.get_group(BAGS[BagsStringLength.MEFAKED_LOW])
        bags_df_list = [planes_bag, pods_bag, ground_sys_bag, low_bag, mefaked_low]
        cls.bags = sort_ordered_dict(
            {bag: dict(sorted(item.values.tolist())) for bag, item in zip(bags_names, bags_df_list)})
        return cls.bags

    @classmethod
    def check_bag_weight(cls):
        """
        Just check those against each other, and if bag matches the max available weight assign them together and
        keep assigning items.
        """
        team_max_weights = sorted([person.max_allowed for person in cls.team])
        for weight in team_max_weights:
            raise NotImplementedError

    def run(cls):
        pass


if __name__ == '__main__':
    AssignBags.set_team()
    AssignBags.divide_df_into_bags(bags_names=BAGS.values())
    AssignBags.assign_items_to_bags()
