with open("advent-of-code\\Day_2\\input.txt", encoding="utf-8") as input_file:
    total_safe = 0
    reports = [[int(item) for item in line.split()] for line in input_file]
    for report in reports:
        safe = True
        decreasing = True if report[0] > report[1] else False
        for i in range(1, len(report)):
            if (decreasing and report[i-1] < report[i]):
                safe = False
            if not decreasing and report[i-1] > report[i]:
                safe = False
            dif = abs(int(report[i]) - int(report[i-1]))
            if (dif < 1 or 3 < dif):
                safe = False

        if safe:
            total_safe += 1
    print(total_safe)
