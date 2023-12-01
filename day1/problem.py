f = open("day1/input.txt", "r")
lines = f.readlines()

numberChars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
str_to_int_map = {"zero": 0,
                  "one": 1,
                  "two": 2,
                  "three": 3,
                  "four": 4,
                  "five": 5,
                  "six": 6,
                  "seven": 7,
                  "eight": 8,
                  "nine": 9}


def number_in_string(string):
    for number_str in str_to_int_map.keys():
        if number_str in string:
            return number_str
    return None


def part1():
    code_numbers = []
    for line in lines:
        # get all number
        number = ""
        for char in line:
            if char in numberChars:
                number += char
        code_nr = number[0]+number[-1]
        code_numbers.append(int(code_nr))

    print("answer part 1:", sum(code_numbers))


def part2():
    def get_first_number(line):
        running_window = ""
        for char in line:
            if char in numberChars:
                return char
            else:
                running_window += char
                if (number := number_in_string(running_window)) != None:
                    return str(str_to_int_map[number])

    def get_second_number(line):
        running_window = ""
        for i in range(len(line)-1, -1, -1):
            char = line[i]
            if char in numberChars:
                return char
            else:
                running_window = char + running_window
                if (number := number_in_string(running_window)) != None:
                    return str(str_to_int_map[number])

    codes = []
    for line in lines:
        line = line.rstrip()
        num1 = get_first_number(line)
        num2 = get_second_number(line)
        codes.append(int(num1 + num2))
    print("answer part2: ", sum(codes))


part1()
part2()
