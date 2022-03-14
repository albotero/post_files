#! /usr/bin/env python3

import os
import requests

feedback_dir = '/data/feedback/'
url_post = 'http://34.72.204.110/feedback/'
keys = ('title', 'name', 'date', 'feedback')

def process_file(file):
   entry = {}
   with open(feedback_dir + file, 'r') as f:
      for key in keys:
         entry[key] = f.readline().strip()
      f.close()
   return entry

def post_data(data):
   print('Sending feedbacks', end = '... ')
   try:
      resp = requests.post(url_post, data)
      code = resp.status_code
      if code >= 200 and code < 300:
         #Success response
         print('OK')
      else:
         print('ERROR, status code {}'.format(code))
   except Exception as e:
      print(e)

def main():
   for file in os.listdir(feedback_dir):
      data = process_file(file)
      post_data(data)

main()
