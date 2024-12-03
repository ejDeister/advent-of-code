def split_nums(given: str):
    for pair in given:            
        num1, num2 = 0, 0
        i = 0
        while pair[i] != " ":
            i += 1
        num1 = pair[0:i]

        while pair[i] == " ":
            i += 1
        num2 = pair[i:]
        
        distance1 = abs(int(num1)-int(num2))
        print('dist:', distance1, 'nums:', num1, num2)

        yield distance1

total = 0

with open("advent-of-code\Day_1\input.txt") as input_file:
    for distance in split_nums(input_file):
        total += distance
    print(total)


