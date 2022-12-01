# https://adventofcode.com/2022/day/1 

# Read input 
with open("input.txt", "r") as f:
    data = f.read().splitlines()

# Part 1
def part1(data):
    # add the number to the next number if the next number is not '' 
    # and the next number is not the last number in the list
    for i, n in enumerate(data):
        if n != '':
            data[i] = int(n)
        #print(i, n)
        if i > len(data) - 2:
            break
        if n != '' and data[i+1] != '' and i+1 <= len(data)-1:
            data[i+1] = int(n) + int(data[i+1])
            #data[i-1] = ''
        #print(i, n)

    
    # remove the empty strings
    nums = list(filter(None, data))
    # can also do nums = [x for x in nums if x != '']

    print(max(nums))
    return nums

# Part 2
def part2(data): 
    # print the top 3 numbers and their sum
    #print(sorted(data, reverse=True)[:3])
    print(sum(sorted(data, reverse=True)[:3]))
        
nums = part1(data)
part2(nums)