import pandas as pd

from Consts import ITEMS_DF, RESOURCES, PATH, DfConsts, UPDATED_ITEMS_FILE, BagsStringLength

pd.set_option("max_columns", 15)
pd.set_option("max_rows", 1000)


class SortAndAssignMustItems:
    _bags: dict = BagsStringLength.BAGS_LENS
    df = ITEMS_DF

    @classmethod
    def add_columns(cls):
        """
        Add len of string in Bags column to a column named beg_len.
        """
        cls.df[DfConsts.BAGS_COLUMN_LENGTH] = cls.df[DfConsts.BAGS].map(len)
        cls.df[DfConsts.ASSIGNED_BAG] = None
        return cls.df

    @classmethod
    def fill_must_with_bool(cls):
        """
        Replace v in the Must column to True and 0 to False.
        """
        cls.df.fillna({DfConsts.MUST: False}, inplace=True)
        cls.df[DfConsts.MUST].loc[(cls.df[DfConsts.MUST] == DfConsts.V)] = True
        return cls.df

    @classmethod
    def duplicate_rows(cls):
        """
        This method multiplies every row in the data frame if that row's quantity > 1 until that row's count is 1.
        :returns an updated csv file.
        """
        cls.df = cls.df.loc[cls.df.index.repeat(cls.df.quantity)].assign(quantity=1).reset_index(drop=True)
        return cls.df

    @classmethod
    def assign_must_items(cls):
        """
        Assign The items that are marked as must to their respective bags.
        The Reason for this method being here and not and in assign items class, is that we want to do a little sanity
        check before assigning rest of the items that the team can carry the bags at their base weight.
        :returns pandas.DataFrame
        """
        cls.df[DfConsts.ASSIGNED_BAG] = cls.df.loc[
            cls.df[DfConsts.MUST] == True][
            DfConsts.BAGS_COLUMN_LENGTH].map(cls._bags)
        return cls.df

    @classmethod
    def export_to_csv(cls):
        cls.df.to_csv(f'{PATH}{RESOURCES}{UPDATED_ITEMS_FILE}')

    @classmethod
    def run(cls):
        cls.add_columns()
        cls.fill_must_with_bool()
        cls.duplicate_rows()
        cls.assign_must_items()
        cls.export_to_csv()


if __name__ == '__main__':
    SortAndAssignMustItems.run()
