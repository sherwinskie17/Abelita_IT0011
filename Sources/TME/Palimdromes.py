def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Input lines
lines = [
    "10,20,30,40,50",
    "90,10,1",
    "20,2,80,120",
    "200,171,459,151,20",
    "50,60,33,22,6",
    "101,202,303,404,505",
    "1000,800,200,2",
    "85,56,34,44,23",
    "5,10,20,40,80",
    "305,700,1058,587,12"
]

for i, line in enumerate(lines):
    numbers = line.split(',')
    total_sum = sum(int(num) for num in numbers)
    if is_palindrome(total_sum):
        print(f"Line {i + 1}: {line} (sum {total_sum}) - Palindrome")
    else:
        print(f"Line {i + 1}: {line} (sum {total_sum}) - Not a palindrome")