def sun_angle(time):
    ho = time.split(':')
    result = "I don't see the sun!"
    if int(ho[0]) > 5 and (int(ho[0]) < 18 or (int(ho[0]) == 18 and int(ho[1]) == 0)):
        dgr = 180 / 12
        h = (int(ho[0]) - 6) * dgr
        m = int(ho[1]) * (dgr / 60)
        result = h + m
    return result


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")