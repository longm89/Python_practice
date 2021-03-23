"""
Given a wordlist, we want to implement a spellchecker 
that converts a query word into a correct word.

For a given query word, the spell checker handles 
two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive), 
then the query word is returned with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') 
of the query word with any vowel individually, it matches a word 
in the wordlist (case-insensitive), then the query word is returned with 
the same case as the match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), 
you should return the same word back.
When the query matches a word up to capitlization, 
you should return the first such match in the wordlist.
When the query matches a word up to vowel errors, 
you should return the first such match in the wordlist.
If the query has no matches in the wordlist, 
you should return the empty string.
Given some queries, return a list of words answer, 
where answer[i] is the correct word for query = queries[i].

Example 1:

Input: wordlist = ["KiTe","kite","hare","Hare"], 
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
 

Note:

1 <= wordlist.length <= 5000
1 <= queries.length <= 5000
1 <= wordlist[i].length <= 7
1 <= queries[i].length <= 7
All strings in wordlist and queries consist only of english letters.
"""


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """
        First, we check for the exact word in the list (case sentitive)
        Second, we check for Capitalization (case in-sensitive)
        Third, we check for case-insensitive and vowers
        To check if a query exists in a wordlist, we could use a
        dictionary in Python
        """

        def replace_vowers(word):
            vowers = ["a", "e", "i", "o", "u"]
            new_word = ""
            for letter in word:
                if letter in vowers:
                    new_word += "*"
                else:
                    new_word += letter
            return new_word

        answer = []

        exact_word_list = {word: word for word in wordlist}
        capitalization_word_list = {word.lower(): word for word in wordlist[::-1]}
        mask_cap_mask_vowers_list = {
            replace_vowers(word.lower()): word for word in wordlist[::-1]
        }
        for query in queries:

            # the case-sensitive case
            if query in exact_word_list:
                answer.append(query)
                continue
            # the Capitalization case
            if query.lower() in capitalization_word_list:
                answer.append(capitalization_word_list[query.lower()])
                continue
            # the vowel and case-insensitive case:
            if replace_vowers(query.lower()) in mask_cap_mask_vowers_list:
                answer.append(mask_cap_mask_vowers_list[replace_vowers(query.lower())])
                continue

            # couldn't find the word
            answer.append("")

        return answer
