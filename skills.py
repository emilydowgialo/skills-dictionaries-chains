"""Skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different::

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """
    # initialize empty list where non duplicate words will be stored
    non_duplicate_words = []

    # iterate over list
    for item in words:
        # if an item in list is not already in list containing duplicate words..
        if item != non_duplicate_words:
            # append item if not in dupe list
            non_duplicate_words.append(item)

    # use set because sets do not contain duplicate items
    non_duplicate_words = set(non_duplicate_words)

    # return a list of non duplicate items
    return list(non_duplicate_words)


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    # produce a new set with items in items1 and items2
    unique_items = set(items1).intersection(items2)

    # return a list of the set containing unique common items in the 2 lists
    return list(unique_items)


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    # split the input string at spaces
    phrase_split = phrase.split()

    # initiate empty dictionary
    word_count = {}

    # iterate over words in the phrase
    for word in phrase_split:
        if word in word_count:

            # if the word is already a key in the dictionary, increase the value by 1
            word_count[word] += 1

        else:
            # if the word is not a key in the dictionary, set its value to 1
            word_count[word] = 1

    return word_count


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    english_to_pirate = {"sir": "matey", "hotel": "fleabag inn", "student": "swabbie", "boy": "matey", "professor": "foul blaggart", "restaurant": "galley", "your": "yer", "excuse": "arr", "students": "swabbies", "are": "be", "restroom": "head", "my": "me", "is": "be", "man": "matey"}

    # list for words that have been matched against translation dictionary
    translation_list = []

    # split the input phrase at spaces
    phrase_split = phrase.split()
    for word in phrase_split:

        # check if the key is in the English to Pirate dictionary
        if word in english_to_pirate:
            # if word is a key, we append the value to the translation list
            word = english_to_pirate[word]
            translation_list.append(word)

        else:
            # if word is not a key, the word is just added to the list
            translation_list.append(word)

    # join the words in the list with a space and return the translated phrase
    return " ".join(translation_list)


def sort_by_word_length(words):
    """Given list of words, return list of ascending (len, [words]).

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- the length
    of the words for that word-length, and the list of words of
    that word length.

    For example::

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]
    """
    # dictionary is useful here: we want key value pairs for length of word and word
    word_dict = {}

    for word in words:

        # word lengths will be keys
        word_length = len(word)

        # check if a word length is already a key in the dictionary
        if word_length not in word_dict:

            # if it is not a key in the dictionary, add it and set its value to an empty list
            word_dict[word_length] = []

        # append the word to the value list
        word_dict[word_length].append(word)

    # use .items method to return the dictionary as a list
    return word_dict.items()


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """
    # use set to remove duplicates from list, and listize the set
    numbers = list(set(numbers))

    # list where pairs that sum to zero will go
    sum_zero_pairs = []

    # use enumerate to get item indexes
    for index, item in enumerate(numbers):

        # start second iteration at the next number
        # eliminates cases like [-2, 2] and [2, -2]. The first loop would find -2,
        # and the second loop would find 2, and the first one would find 2, while
        # the second finds -2. Want to try pairs that haven't been tried before.
        for i in range(index+1, len(numbers)):

            # if both numbers sum to zero, add the pair to the list
            if item + numbers[i] == 0:
                sum_zero_pairs.append([item, numbers[i]])

        # if one of the items is zero, add a pair of zeros to the list
        if item == 0:
            sum_zero_pairs.append([item, 0])

    # return the list of pairs that sum to zero, with no dupes
    return sum_zero_pairs


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    # dictionary with the first letter of names as the key, and the name as the value
    name_dict = {}

    # we want to always start with the first word of the list of names; this
    # is a list containing that first word
    output_words = [names[0]]

    # add to the name_dict - if a key is not already in the dictionary, 
    # add an empty list as its value
    for name in names:
        if name[0] not in name_dict:
            name_dict[name[0]] = []

        # append word to the value list if the key already exists
        name_dict[name[0]].append(name)

    # condition for breaking the while loop set to False
    leave_loop = False

    # bind the first key to the first letter of the word item in the input list
    key = names[0][-1]

    # remove the first word from the name input list, because it is already
    # in the output list, and we can't use names twice
    first_word_remove_from_dict_key = output_words[0][0]
    del name_dict[first_word_remove_from_dict_key][0]

    while leave_loop is False:

        # if a dictionary key (the keys are lists of names) is empty, break out
        # of the loop
        error_check = name_dict.get(key)
        if error_check is None:
            leave_loop = True
            break

        # if the key's value, which is a list, has a length more than zero,
        # the next name to append to the output list is the next name that
        # begins the with the last letter of the previous word;
        # add this next word to the output list using pop to remove it from
        # the dictionary, as names can only be used once; bind a new value to
        # the key for the next time we go through the loop - the new key will be
        # the last letter of the word just appended to the output list
        if len(name_dict[key]) > 0:
            next_name = name_dict[key][0]
            output_words.append(next_name)
            name_dict[key].pop(0)
            key = next_name[-1]

        # if the key's value, which is a list, is not more than 0, we want to
        # break out of the loop
        else:
            leave_loop = True
            break

    return output_words


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
