# String-Matching Algorithm
A simple program that searches for a substring from a string with the help of the Knuth-Morris-Pratt Algorithm or the naive approach.

## Uni-Project submission
* Course name: Programmierung I
* Course code: PRO-1A
* Project theme: String-Matching
* Student name: Jia Jian Lee

## Table of contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Usage](#usage)
* [FAQs](#FAQs)

## General Info
This program is designed to be called from the command line. It will search for the substring/word and gives out its respective position(s) in a string/text, both provided by the user via the command line. The user has three options to input his/her text:
* enter directly via command line
* a .txt-formatted file
* a directory, in which the program will search for all .txt-formatted files (Best for seraching in multiple .txt-files)

By default the program uses the Knuth-Morris-Pratt Algorithm, which is more efficient in terms of time complexity than the naive approach, to search for the substring/word. The user however has the option to select the naive approach if preferred. Case sensitivity is possible to be switched off by the user, else the programm is case sensitive by nature. After the user entered a substring/word and a string/text correctly, the program will return the index or if the word appeares more than once the indices of the substring/word. If the substring/word is not found, the program will return a empty Index, e.g. ```Index(es):   ```. The sample .txt-files which are used in the usage examples below are available in the repository. 

## Technologies
Project is created with Python 3.8

## Usage
The program can be called directly from the command line

```python string_matching.py```

### Examples of use
Below are a few examples of searching the word ```dog```.
* String as text, case insensitive, Knuth-Morris-Pratt 

```python string_matching.py "dog" -s "As a Dog, I go to school by bus and meet my dog friend." -i```

```
# returns
String: As a Dog, I go to school by bus and meet my dog friend.
Pattern: dog
Index(es): 5, 44
```
* .txt-file as text, case sensitive, Knuth-Morris-Pratt

```python string_matching.py "dog" -t "dog.txt"```

```
# returns
File: dog.txt
Pattern: dog
Index(es): 44, 82, 140, 171
```

* a directory with .txt-files, case insensitive, naive approach

```python string_matching.py "dog" -d "./sample_directory" -i -n```

```
# returns
Directory: ./sample_directory
File: berlin.txt
Pattern: dog
Index(es): 254 

Directory: ./sample_directory
File: dog.txt
Pattern: dog
Index(es): 5, 44, 82, 140, 171 

Directory: ./sample_directory
File: peloton.txt
Pattern: dog
Index(es):  
```

## FAQs
A list of frequently asked questions
1. **What happens if I entered an empty pattern (e.g. "", " ")?**
 
```python string_matching.py " " -s "As a Dog, I go to school by bus and meet my dog friend." -i``` 
``` 
$ Search Pattern is empty! Please try again!
```

2. __What happens if I entered an empty string (e.g. -s " ")?__ 

```python string_matching.py "dog" -s " "``` 
``` 
$ Empty String found!
```
