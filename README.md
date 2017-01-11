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

This got me curious about what a normal breakdown is among characters so I wanted to compare it. I chose an equally important document to history, the Declaration of Independence (ok, maybe not equally), and show the breakdown below as a percentage of the total text.
This code can be found in fileparsey.py as well. The character usage is actually quite similar, with by far the biggest % difference being on H which Mr. Thomas Jefferson used almost 3x as much as me (The "We hold these truths to be self-evident" sentence alone contains 25% of the total H's I have).

![resume_dec](https://cloud.githubusercontent.com/assets/17169813/21834467/59598f84-d783-11e6-9f44-c10b584e906d.png)

## Friendly Competition
I downloaded the file from the link to a google sheet (I don't have Excel on my laptop), removed some of the information that wasn't needed, and made some calculations to annualize all of the salary's based off the average of the range. I then loaded that data into a Django database. It could have been done (probably quicker) in Google Sheets/Excel given it was only about 4,000 rows but I wanted to use some SQL anyway. I ran them in the command line but included below.

1. The DEPT OF HEALTH/MENTAL HYGIENE has 1,294 jobs open, 2.6x as many as the DEPT OF ENVIRONMENT PROTECTION which comes in 2nd place.
```
SELECT ID, COUNT(agency)as total 
  FROM workmarket_jobs 
  GROUP BY agency 
  ORDER BY total DESC LIMIT 5"
```

2. The OFFICE OF COLLECTIVE BARGAINING has a low salary of $17,920 and the DEPT OF ENVIRONMENT PROTECTION has a high of $198,518, both annually.
I ran the below for MIN and then for MAX as I don't particularly like joining those two on the same table.
```
SELECT ID, agency, MIN(salary) 
FROM workmarket_jobs
```

3. The DEPT OF CITYWIDE ADMIN SVCS has had a Graphic Artist job that was posted in 2011 so surely that must be the hardest one to fill! But it also hasn't been updated since the posting date so I think someone forgot about it.

For this, I wanted to examine the longest difference between a job being posted and when the posting was updated, which signals to me that a new hire is being actively searched for and not found. I queried for the roles that had >= a year from original post and updated one, which gave me 50 results. I could look through these and see that many had comparably higher salaries (20% of the 50 over $99k vs a $72k average overall jobs) and advanced degree requirements (lawyers, doctors, chemists, financial, etc). 

```
SELECT ID, agency, (posting_date - post_updated) as total, salary 
  FROM workmarket_jobs 
  GROUP BY ID
  WHERE total <= -1 
  ORDER BY total DESC"
```

