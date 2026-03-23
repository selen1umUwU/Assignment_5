def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    test_list = [5, 10, 15, 20]
    result = sum_of_list(test_list)
    print(result)

main()