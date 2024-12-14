with open("advent-of-code\\Day_2\\input.txt", encoding="utf-8") as input_file:
    # #Part 1
    # total_safe = 0
    # reports = [[int(item) for item in line.split()] for line in input_file]
    # for report in reports:
    #     safe = True
    #     decreasing = True if report[0] > report[1] else False
    #     for i in range(1, len(report)):
    #         if (decreasing and report[i-1] < report[i]):
    #             safe = False
    #         if not decreasing and report[i-1] > report[i]:
    #             safe = False
    #         dif = abs(int(report[i]) - int(report[i-1]))
    #         if (dif < 1 or 3 < dif):
    #             safe = False

    #     if safe:
    #         total_safe += 1
    # print(total_safe)

    # #Part 2 - WIP had to cheat :/
    def is_safe(report: list) -> int: # pylint: disable=missing-function-docstring
        for num in report:
            report_copy = report.copy()
            report_copy.remove(num)
            decreasing = report_copy[0] > report_copy[1]
            
            for i in range(len(report_copy)-1):
                if decreasing and report_copy[i] < report_copy[i+1]:
                    return 0
                if not decreasing and report_copy[i] > report_copy[i+1]:
                    return 0
                difference = abs(report_copy[i] - report_copy[i+1])
                if difference < 1 or 3 < difference:
                    return 0
            return 1

    num_safe = sum(is_safe(report) for report in [[int(item) for item in line.split()] for line in input_file])
    print(num_safe)

