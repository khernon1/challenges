# challenges

I completed the first two challenges on this repo for ease of viewing, with the specifics below.

## Counting Vitae

I used a Python script that can be find in the resume function of the fileparser.py file above (with comments) and Plotly for the bar chart. I put the code below as well.

```
    myfile = open("resume.txt", "r")
    all_lines = myfile.readlines()
    lines_no_breaks = map(strip, all_lines)
    merged = ''.join(lines_no_breaks).lower().translate(None, string.punctuation)
    uniq_merged = sorted(set(merged.translate(None, string.whitespace)))
    for char in uniq_merged:
      self.resume_char_dict[char] = merged.count(char)
```
![resume_char](https://cloud.githubusercontent.com/assets/17169813/21834285/ff211dbc-d781-11e6-9261-40e16d39a5d7.png)

This got me curious about what a normal breakdown is among characters so I wanted to compare it. I chose an equally important document to history, the Declaration of Independence (ok, maybe not equally), and show the breakdown below.
This code can be found in fileparsey.py as well. The character usage is actually quite similar, with by far the biggest % difference being on H which Mr. Thomas Jefferson used almost 3x as much as me (The "We hold these truths to be self-evident" sentence alone contains 11 H's while I have only 45 total).

![resume_dec](https://cloud.githubusercontent.com/assets/17169813/21834467/59598f84-d783-11e6-9f44-c10b584e906d.png)
