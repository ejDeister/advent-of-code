with open("advent-of-code\\Day_1\\input.txt", encoding="utf-8") as input_file:
    #Part 1
    TOTAL = 0
    nums1, nums2 = [], []
    for line in input_file:
        num1, num2 = line.split()
        nums1.append(num1)
        nums2.append(num2)
    nums1.sort()
    nums2.sort()
    for num1, num2 in zip(nums1, nums2):
        TOTAL += abs(int(num1)-int(num2))
    print("Total:",TOTAL)

    #Part 2
    unique_nums1 = set()
    frequencies = {}
    for num in nums1:
        unique_nums1.add(num)
    for num in nums2:
        if num in unique_nums1:
            frequencies[num] = frequencies.get(num, 0) + int(num)
    sim_score = sum(freqs for freqs in frequencies.values())
    print("Similarity Score:", sim_score)
