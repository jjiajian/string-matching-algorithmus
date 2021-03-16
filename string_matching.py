#!/usr/bin/env python
import argparse
import glob
import os


class StringMatcher:
    def __init__(self, pattern, source):
        """
        Initialize class variables

        Args:
            pattern:
            source:
        """
        self.pattern = pattern
        self.source = source

    def naive(self, case_insensitive):
        """
        Uses the Naive Algorithm to search for a given pattern.

        Args:
            pattern (str): word to look for
            source (str): text to be searched
            case_insensitive (bool): ignore case sensitivity

        Returns:
            list: index(es) of the word sought
    """

        if case_insensitive:
            self.pattern = self.pattern.lower()
            self.source = self.source.lower()

        pat_length = len(self.pattern)
        source_length = len(self.source)
        indexes_n = []

        for i in range(source_length - pat_length + 1):
            j = 0

            while j < pat_length:
                if self.source[i + j] != self.pattern[j]:
                    break
                j += 1

            if j == pat_length:
                indexes_n.append(i)
                # return i
        return indexes_n

    def lps_table(self, pattern_length):
        """
        Facilitate the Knuth-Morris-Pratt-Algorithm. LPS stands for Longest proper Prefix which is Suffix.

            Args:
                pattern_length (int): length of the word

            Returns:
                list:
        """

        longest_pre_suffix = 0
        pointer = 1  # at index 0, lps always 0, so starts at 1
        lps = [0] * pattern_length

        while pointer < pattern_length:
            if self.pattern[longest_pre_suffix] == self.pattern[pointer]:
                longest_pre_suffix += 1
                lps[pointer] = longest_pre_suffix
                pointer += 1

            elif longest_pre_suffix == 0:
                lps[pointer] = 0
                pointer += 1

            else:
                longest_pre_suffix = lps[longest_pre_suffix - 1]
        print('############')
        print(lps)
        return lps

    def kmp(self, case_insensitive):
        """
        Uses the Knuth-Morris-Pratt-Algorithm to search for a given pattern.

        Args:
            pattern (str): word to look for
            source (str): text to be searched
            case_insensitive (bool): ignore case sensitivity

        Returns:
            list: index(es) of the word sought
        """

        if case_insensitive:
            self.pattern = self.pattern.lower()
            self.source = self.source.lower()

        pattern_length = len(self.pattern)
        source_length = len(self.source)
        lps = self.lps_table(pattern_length)  # Initialize

        source_pointer = 0
        pattern_pointer = 0
        indexes = []

        while source_pointer < source_length:
            # Character matches
            if self.pattern[pattern_pointer] == self.source[source_pointer]:
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
                indexes.append(source_pointer - pattern_pointer)
                pattern_pointer = lps[pattern_pointer - 1]

        return indexes


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f'{path} is not a valid directory path.')


def main():
    parser = argparse.ArgumentParser(prog='String Matcher', description='Finds the index of a target word in a text')
    parser.add_argument('pattern', metavar='pattern', type=str, help='the word/pattern to search for')
    parser.add_argument('-s', metavar='string', type=str, help='a text as input')
    parser.add_argument('-t', metavar='txt', type=argparse.FileType('r'), help='a .txt-formatted file as input')
    parser.add_argument('-d', metavar='dir', type=dir_path, help='a directory as input')
    parser.add_argument('-i', '--case-insensitive', action='store_true', help='ignore lowercase & uppercase letters')
    parser.add_argument('-n', '--naive', action='store_true', help='uses the naive Approach')
    args = parser.parse_args()

    if args.s:
        string_matcher_s = StringMatcher(args.pattern, args.s)
        print(f'String: {args.s}')
        print(f'Pattern: {args.pattern}')
        if not args.naive:
            print(f'Index(es): {", ".join(map(str, string_matcher_s.kmp(args.case_insensitive)))} \n')
        else:
            print(f'Index(es): {", ".join(map(str, string_matcher_s.naive(args.case_insensitive)))} \n')

    elif args.t:
        string_matcher_t = StringMatcher(args.pattern, args.t.read())
        print(f'File: {args.t.name}')
        print(f'Pattern: {args.pattern}')
        if not args.naive:
            print(f'Index(es): {", ".join(map(str, string_matcher_t.kmp(args.case_insensitive)))} \n')
        else:
            print(f'Index(es): {", ".join(map(str, string_matcher_t.naive(args.case_insensitive)))} \n')

    elif args.d:
        os.chdir(args.d)
        for filename in glob.glob('*.txt'):
            with open(os.path.join(os.getcwd(), filename), 'r') as f:
                all_text = f.read()
                string_matcher_d = StringMatcher(args.pattern, all_text)
                print(f'File: {filename}')
                print(f'Pattern: {args.pattern}')
            if not args.naive:
                print(f'Index(es): {", ".join(map(str, string_matcher_d.kmp(args.case_insensitive)))} \n')
            else:
                print(f'Index(es): {", ".join(map(str, string_matcher_d.naive(args.case_insensitive)))} \n')

    else:
        parser.error('Use at least one input method!')




    string_matcher_t = StringMatcher(args.pattern, args.d)
    # string_matcher = StringMatcher(args.pattern, args.t.read())  # for txt
    # if not args.naive:
    #     print(f'{args.pattern} found at index {", ".join(map(str, string_matcher.kmp(args.case_insensitive)))}')
    # # elif args.source == 'folder':
    # #     print(f'{args.pattern} found at index {string_matcher.kmp(args.case_insensitive)}')
    # else:
    #     print(f'{args.pattern} found at index {", ".join(map(str, string_matcher.naive(args.case_insensitive)))}')

   # my_parser.error if no arguments

    # string_matcher = StringMatcher(args.pattern, args.source.read())
    # if args.naive:
    #     print(f'{args.pattern} found at index {string_matcher.naive(args.case_insensitive)}')
    # else:
    #     if args.txt:
    #         print(f'{args.pattern} found at index {string_matcher.kmp(args.case_insensitive)}')


    # print(apple.naive("GJ", "AAAABBGGJJJJ"))  # 7
    # print(apple.kmp("onion", "onisOnionskl"))  # 4

    # print(string_matcher.kmp(args))
    # print(apple.naive("onion", "onisonionskl"))


if __name__ == '__main__':
    main()

