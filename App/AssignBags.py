import pandas as pd
from Consts import DfViewSettings, RESOURCES, BAGS, BagsStringLength, DfConsts, UPDATED_ITEMS_FILE, PATH, BAGS_NAMES
from TestCases import TEST_NAMES, TEST_WEIGHTS, TEST_MAX_CARRIES
from Utils import create_team

DfViewSettings()


class AssignBags:
    df = pd.read_csv(f'{PATH}{RESOURCES}{UPDATED_ITEMS_FILE}')
    team = None
    bags = None
    categories = None
    if bags is None:
        bags = {}

    @classmethod
    def set_team(cls, names, weights, max_carries):
        cls.team = create_team(names=names, weights=weights, max_carries=max_carries, mefaked_name='gil')
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
    def divide_df_into_bags(cls, bags_names):
        """
        :param bags_names: list of the bags names to group by.
        :return: cls.bags: dictionary containing nested
        dictionary for every bag's assigned must items, to this dictionaries we'll add the rest of items.
        """
        # TODO: A for loop failed here for some reason.
        bags = cls.df.groupby(DfConsts.ASSIGNED_BAG)[[DfConsts.ITEM, DfConsts.WEIGHT]]
        planes_bag = bags.get_group(BAGS[BagsStringLength.PLANES_LEN])
        pods_bag = bags.get_group(BAGS[BagsStringLength.PODS_LEN])
        ground_sys_bag = bags.get_group(BAGS[BagsStringLength.GROUND_SYSTEM_LEN])
        mefaked_low = bags.get_group(BAGS[BagsStringLength.MEFAKED_LOW])
        low_bag = bags.get_group(BAGS[BagsStringLength.LOW_BAG])
        bags_df_list = [planes_bag, pods_bag, ground_sys_bag, mefaked_low, low_bag]
        bag = {bag: dict(sorted(item.values.tolist())) for bag, item in zip(bags_names, bags_df_list)}
        cls.bags = {bag_name: bag_items for bag_name, bag_items in bag.items()}
        return cls.bags

    @classmethod
    def assign_mefaked(cls):
        for person in cls.team:
            if person.mefaked:
                person.bag = cls.bags[BAGS[BagsStringLength.MEFAKED_LOW]]
                cls.bags.pop(BAGS[BagsStringLength.MEFAKED_LOW])

        return cls.bags, cls.team

    @classmethod
    def current_bag_weight(cls):
        for name in BAGS_NAMES:
            if name not in cls.bags.keys():
                BAGS_NAMES.remove(name)

        items_weights = list(map(lambda bag: cls.bags[bag].values(), BAGS_NAMES))
        bags_weight_sum_dict = {bag: sum(item) for bag, item in zip(cls.bags.keys(), items_weights)}
        return bags_weight_sum_dict

    @classmethod
    def assign_bags_to_team(cls):
        """
        Just check those against each other, and if bag matches the max available weight assign them together and
        keep assigning items.
        """

        team_max_weights = sorted([person.max_allowed for person in cls.team])
        index = 0

        # Assign Mefaked Bag
        cls.assign_mefaked()

