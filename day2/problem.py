f = open("day2/input.txt", "r")
lines = f.readlines()


def part1():
    possible_games = []
    for index, line in enumerate(lines):
        game = line.rstrip()
        draws = game.split(":")[1].split(";")
        impossible_game = False
        for draw in draws:
            draw = draw.strip()
            dices = draw.split(",")
            for dice in dices:
                dice = dice.strip()
                number, color = dice.split(" ")
                if color == "red":
                    if int(number) > 12:
                        impossible_game = True
                if color == "green":
                    if int(number) > 13:
                        impossible_game = True
                if color == "blue":
                    if int(number) > 14:
                        impossible_game = True

        if not impossible_game:
            possible_games.append(index + 1)

    print("Possible games:", possible_games)
    print(sum(possible_games))


def part2():
    set_list = []
    for game in lines:
        max_red = 0
        max_green = 0
        max_blue = 0
        draws = game.split(":")[1].split(";")
        for draw in draws:
            draw = draw.strip()
            dices = draw.split(",")
            for dice in dices:
                dice = dice.strip()
                number, color = dice.split(" ")
                if color == "red":
                    if int(number) > max_red:
                        max_red = int(number)

                if color == "green":
                    if int(number) > max_green:
                        max_green = int(number)

                if color == "blue":
                    if int(number) > max_blue:
                        max_blue = int(number)

        set_power = max_red * max_green * max_blue
        set_list.append(set_power)

    print("Answer part2: ", sum(set_list))


part2()
