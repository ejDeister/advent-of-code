with open("advent-of-code\\Day_1\\input.txt", encoding="utf-8") as input_file:
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
    print(TOTAL)

