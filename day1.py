"""
--- Day 1: Report Repair ---

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input);
apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two 
numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces
1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you 
get if you multiply them together?

Your puzzle answer was 870331.

--- Part Two ---

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin 
they had left over from a past vacation. They offer you a second one if you can find three numbers
in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. 
Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

"""

def find_terms(target, n, added, product=1):
    
    '''
        Function to open a file and find 2 numbers that add up to a specific number.

        :param target: path to file to read from.
        :param n: number of operands for the sum.
        :param added: target sum.
        :param product: defaults to 1.

    '''
    
    inputFile = open(target, 'r')
    lines = inputFile.read()
    
    val_int = []
    for line in lines.split("\n"):
        val_int.append(int(line))

    if added <= 0:
        print("Sum must be > 0.")

    if n == 2:
        for x in val_int:
            y = added - x
            if y in val_int:
                res = x * y * product
                return res
    elif n > 2:
        for x in val_int:
            if x > added:
                continue
            res = find_terms(target, n - 1, added - x, x * product)
            if res is not None:
                return res
    inputFile.close()
    return None

# --- Part 1 ---

print("Part1: ", find_terms("./data/1_input.txt", 2, 2020))

# --- Part 2 ---

print("Part2: ", find_terms("./data/1_input.txt", 3, 2020))
