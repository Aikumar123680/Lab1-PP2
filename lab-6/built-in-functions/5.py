from functools import reduce

def all_true(tpl):
    return all(tpl)

print("All elements True:", all_true((True, True, False)))
