#!/usr/bin/env python2
"""
Python script that prints the answers
of the following 3 questions:
Q1: What are the most popular three articles of all time?
Q2: Who are the most popular article authors of all time?
Q3: On which days did more than 1% of requests lead to errors?
based on the data from a database called: news
"""
import psycopg2
db = psycopg2.connect("dbname=news")

question1 = 'What are the most popular three articles of all time?'
# Which articles have been accessed the most?
# Present this information as a sorted list
# with the most popular article at the top.
query1 = '''
SELECT title, views FROM articles JOIN 
(SELECT path, COUNT(path) AS views FROM 
log GROUP BY path) AS log2 ON 
log2.path = concat('/article/', articles.slug)
 ORDER BY views DESC LIMIT 3;
 '''


question2 = 'Who are the most popular article authors of all time?'
#  Who are the most popular article authors of all time?
#  That is, when you sum up all of the articles each author has written,
#  which authors get the most page views?
#  Present this as a sorted list with the most popular author at the top.
query2 = '''
SELECT authors.name, COUNT(authors.id) AS views
 FROM articles JOIN authors ON articles.author = authors.id
 JOIN log ON log.path = concat('/article/', articles.slug)
 GROUP BY name ORDER BY views DESC;
 '''


question3 = 'On which days did more than 1% of requests lead to errors?'
#  On which days did more than 1% of requests lead to errors?
#  The log table includes a column status that indicates the HTTP status code
#  that the news site sent to the user's browser.
query3 = '''
SELECT time::DATE AS date2, round(access*100.0/count(status), 3)
AS num_of_access FROM log JOIN (SELECT time::DATE AS date, count(status)
AS access FROM log WHERE status LIKE '4%' GROUP BY date)
AS log2 ON log.time::DATE = log2.date GROUP BY date2,
access ORDER BY num_of_access DESC LIMIT 1;
'''
def get_results(query):
	'''Connecting to News DB and 
	fitching the results of the queries'''
	try:
		db = psycopg2.connect(database='news')
		cursor = db.cursor()
		cursor.execute(query)
		results = cursor.fetchall()
		db.close()
		return results
	except psycopg2.Error as error:
		print(error.pgerror)
		raise error

def print_results(question, result):
	'''prints the results of the
	 queries as a plain text'''
	text = '\n' + question + '\n'
	for i in range(len(result)):
		text = text + str(i+1)+') ' + str(result[i][0]) + ' -> ' + str(result[i][1]) + '\n'
	return text +"=================\n"



if __name__ == '__main__':
	result1 = get_results(query1)
	result2 = get_results(query2)
	result3 = get_results(query3)

	text1 = print_results(question1, result1)
	text2 = print_results(question2, result2)
	text3 = print_results(question3, result3)
	print text1, text2, text3

	# uncomment the following code if you 
	# want a txt copy from the results
	with open("example.txt","w") as file:
		file.write(text1)
		file.write(text2)
		file.write(text3)
