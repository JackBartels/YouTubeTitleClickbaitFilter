#### Regular Expression YouTube Title Clickbait Filter

**Summary**

I wrote a Python program that indicates whether or not YouTube titles are clickbait. It does this by fetching YouTube's trending video webpage HTML which then gets parsed into a list of video titels. The video titles are then passed through a 3-layer regular expression filter. The layers are word, phrase, and filter.

The program also has a gold standard list generated through real person surveys against which the program's current filter quality can be evaluated, returning F-scores and their breakdowns.

**Where to find things**

Source Code: clickbaitFilter.py
Paper: RegexFilterPaper.pdf
