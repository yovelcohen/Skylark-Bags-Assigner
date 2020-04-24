import pandas as pd

from BagsFormatter.Consts import ITEMS_DF, BAGS_LENS, RESOURCES, PATH, PandasConsts, UPDATED_ITEMS_FILE

pd.set_option("max_columns", 15)
pd.set_option("max_rows", 1000)


class SortAndAssignMustItems:
    _bags: dict = BAGS_LENS
    df = ITEMS_DF

    @classmethod
    def create_bag_df(cls):
        """
        Add len of string in Bags column to a column named beg_len.
        """
        cls.df[PandasConsts.BAGS_COLUMN_LENGTH] = cls.df[PandasConsts.BAGS].map(len)
        cls.df[PandasConsts.ASSIGNED_BAG] = None
        return cls.df

    @classmethod
    def assign_must_items(cls):
        """
        Assign The items that are marked as must to their respective bags.
        :returns pandas.DataFrame
        """
        cls.df.fillna({PandasConsts.MUST: 0}, inplace=True)
        cls.df[PandasConsts.ASSIGNED_BAG] = cls.df.loc[
            cls.df[PandasConsts.MUST] != '0'][
            PandasConsts.BAGS_COLUMN_LENGTH].map(cls._bags)
        cls.df.fillna({PandasConsts.ASSIGNED_BAG: 0}, inplace=True)
        return cls.df

    @classmethod
    def duplicate_rows(cls):
        """
        This method multiplies every row in the data frame if that row's quantity > 1 until that row's count is 1.
        :returns an updated csv file.
        """
        cls.df = cls.df.loc[cls.df.index.repeat(cls.df.quantity)].assign(quantity=1).reset_index(drop=True)
        cls.df.to_csv(f'{PATH}{RESOURCES}{UPDATED_ITEMS_FILE}')
        print(cls.df)
        return cls.df


if __name__ == '__main__':
    SortAndAssignMustItems.create_bag_df()
    SortAndAssignMustItems.assign_must_items()
    SortAndAssignMustItems.duplicate_rows()
    pass
