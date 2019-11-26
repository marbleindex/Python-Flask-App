import requests
import json

# class to make API calls and process input

class Trivia(object):
	def __init__(self, trivia_question="", trivia_correct_answer="",category="", answer=True):
		self.trivia_question = trivia_question
		self.trivia_correct_answer = trivia_correct_answer
		self.category = category
		self.answer = answer


# function to call API based on category selected
	def categorytrivia(self,category):

		response = requests.get('https://api.fungenerators.com/trivia/random?category='+ str(category),
		headers={'X-FunGenerators-Api-Secret': 'vxMlxI9lADxza7qB8tEDoweF'})
																								
		response_data = response.json()


		trivia_question  = response_data['contents'][0]['question']
		trivia_correct_answer = response_data['contents'][0]['answer'][0]

		# return response_data
		return trivia_question, trivia_correct_answer
		# print("Your question is: " + trivia_question + "?")
		# print("The correct answer is: " + trivia_correct_answer)

# function to call API based on random category

	def randomtrivia(self):

		response = requests.get(
		'https://api.fungenerators.com/trivia/random',
		headers={'X-FunGenerators-Api-Secret': 'vxMlxI9lADxza7qB8tEDoweF'})
																							
		response_data = response.json()

		# trivia_question  = response_data['contents'][0]['question']
		# trivia_correct_answer = response_data['contents'][0]['answer'][0]
		
		return response_data

		# print("Your question is: " + trivia_question + "?")
		# print("The correct answer is: " + trivia_correct_answer)

#function to validate player answer against correct answer.

	def validatetrivia(answer, trivia_correct_answer):

		if answer == trivia_correct_answer:
			answer = True
			return answer

		elif answer != trivia_correct_answer:
			answer = False
			return answer



		
# q1 = Trivia()

# q1.categorytrivia("sports")