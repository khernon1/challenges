from django.shortcuts import render
from django.http import HttpResponse
# from django.core.files import File
import string
import itertools
import collections
import pdb
import plotly.plotly as py
import plotly.graph_objs as go

def index(request):
  # data = [go.Bar(
  #           x=['giraffes', 'orangutans', 'monkeys'],
  #           y=[20, 14, 23]
  #   )]
  # py.plot(data, filename='basic-bar')

  with open("workmarket/resume.txt", "r") as myfile:      
    char_list = []
    char_dict = {}#collections.OrderedDict()
    # iterate through each line of the text file
    for line in myfile:
      #split the line and convert to lowercase
      split_line = line.lower().split()
      # combine into one line of characters and remove punctuation        
      line_to_string = ''.join(split_line).translate(None, string.punctuation)
      char_list.append(line_to_string)
      # flatten array
      merged = list(itertools.chain(*char_list))
      uniq_merged = sorted(set(merged))
    # create dict of letter and count
    for char in uniq_merged:
      char_dict[char] = merged.count(char)

  char_keys = char_dict.keys()
  char_values = char_dict.values()
  data = [go.Bar(
            x=[char_keys],
            y=[char_values]
    )]
  py.plot(data, filename='basic-bar')

  # pdb.set_trace()


  # merged.count('a')
  
  # iterate through the sorted(set(merged)) and count the existence 
  # of each char in the total merged

# where do i place this logic