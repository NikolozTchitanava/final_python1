#jam is acronim of jami, which means sum in Georgian
def calculate_checksum(payload):
    digits = str(payload)[::-1]
    a = []
    jam1 = 0
    jam2 = 0

    for i, digit in enumerate(digits):
        if i % 2 == 0: 
            a.append(int(digit) * 2)
            jam1 += int(digit)
        else: 
            jam2 += int(digit)

    total_sum = sum((j // 10 + j % 10) for j in a)
    total_sum += jam2
    if total_sum % 10 == 0: 
        checksum = 0
        high = total_sum
    else:
        high = ((total_sum // 10 + 1) * 10)
        checksum = high - total_sum

    print("Sum is:", total_sum)
    print("Nearest round number:", high)
    print("Checksum is:", checksum)

payload = int(input("Enter payload: "))
calculate_checksum(payload)


