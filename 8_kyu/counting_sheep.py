# When you can't sleep, count sheep!

# Level 8 kyu kata exercise

def count_sheep(number):
    sheep_count = ""
    for item in range(1, number + 1):
        sheep_count += str(item) + " sheep..."
    print(sheep_count)
    return sheep_count


count_sheep(0)