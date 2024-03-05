f = open("day5/input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

def get_maps():
    seed_to_soil = {}
    soil_to_fertilizer = {}
    fertilizer_to_water = {}
    water_to_light = {}
    light_to_temp = {}
    temp_to_humid = {}
    humid_to_location = {}

    i = 0
    while  i < len(lines):
        if lines[i] == "seed-to-soil map:":
            i = fill_map(seed_to_soil, i)

        elif lines[i] == "soil-to-fertilizer map:":
            i = fill_map(soil_to_fertilizer, i)

        elif lines[i] == "fertilizer-to-water map:":
            i = fill_map(fertilizer_to_water, i)

        elif lines[i] == "water-to-light map:":
            i = fill_map(water_to_light, i)

        elif lines[i] == "light-to-temperature map:":
            i = fill_map(light_to_temp, i)

        elif lines[i] == "temperature-to-humidity map:":
            i = fill_map(temp_to_humid, i)

        elif lines[i] == "humidity-to-location map:":
            i = fill_map(humid_to_location, i)
        i += 1

    return (
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temp,
        temp_to_humid,
        humid_to_location,
    )

def fill_map(map_dict, read_index):
    read_index += 1
    while "" != lines[read_index]:
        dest, source, range_ = lines[read_index].split(" ")
        add_entries(map_dict, int(dest), int(source), int(range_))
        read_index += 1
        if read_index >= len(lines) - 1:
            return read_index
    return read_index


def add_entries(map_dict, dest, source, range_):
    for j in range(range_):
        map_dict[source + j] = dest + j
    return map_dict


def get_seeds():
    seeds = []
    for line in lines:
        if "seeds:" in line:
            for seed in line[7:].split(" "):
                seeds.append(seed)
    return seeds


def seed_to_location(seed):
    soil = read_map(seed_to_soil, int(seed))
    fert = read_map(soil_to_fertilizer, soil)
    water = read_map(fertilizer_to_water, fert)
    light = read_map(water_to_light, water)
    temp = read_map(ligth_to_temp, light)
    humid = read_map(temp_to_humid, temp)
    location = read_map(humid_to_location, humid)
    return location

def read_map(map, key):
    if key not in map:
        return key
    return map[key]


seeds = get_seeds()
print(seeds)
(seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        ligth_to_temp,
        temp_to_humid,
        humid_to_location) = get_maps()
print("YH")

locations = []
for seed in seeds:
    locations.append(seed_to_location(seed))

print("answer: ", min(locations))
