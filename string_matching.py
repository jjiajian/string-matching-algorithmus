import argparse


def naive(pattern, source):
    """Uses the Naive Algorithm to search for a given pattern.

    Args:
        pattern (str): word to look for
        source (str): text to be searched

    Returns:
        int: index of the word sought
    """

    pat_length = len(pattern)
    source_length = len(source)

    for i in range(source_length - pat_length + 1):
        j = 0

        while j < pat_length:
            if source[i + j] != pattern[j]:
                break
            j += 1

        if j == pat_length:
            return i


def lps_table(pattern, pattern_length):
    """Facilitate the Knuth-Morris-Pratt-Algorithm. LPS stands for Longest proper Prefix which is Suffix.

        Args:
            pattern (str): word to look for
            pattern_length (int): length of the word

        Returns:
            int: index of the word sought
        """

    longest_pre_suffix = 0
    pointer = 1  # at index 0, lps always 0, so starts at 1
    lps = [0] * pattern_length

    while pointer < pattern_length:
        if pattern[longest_pre_suffix] == pattern[pointer]:
            longest_pre_suffix += 1
            lps[pointer] = longest_pre_suffix
            pointer += 1

        elif longest_pre_suffix == 0:
            lps[pointer] = 0
            pointer += 1

        else:
            longest_pre_suffix = lps[longest_pre_suffix - 1]

    return lps


def kmp(pattern, source):
    """Uses the Knuth-Morris-Pratt-Algorithm to search for a given pattern.

    Args:
        pattern (str): word to look for
        source (str): text to be searched

    Returns:
        int: index of the word sought
    """

    pattern_length = len(pattern)
    source_length = len(source)
    lps = lps_table(pattern, pattern_length)  # Initialize

    source_pointer = 0
    pattern_pointer = 0

    while source_pointer < source_length:
        # Character matches
        if pattern[pattern_pointer] == source[source_pointer]:
            pattern_pointer += 1
            source_pointer += 1
        # Character does not match
        else:
            if pattern_pointer != 0:
                pattern_pointer = lps[pattern_pointer - 1]
            else:
                source_pointer += 1
        # Pattern found and matched
        if pattern_pointer == pattern_length:
            return source_pointer - pattern_pointer
            


def main():
    # my_parser = argparse.ArgumentParser(description='Match the index of a target word')
    # my_parser.add_argument('Word', metavar='word', type=str, help='the word to search for')
    print(kmp("GJ", "AAAABBGGJJJJ"))  # test
    print(kmp("onion", "onisonionskl"))  # test


if __name__ == '__main__':
    main()

