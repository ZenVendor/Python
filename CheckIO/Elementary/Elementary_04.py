import re

def second_index_attempt1(text: str, symbol: str) -> int:
    p = re.compile(symbol)
    r = p.finditer(text)
    result = list(r)
    if len(result) > 1:
        return result[1].start()
    else:
        return

def second_index_attempt1_clean(text: str, symbol: str) -> int:
    result = list(re.finditer(symbol, text))
    if len(result) > 1:
        return result[1].start()
    else:
        return

def second_index(text: str, symbol: str) -> int:
    try:
        return text.index(symbol, text.index(symbol) + 1)
    except:
        return None

print(second_index("sims", "s"))

if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
