"""Skills Assessment: Lists.

To work on an item, uncomment the entire function (including the docstring)
and then run this script. It should output an error that the newly-uncommented
function is now failing its tests.

Edit the function body until you have a solution and the test passes, and then
move on to the next function.

This assessment is DUE TO YOUR ADVISOR BY SUNDAY EVENING.
"""


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.
    """
    
    new = []
    for num in number_list:
        if num % 2 != 0:
            new.append(num)
    return new


def all_even(number_list):
    """Return a list of only the even numbers in the input list.
    """

    new = []
    for num in number_list:
        if num %2 == 0:
            new.append(num)
    return new


def print_indeces(my_list):
    """Print the index of each list item, followed by the item itself.
    """

    for item in my_list:
        print my_list.index(item), item


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.
    """
    new = []
    for item in word_list:
        if len(item) > 4:
            new.append(item)
    return new

def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    """
    return min(number_list)
    

def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.
    """

    return max(number_list)


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.
    """
    new = []
    for num in number_list:
        new.append(float(num)/2)

    return new


def word_lengths(word_list):
    """Return the length of words in the input list.
    """

    new = []
    for word in word_list:
        new.append(len(word))
    return new

def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.
    """

    sum_num = 0
    for num in number_list:
        sum_num += num
    return sum_num


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.
    """
    mult_num = 1
    for num in number_list:
        mult_num *= num
    return mult_num


def join_strings(word_list):
    """Return a string of all input strings joined together.
    """
    final_string = ""
    for word in word_list:
        final_string += word
    return final_string


def average(number_list):
    """Return the average (mean) of the list of numbers given.
    """

    return float(sum_numbers(number_list))/len(number_list)


##############################################################################
# END OF SKILLS TEST; YOU CAN STOP HERE OR YOU CAN WORK ON ADVANCED PROBLEMS


def advanced_join_strings(list_of_words):
    """Return a single string with each word from the input list
     separated by a comma.
    """
    final_string = ""
    if len(list_of_words) < 2:
        return list_of_words[0]

    else:
        for word in list_of_words[:-1]:
            final_string += word + ", "

    return final_string + list_of_words[-1]


##############################################################################
# You can ignore everything after here

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
