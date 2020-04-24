from pandas import read_csv

PLANES_LEN = 6
PODS_LEN = 4
GROUND_SYSTEM_LEN = 13
LOW_BAG = 7
MEFAKED_LOW = 14
# Base DataFrame containing all items.
ITEMS_DF = read_csv("/home/yovel/PycharmProjects/BagsFormatter/Resources/Items.csv",
                    dtype={'Item': 'str',
                           'Weight': 'float',
                           'Bags': 'str',
                           'quantity': 'int',
                           'must quantity': 'int'
                           },
                    )

BAGS_LENS = {
    PLANES_LEN: 'planes bag',
    PODS_LEN: 'pods bag',
    GROUND_SYSTEM_LEN: 'ground system bag',
    LOW_BAG: 'low bag',
    MEFAKED_LOW: 'mefaked low'
}

INDEX = 0

PATH = '/home/yovel/PycharmProjects/BagsFormatter/'

RESOURCES = 'Resources/'
UPDATED_ITEMS_FILE = 'Updated_items.csv'


class PandasConsts:
    BAGS = 'Bags'
    BAGS_COLUMN_LENGTH = 'bags column length'
    ASSIGNED_BAG = 'assigned_bag'
    MUST = 'Must'
    MUST_QUANTITY = 'must quantity'
    QUANTITY = 'quantity'
    ITEM = 'Item'


class TypesConsts:
    STRING = 'string'
    FLOAT = 'float'
    INT = 'int'
