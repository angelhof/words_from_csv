## Test for knowledge of words in different languages

It was created for the purposes of GRE and TOEFL. However it can be used with whatever language.

Its argument should be the name of a csv file containing two header rows and 3 columns. The first one contains the words in question, the second contains the meaning in one language and the last one the meaning in another language.


Example:
```python
Do you know: abhorrent

  -- Greek   Meaning: αποτρόπαιος, αποκρουστικός
  -- English Meaning: morally, repulsive
> n
Do you know: momentous

  -- Greek   Meaning: μνημειώδης, κοσμοιστορικός
  -- English Meaning: very important
> y
Congratulations: You have found the meaning of momentous correctly 1 times
```

