import argparse


def naive(pattern, source):
    """Uses the Naive Algorithm to search for a given pattern"""
    pat_length = len(pattern)
    source_length = len(source)

    for current_letter_pos in range(source_length - pat_length + 1):
        next_letter_pos = 0

        while next_letter_pos < pat_length:
            if source[current_letter_pos + next_letter_pos] != pattern[next_letter_pos]:
                break
            next_letter_pos += 1

        if next_letter_pos == pat_length:
            print(current_letter_pos)


def kmp(pattern, source):
    """Uses the Knuth-Morris-Pratt-Algorithm to search for a given pattern"""
    pass


def main():
    # my_parser = argparse.ArgumentParser(description='Match the index of a target word')
    # my_parser.add_argument('Word', metavar='word', type=str, help='the word to search for')
    print(naive("AA", "AAAABBGGJJJJ"))  # test


if __name__ == '__main__':
    main()

