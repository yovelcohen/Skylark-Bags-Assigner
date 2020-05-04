from pandas import read_csv

# Base DataFrame containing all items.
ITEMS_DF = read_csv("/home/yovel/PycharmProjects/BagsFormatter/Resources/Items.csv",
                    dtype={'Item': 'str',
                           'Weight': 'float',
                           'Bags': 'str',
                           'quantity': 'int',
                           'must quantity': 'int'
                           },
                    )


class BagsStringLength:
    """
    Lens of all bags strings.
    And dictionary that contains string representing those lens.
    """

    PLANES_LEN = 6
    PODS_LEN = 4
    GROUND_SYSTEM_LEN = 13
    LOW_BAG = 7
    MEFAKED_LOW = 14

    lens_list = [PLANES_LEN, PODS_LEN, GROUND_SYSTEM_LEN, LOW_BAG, MEFAKED_LOW]


BAGS = {
    BagsStringLength.PLANES_LEN: 'planes bag',
    BagsStringLength.PODS_LEN: 'pods bag',
    BagsStringLength.GROUND_SYSTEM_LEN: 'ground system bag',
    BagsStringLength.LOW_BAG: 'low bag',
    BagsStringLength.MEFAKED_LOW: 'mefaked low'
}

BAGS_NAMES = list(BAGS.values())

# Base Index
INDEX = 0

# Home Directory
PATH = '/home/yovel/PycharmProjects/BagsFormatter/'

# resources folder
RESOURCES = 'Resources/'
UPDATED_ITEMS_FILE = 'Updated_items.csv'


# The items df consts.
class DfConsts:
    BAGS = 'Bags'
    BAGS_COLUMN_LENGTH = 'bags column length'
    ASSIGNED_BAG = 'assigned_bag'
    MUST = 'Must'
    MUST_QUANTITY = 'must quantity'
    QUANTITY = 'quantity'
    ITEM = 'Item'
    V = 'v'
    WEIGHT = 'Weight'
    CATEGORY = 'category'


# for defining of types in df.
class TypesConsts:
    STR = 'string'
    FLOAT = 'float'
    INT = 'int'
