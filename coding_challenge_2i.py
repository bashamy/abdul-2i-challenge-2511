def identify_largest_sum(str_list: list):
    """
    Assumptions:
    - All strings in the list has no number then it returns 0.
    - If List is empty then it returns 0.
    - Special chars (eg: ¼, /, ^, *, +, -, %) are treated as string and not numbers.
    - If there are any exceptions, it will return 0
    """
    max_sum = 0
    try:
        for val in str_list:
            new_sum = sum(int(c) for c in val if c.isdigit())
            max_sum = new_sum if new_sum > max_sum else max_sum
        return max_sum
    except Exception:
        return 0


# Test Cases
# ************
assert identify_largest_sum(["dh7js4jf", "or2rjvn2w", "h1n36mfl", "a7e6fw"]) == 13
assert identify_largest_sum(["abcdef", "ghijkl"]) == 0
assert identify_largest_sum(["a123b", "a123b", "c123d", "e123f", "123gh"]) == 6
assert identify_largest_sum(["a¼b"]) == 0
assert identify_largest_sum(["a1/2b", "ccc2^3", "dd2%3d", "dd2+3d", "dd9-9d", "dd5*3d"]) == 18
assert identify_largest_sum([]) == 0
assert identify_largest_sum(["123", 456, "789"]) == 0
