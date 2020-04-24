# import pandas as pd
#
# from BagsFormatter.Consts import PATH, RESOURCES
# from BagsFormatter.Utils import get_max_carry_in_kg
#
# team = {
#     'yovel': get_max_carry_in_kg(warrior_weight=83, max_percentage_allowed=50),
#     'ido': get_max_carry_in_kg(warrior_weight=73, max_percentage_allowed=50),
#     'eyal': get_max_carry_in_kg(warrior_weight=77, max_percentage_allowed=50),
#     'peleg': get_max_carry_in_kg(warrior_weight=74, max_percentage_allowed=50),
#     'mefaked': get_max_carry_in_kg(warrior_weight=73, max_percentage_allowed=50)
# }
#
# df = pd.read_csv(f'{PATH}{RESOURCES}Updated_items.csv')
# team = {k: v for k, v in sorted(team.items(), key=lambda item: item[1])}
#
# to_match_str = 'planes bag'
# planes = df[df['assigned_bag'].str.match(to_match_str)]
# print(planes)


class F(str):
