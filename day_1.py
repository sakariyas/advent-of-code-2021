def get_num_of_increments_in_list(l):
    print("Processing depth chart...")

    num_of_increments = 0
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            num_of_increments += 1
    print("The amount of depth increments are: " + str(num_of_increments) + "!")
    return num_of_increments


def convert_list_of_strings_to_ints(list_of_strings):
    result = []
    for value in list_of_strings:
        result.append(int(value))
    return result


def get_three_measurement_list(list_of_ints):
    result = []
    i = 0
    while i+2 < len(list_of_ints):
        result.append(list_of_ints[i] + list_of_ints[i + 1] + list_of_ints[i + 2])
        i += 1
    return result


def day_1_run():
    file = open('sea_floor_depth_chart', 'r')
    sea_floor_depth_chart = file.read().split()
    formatted_depth_chart = convert_list_of_strings_to_ints(sea_floor_depth_chart)

    print("------ Part 1 ------")
    get_num_of_increments_in_list(formatted_depth_chart)

    print("\n------ Part 2 ------\n")
    threes_measurement_chart = get_three_measurement_list(formatted_depth_chart)
    get_num_of_increments_in_list(threes_measurement_chart)

    file.close()
