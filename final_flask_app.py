from flask import Flask, render_template, request
import random
from trivia import Trivia

app = Flask(__name__)

# flask app trivia game

# homepage that asks for player to select a category or random. 
@app.route('/', methods=["GET","POST"])
def index():
    # player_name = request.args.get("query")
    
    category = request.form.get('category') 

    # print(category)
    
    return render_template('index.html')


# route if player selects random category. API call for random is initiated.The question and answer submit form is rendered in the html
@app.route('/random/', methods=["GET", "POST"])
def random():
    q1 = Trivia()
    response_data = q1.randomtrivia()
     

    q1.trivia_question  = response_data['contents'][0]['question']
    q1.trivia_correct_answer = response_data['contents'][0]['answer'][0]

    answer = request.args.get("query")
    
    return render_template('question.html', trivia_question=q1.trivia_question,trivia_correct_answer=q1.trivia_correct_answer,query=answer)


# route if player selects a category other than random. API call for category is initiated. The question and answer submit form is rendered in the html

@app.route('/categories/',methods=["GET","POST"])
def category_q():
    q1 = Trivia()
    category = request.form.get("category") 
    # print(category) 

    response_data = q1.categorytrivia(category)
    # print(response_data)
    # print(q1.trivia_question)
    # print(q1.trivia_correct_answer)


    q1.trivia_question  = response_data[0]
    q1.trivia_correct_answer = response_data[1]

    answer = request.args.get("query")
    
    return render_template('question.html', trivia_question=q1.trivia_question,trivia_correct_answer=q1.trivia_correct_answer, category=category, query=answer)

# route where user answer is validated against API call response answer. The user should be presented with conditional html based on answer.
@app.route('/validate/',methods=["GET","POST"])
def validate():
    
    answer = request.args.get("query")
    # validatetrivia(answer, trivia_correct_answer)
    # answer = True
    # answer = False

    return render_template('validatetrivia.html', query=answer)

	

# Run the app when the program starts!
if __name__ == '__main__':
    app.run(debug=True)