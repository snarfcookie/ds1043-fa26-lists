"""lists

Exercises for exploring lists
"""

from pathlib import Path


def clamp(a: list[int], low: int = 0, high: int = 10) -> None:
    """Modify the values of a to be `low` when they fall below `low` or `high` when the fall above `high`"""
    for index,element in enumerate(a):
        if a[index] < 0:
            a[index] = 'low'
        elif a[index] > 10:
            a[index] = 'high'
    return a


# Try writing your own reverse function by actually moving values around rather than
# using reversed, list.reverse, a[::-1], etc
def reverse(a: list) -> None:
    reversed = []
    for index in range(len(a) - 1, -1, -1):
        reversed.append(a[index])
    return reversed


# Read the following function and write out your prediction of what it will do
# in the following situations:
# - create a list named `susan`. Call `hop_in` multiple times, passing `susan`
#   as the `pouch` argument
"""'susan' keeps getting added to the list susan which is acting as the pouch"""
# - simply call `hop_in` multiple times without specifying a `pouch`
"""If we don't specify a pouch, pouch will default to an empty list and our code will function the same as when we initialized susan as an empty list and passed it into pouch"""
# Now run this in the console. Was your prediction correct?
def hop_in(name: str, pouch: list[str] = []) -> None:
    if len(pouch) > 0:
        siblings = f' with their siblings: {", ".join(pouch)}'
    else:
        siblings = ''
    print(f"{name} hops into their mother's pouch{siblings}")
    pouch.append(name)


# You can point this function a folder on your computer and it will list
# all the files in it and any subfolders. Experiment with how `items` is
# built (Stack vs Queue) and see how the ordering changes.
def list_files(folder: str) -> list[str]:
    """Create a list of all files under `root`"""
    root = Path(folder)
    filenames: list[str] = []
    items: list[Path] = []
    while len(items) > 0:
        item = items.pop
        if item.is_dir():  # if the item is a folder...
            items.extend(item.iterdir())
        else:
            filenames.append(item.name)
    return filenames


# Implement this function using a list as a stack to find matching parentheses
# if a match is not found, raise a ValueError with a helpful message (like the
# index of the unmatched parenthesis)
def match_parentheses(line: str) -> list[str]:
    """Given a string containing an expression, return a list of subexpressions delineated by parenthesis"""
    stack = []
    results = []
    for i in range(len(line)):
        if line[i] == '(':
            stack.append(i)
        elif line[i] == ')':
            if len(stack) == 0:
                raise ValueError(f'unmatched parenthesis at index {i}')
            else:
                start = stack.pop
                results.append(line[start + 1 : i])
    if len(stack) > 0:
        raise ValueError(f'unmatched parenthesis at index {stack[-1]}')
    return results

