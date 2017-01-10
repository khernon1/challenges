import string
from string import strip, rstrip
import collections
import pdb
import plotly.plotly as py
import plotly.graph_objs as go

# break down into multiple formulas with __init__
# add legend to chart
# break it down into percentages and compare to other documents?

class ParseFiles():

  def __init__(self):
    self.resume_char_dict = collections.OrderedDict()
    self.dec_char_dict = collections.OrderedDict()
    self.resume()
    self.declaration()
    self.compare_and_build_charts()

  def resume(self):
    myfile = open("resume.txt", "r")
    # reads file in as a list separated by line
    all_lines = myfile.readlines()
    # remove line breaks
    lines_no_breaks = map(strip, all_lines)
    # convert to one string and remove punctuation
    merged = ''.join(lines_no_breaks).lower().translate(None, string.punctuation)
    # get sorted, unique values in text without spaces
    uniq_merged = sorted(set(merged.translate(None, string.whitespace)))
    # create dict of letter and count
    
    for char in uniq_merged:
      self.resume_char_dict[char] = merged.count(char)

  def declaration(self):    
    myfile = open("declaration.txt", "r")
    all_lines = myfile.readlines()
    lines_no_breaks = map(strip, all_lines)
    merged = ''.join(lines_no_breaks).lower().translate(None, string.punctuation)
    uniq_merged = sorted(set(merged.translate(None, string.whitespace)))    
    
    for char in uniq_merged:
      self.dec_char_dict[char] = merged.count(char)

  def compare_and_build_charts(self):
    # bar chart for just the resume
    resume_data = [go.Bar(
          x=self.resume_char_dict.keys(),
          y=self.resume_char_dict.values(),
          name='Resume'
    )]
    # py.plot(resume_data, filename='resume-bar')
    
    # add up the count in the values of each dict
    # iterate through and get %
    # chart percentages
    resume_total = sum(self.resume_char_dict.values())
    resume_percents = collections.OrderedDict()
    for k,v in self.resume_char_dict.items():
      resume_percents[k] = round(v/float(resume_total) * 100,2)

    dec_total = sum(self.dec_char_dict.values())
    dec_percents = collections.OrderedDict()
    for k,v in self.dec_char_dict.items():
      dec_percents[k] = round(v/float(dec_total) * 100,2)

    resume_data = go.Bar(
          x=resume_percents.keys(),
          y=resume_percents.values(),
          name='Resume (%)'
    )

    dec_data = go.Bar(
          x=dec_percents.keys(),
          y=dec_percents.values(),
          name='Declaration (%)'
    )

    data = [resume_data, dec_data]
    layout = go.Layout(
          barmode='group'
    )

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='stacked-bar')


ParseFiles()

