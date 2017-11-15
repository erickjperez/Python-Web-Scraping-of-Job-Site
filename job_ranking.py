"""
Erick Perez
COMP 305:02
Due Date: 9-13-17
Project 1: Web Scraping
Description: python3 program that scrapes data from job ranking website and displays two lists:
	order by rank and alphabetical order
"""

import os
import re
import operator

class Jobs(object):
	job = ""
	rank = ""

	def __init__(self, job,rank):
		self.job = job
		self.rank = rank
def make_job(job, rank):
	job_object = Jobs(job,rank)
	return job_object


#lynx used to scrape webpages and put it in jobs.txt
os.system('lynx -dump -nolist http://www.careercast.com/jobs-rated/2017-jobs-rated-report '
		'-dump -nolist http://www.careercast.com/jobs-rated/2017-jobs-rated-report?page=1 '
		'-dump -nolist http://www.careercast.com/jobs-rated/2017-jobs-rated-report?page=2 '
		'-dump -nolist http://www.careercast.com/jobs-rated/2017-jobs-rated-report?page=3 '
		'-dump -nolist http://www.careercast.com/jobs-rated/2017-jobs-rated-report?page=4 '
		'-dump -nolist http://www.careercast.com/jobs-rated/2017-jobs-rated-report?page=5 '
		'-dump -nolist http://www.careercast.com/jobs-rated/2017-jobs-rated-report?page=6 '
		'-dump -nolist http://www.careercast.com/jobs-rated/2017-jobs-rated-report?page=7 '
		'-dump -nolist http://www.careercast.com/jobs-rated/2017-jobs-rated-report?page=8 '
		'-dump -nolist http://www.careercast.com/jobs-rated/2017-jobs-rated-report?page=9 '
		'> jobs.txt')

f = open('jobs.txt',  errors='ignore')
lines =  f.readlines()

#2. Rids the file of everything before the first job listing
while lines:
	line = lines[0]
	if '1. Statistician' not in line:
		del lines[0]
	else:
		break


#3 Trims end of file after last job ranking is found
jobrankings = []

while True:
	jobrankings.append(lines[0])
	del lines[0]
	if '200. Newspaper Reporter' not in lines[0]:
		continue
	else:
		jobrankings.append(lines[0])
		break
"""
From whats left, a regular expression only pulls text that is a number followed
	by a period and then a space and a capital letter and whatever follows
Splits what's found by regex based on period and stores as object attributes which
	are then added to the new list
"""
rankings = list()
for jobranking in jobrankings:
	job = re.search(r'(\d+[.][ ](?P<job>[A-Z][A-Za-z\t.]+..+))', jobranking)
	if job:
		gotIt = job.group(1)
		rank,title  = gotIt.split(".")
		title = title[1:]
		temp = make_job(title, rank)
		rankings.append(temp)


print("In Order By Ranking")
for ranking in rankings:
	print("%s. %s" % (ranking.rank,ranking.job))
print("----------------------------------------------------------")
#uses built in function to sort the list by a specified attribute
print("In Alphabetical Order")
rankings.sort(key = operator.attrgetter('job'))
for ranking in rankings:
	print("%s. %s"% (ranking.rank, ranking.job))
