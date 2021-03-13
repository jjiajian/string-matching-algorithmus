#!/usr/bin/env python
import argparse


class StringMatcher:
    def naive(self, pattern, source, case_insensitive):
        """Uses the Naive Algorithm to search for a given pattern.

        Args:
            pattern (str): word to look for
            source (str): text to be searched
            case_insensitive (bool): ignore case sensitivity

        Returns:
            int: index of the word sought
        """

        if case_insensitive:
            pattern = pattern.lower()
            source = source.lower()

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

    def lps_table(self, pattern, pattern_length):
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

    def kmp(self, pattern, source, case_insensitive):
        """Uses the Knuth-Morris-Pratt-Algorithm to search for a given pattern.

        Args:
            pattern (str): word to look for
            source (str): text to be searched
            case_insensitive (bool): ignore case sensitivity

        Returns:
            int: index of the word sought
        """

        if case_insensitive:
            pattern = pattern.lower()
            source = source.lower()

        pattern_length = len(pattern)
        source_length = len(source)
        lps = self.lps_table(pattern, pattern_length)  # Initialize

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
                print(source_pointer - pattern_pointer, end=', ')
                pattern_pointer = lps[pattern_pointer - 1]  #Code unreachable
        # return self.kmp(pattern, source)
        #         return source_pointer - pattern_pointer

def main():
    my_parser = argparse.ArgumentParser(prog='String Matcher', description='Finds the index of a target word in a text')
    my_parser.add_argument('Pattern', metavar='pattern', type=str, help='the word/pattern to search for')
    my_parser.add_argument('Source', metavar='source', type=str, help='a text, a .txt-formatted file or a folder')
    my_parser.add_argument('-i', '--case-insensitive', action='store_true', help='ignore lowercase & uppercase letters')
    my_parser.add_argument('-n', '--naive', action='store_true', help='uses the naive Approach')
    args = my_parser.parse_args()
    case_insensitve = args.case_insensitive

        # string_search
    print(args.naive)
    print(args.case_insensitive)
    print('word is: ' + args.Pattern)
    print('text is: ' + args.Source)
    lower_key = '-i'
    # file_obj = open(args.Text, 'r')
    # print(file_obj.read())
    # file = str(file_obj)
    # print(type(file))

    # for f in os.listdir('/string-matching-algorithmus'):
    #     if f.endswith('.txt'):
    #         print(os.path.join('*/string-matching-algorithmus/'), f)


    string_matcher = StringMatcher()
    if args.naive:
        print(string_matcher.naive(args.Pattern, args.Source, args.case_insensitive))
    print(string_matcher.kmp(args.Pattern, args.Source, args.case_insensitive))


    # print(apple.naive("GJ", "AAAABBGGJJJJ"))  # 7
    # print(apple.kmp("onion", "onisOnionskl"))  # 4

    # print(string_matcher.kmp(args))
    # print(apple.naive("onion", "onisonionskl"))


if __name__ == '__main__':
    main()

