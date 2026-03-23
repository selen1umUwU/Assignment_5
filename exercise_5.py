def remove_uneven(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def main():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cut_down_list = remove_uneven(original_list)
    
    print(original_list)
    print(cut_down_list)

main()