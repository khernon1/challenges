import string
from string import strip, rstrip
import itertools
import collections
import pdb
import plotly.plotly as py
import plotly.graph_objs as go

# break down into multiple formulas with __init__

myfile = open("resume.txt", "r")
# reads file in as a list separated by line
lines = myfile.readlines()
# remove line breaks
lines3 = map(strip, lines)
# convert to one string and remove punctuation
str_line = ''.join(lines3).lower().translate(None, string.punctuation)

# get sorted, uniq values in text and remove all whitespace
uniq_merged = sorted(set(str_line.translate(None, string.whitespace)))

# create dict of letter and count
char_dict = collections.OrderedDict()
for char in uniq_merged:
  char_dict[char] = str_line.count(char)

# pdb.set_trace()
data = [go.Bar(
          x=char_dict.keys(),
          y=char_dict.values()
  )]
py.plot(data, filename='basic-bar')

  


  # merged.count('a')
  
  # iterate through the sorted(set(merged)) and count the existence 
  # of each char in the total merged

# where do i place this logic