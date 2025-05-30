
# Word search

The exercise template includes the file words.txt, which contains words in English.

Please write a function named find_words(search_term: str). It should return a list containing all the words in the file which match the search term.

The search term may include lowercase letters and the following wildcard characters:

- A dot . means that any single character is acceptable in its place. For example, ca. would yield words like cat and car, p.ng would yield words like ping and pong, and .a.e would yield words like sane, care and late.

- An asterisk \* at the end of the search term means that any word which begins with the search term is acceptable. An asterisk at the beginning of the search term means that any word which ends with the search term is acceptable. For example, ca* would yield words like california, cat, caring and catapult, while \* ane would yield words like crane, insane and aeroplane. There can only ever be a single asterisk in the search term.

- If there are no wildcard characters in the search term, only words which match the search term exactly are returned.

You may assume both wildcards are never used in the same search term.

The words in the file are all written in lowercase. You may also assume the argument to the function will be in lowercase entirely.

If no matching words are found, the function should return an empty list.

Hint: the Pythons string methods startswith() and endswith() may be useful here. You can search for more information about them online.

An example of the function in action:

```python
print(find_words("*vokes"))
```

```markdown
['convokes', 'equivokes', 'evokes', 'invokes', 'provokes', 'reinvokes', 'revokes']
```
