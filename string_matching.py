import argparse


def naive(pattern, source):
    """Uses the Naive Algorithm to search for a given pattern.

    Args:
        pattern (str): substring (word to look for)
        source (str): string (text)

    Returns:
        int: index of the word
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


def kmp(pattern, source):
    """Uses the Knuth-Morris-Pratt-Algorithm to search for a given pattern.

    Args:
        pattern (str): substring (word to look for)
        source (str): string (text)

    Returns:
        int: index of the word
    """
    pass


def main():
    # my_parser = argparse.ArgumentParser(description='Match the index of a target word')
    # my_parser.add_argument('Word', metavar='word', type=str, help='the word to search for')
    print(naive("GJ", "AAAABBGGJJJJ"))  # test


if __name__ == '__main__':
    main()

