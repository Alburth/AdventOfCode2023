f = open("day5/input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]


def get_maps():
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temp = []
    temp_to_humid = []
    humid_to_location = []

    i = 0
    while i < len(lines):
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
        map_dict.append((int(dest), int(source), int(range_)))
        read_index += 1
        if read_index >= len(lines) - 1:
            return read_index
    return read_index


def get_seeds():
    seeds = []
    for line in lines:
        if "seeds:" in line:
            for seed in line[7:].split(" "):
                seeds.append(seed)
    return seeds


def get_seeds_p2():
    seeds = []
    for line in lines:
        if "seeds:" in line:
            for seed in line[7:].split(" "):
                seeds.append(seed)
    # Interpret as ranges
    ranges = []
    for i in range(0, len(seeds), 2):
        start = int(seeds[i])
        length = int(seeds[i + 1])
        ranges.append(range(start, start + length))

    return ranges


def seed_to_location(seed):
    soil = read_map(seed_to_soil, int(seed))
    fert = read_map(soil_to_fertilizer, soil)
    water = read_map(fertilizer_to_water, fert)
    light = read_map(water_to_light, water)
    temp = read_map(ligth_to_temp, light)
    humid = read_map(temp_to_humid, temp)
    location = read_map(humid_to_location, humid)
    return location

def location_to_seed(location):
    humid = read_map(humid_to_location, location, backwards=True)
    temp = read_map(temp_to_humid, humid, backwards=True)
    light = read_map(ligth_to_temp, temp, backwards=True)
    water = read_map(water_to_light, light, backwards=True)
    fert = read_map(fertilizer_to_water, water, backwards=True)
    soil = read_map(soil_to_fertilizer, fert, backwards=True)
    seed = read_map(seed_to_soil, soil, backwards=True)
    return seed

def read_map(map, key, backwards=False):
    for dest, source, range_ in map:
        # Read direction
        if backwards:
            offset = source - dest
            if dest <= key and key < dest + range_:
                key = key + offset
                return key
            
        else:
            offset = dest - source
            if source <= key and key < source + range_:
                key = key + offset
                return key
    return key

    # if key not in map:
    #     return key
    # return map[key]


(
    seed_to_soil,
    soil_to_fertilizer,
    fertilizer_to_water,
    water_to_light,
    ligth_to_temp,
    temp_to_humid,
    humid_to_location,
) = get_maps()

def part1():
    seeds = get_seeds()
    locations = []
    for seed in seeds:
        locations.append(seed_to_location(seed))

    print("answer: ", min(locations))

def part2():
    # Tests
    def test_conversions_forward():
        seed = 82
        location = seed_to_location(seed)
        assert location == 46
    def test_conversions_backward():
        location = 46
        seed = location_to_seed(location)
        assert seed == 82

    def test_individual_maps():
        location = 46
        humid = read_map(humid_to_location, location, backwards=True)
        assert humid == 46
        temp = read_map(temp_to_humid, humid, backwards=True)
        assert temp == 45
        light = read_map(ligth_to_temp, temp, backwards=True)
        assert light == 77
        water = read_map(water_to_light, light, backwards=True)
        assert water == 84
        fert = read_map(fertilizer_to_water, water, backwards=True)
        assert fert == 84
        soil = read_map(soil_to_fertilizer, fert, backwards=True)
        assert soil == 84
        seed = read_map(seed_to_soil, soil, backwards=True)
        assert seed == 82
        
    
    # test_individual_maps()
    # test_conversions_forward()
    # test_conversions_backward()
    # Start with location 0 and go upwards until one seed is found

    seed_ranges = get_seeds_p2()
    closest_location = None
    location = 0
    while closest_location is None:
        seed = location_to_seed(location)
        if seed != location:
            for seed_range in seed_ranges:
                if seed in seed_range:
                    closest_location = location
                    break
        location += 1

    print("answer: ", closest_location)

part2()
