from collections import OrderedDict

from App.Person import Person


def create_team(names, weights, max_carries):
    """
    Craete a list of Person object for every team member.
    """
    weight_data = list(zip(weights, max_carries))
    max_allowed = [Person.get_max_carry_in_kg(max_allowed=max_allowed, weight=weight) for max_allowed, weight in
                   weight_data]
    people = list(zip(names, max_allowed))
    team = [Person(name=name, max_allowed=max_allowed) for name, max_allowed in people]
    return team


def sort_ordered_dict(dictionary):
    """
    Takes in a regular dictionary containing nested dictionaries and returns it sorted by the nested dicts values sum.
    :return sorted_dict = collections.OrderedDict:
    """
    sorted_dict = OrderedDict(
        sorted([[k, v] for (k, v) in dictionary.items()], key=lambda kv: sum(kv[1].values()), reverse=True)
    )
    return sorted_dict
