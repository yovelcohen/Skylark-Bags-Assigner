from BagsFormatter.Base.BaseClasses import Person

test_team = {1: Person(max_allowed=50, weight=74),
             2: Person(max_allowed=50, weight=83),
             3: Person(max_allowed=50, weight=73),
             4: Person(max_allowed=50, weight=77),
             5: Person(max_allowed=50, weight=74, mefaked=True)
             }
