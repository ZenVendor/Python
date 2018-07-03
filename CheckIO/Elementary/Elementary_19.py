def most_frequent(data):
    most = ''
    count = 0
    for word in data:
        if data.count(word) > count:
            most = word
            count = data.count(word)
    return most

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    assert most_frequent(["a","a","z"]) == 'a'
    print('Done')
