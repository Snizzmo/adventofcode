"""PART 1"""


def part1():
    # read the txt from data/1_1.txt
    data = []
    with open("data/1/1.txt", "r") as f:
        for line in f.readlines():
            data.append(line.strip())

    # get only the numbers from the strings, using regex. There may be multiple numbers in a string - we want them all
    import re

    data = [re.findall(r"[-+]?\d*\.\d+|\d+", x) for x in data]
    # append all the numbers together into one list, so [[1, 23, 4], [8]] becomes [[1234], [8]]
    data = [[("".join(x))] for x in data]
    # now we have a bunch of numbers as strings. get the first and last character of each string and append them together.
    # This is the format we want for the final output
    data = [x[0][0] + x[0][-1] for x in data]
    # convert the strings to integers
    data = [int(x) for x in data]
    # sum the integers
    print(data)
    print(sum(data))


"""PART 2"""


# well it looks like some of the numbers are spelled out. Gotta restart
def part2():
    data2 = []
    with open("data/1/1.txt", "r") as f:
        for line in f.readlines():
            data2.append(line.strip())

    # We gotta get all the numbers from the strings again, but this time we have to deal with the spelled out numbers
    # We'll use a dictionary to convert the spelled out numbers to integers
    num_dict = {
        # "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    # the numbers are not pretty, i.e. [jlvnsbshjmxnxfouronesix2zlff5]
    # so we'll use regex to extract the numbers
    import re

    pattern = "|".join(num_dict.keys())
    # replace the spelled out numbers with the integers
    # data2 = [re.sub(pattern, lambda m: str(num_dict[m.group(0)]), x) for x in data2]
    # The issue with this is that when the numbers overlap, i.e. [oneight], it will only replace the first one.
    # To fix this, we need to replace retain the first and last characters of the string, and replace the middle with the integer
    # We'll use regex for this again
    print(data2)
    data2 = [
        re.sub(
            pattern,
            lambda m: m.group(0)[0] + str(num_dict[m.group(0)]) + m.group(0)[-1],
            x,
        )
        for x in data2
    ]
    print(data2)
    # do it again
    data2 = [
        re.sub(
            pattern,
            lambda m: m.group(0)[0] + str(num_dict[m.group(0)]) + m.group(0)[-1],
            x,
        )
        for x in data2
    ]
    print(data2)
    # now it's the same as part 1
    data2 = [re.findall(r"[-+]?\d*\.\d+|\d+", x) for x in data2]
    print(data2)
    data2 = [[("".join(x))] for x in data2]
    print(data2)
    data2 = [x[0][0] + x[0][-1] for x in data2]
    print(data2)
    data2 = [int(x) for x in data2]
    print(data2)
    print(sum(data2))


if __name__ == "__main__":
    # part1()

    part2()
