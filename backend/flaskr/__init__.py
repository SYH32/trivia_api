import os
from flask import Flask, request, abort, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_cors import CORS
import random

from models import setup_db, Question, Category, db

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    def paginate_questions(questions):
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * 10
        end = start + 10

        formatted_questions = [question.format() for question in questions]
        return formatted_questions[start:end]

    def formatted_categories():

        categories = Category.query.order_by(Category.type).all()
        dict_categories = {category.id: category.type for category in categories}

        return dict_categories

    @app.route('/categories')
    def get_categories():

        categories = Category.query.order_by(Category.type).all()

        if len(categories) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'categories': {category.id: category.type for category in categories}
        })

    @app.route('/questions')
    def get_questions():

        questions = Question.query.order_by(Question.id).all()

        current_questions = paginate_questions(questions)
        dict_categories = formatted_categories()

        if len(current_questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(questions),
            'categories': dict_categories,
            'current_category': None
        })

    @app.route('/questions/<question_id>', methods=['DELETE'])
    def delete_question(question_id):

        try:
            Question.query.get(question_id).delete()
            db.session.commit()

            return jsonify({
                'success': True,
                'message': 'Question with ID ' + question_id + ' is deleted'
            })

        except:
            abort(422)

    @app.route('/questions', methods=['POST'])
    def create_question():
        try:
            body = request.get_json()

            question = body.get('question', None)
            answer = body.get('answer', None)
            difficulty = body.get('difficulty', None)
            category = body.get('category', None)

            if question is None or answer is None or difficulty is None or category is None:
                abort(422)

            new_question = Question(
                question=question,
                answer=answer,
                difficulty=difficulty,
                category=category
            )

            db.session.add(new_question)
            db.session.commit()

            return jsonify({
                'success': True,
                'created': "New Question Created with ID " + str(new_question.id)
            })

        except Exception as e:
            db.session.rollback()
            return jsonify({
                'success': False,
                'error': str(e),
            })

        finally:
            db.session.close()

    @app.route('/questions/search', methods=['POST'])
    def search_questions():

        body = request.get_json()
        search_term = body.get('searchTerm')

        if search_term == '' or None:
            abort(404)

        search_term = "%{}%".format(search_term)

        questions = Question.query.filter(Question.question.ilike(search_term)).all()
        current_questions = paginate_questions(questions)

        dict_categories = formatted_categories()

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(questions),
            'categories': dict_categories,
            'current_category': None

        })

    @app.route('/categories/<category_id>/questions')
    def questions_by_category(category_id):

        questions = Question.query.order_by(Question.id).filter_by(category=category_id).all()

        if not questions:
            abort(404)

        current_questions = paginate_questions(questions)
        dict_categories = formatted_categories()

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(questions),
            'categories': dict_categories,
            'current_category': category_id

        })

    @app.route('/quizzes', methods=['POST'])
    def take_quiz():

        body = request.get_json()

        if "previous_questions" not in body or "quiz_category" not in body:
            abort(422)

        previous_questions = body.get('previous_questions')
        quiz_category = body.get('quiz_category')['id']

        if quiz_category != 0:
            new_question = Question.query.filter(Question.category == quiz_category).\
                filter(Question.id.notin_(previous_questions)).order_by(func.random()).first()
        else:
            new_question = Question.query.filter(Question.id.notin_(previous_questions)).\
                order_by(func.random()).first()

        return jsonify({
            'success': True,
            'question': new_question.format() if new_question else None
        })

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not Found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable Request"
        }), 422

    @app.errorhandler(405)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method Not Allowed"
        }), 405

    return app


'''
@TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
DONE
'''

'''
@TODO: Use the after_request decorator to set Access-Control-Allow
DONE
'''

'''
@TODO: 
Create an endpoint to handle GET requests 
for all available categories.
DONE
'''

'''
@TODO: 
Create an endpoint to handle GET requests for questions, 
including pagination (every 10 questions). 
This endpoint should return a list of questions, 
number of total questions, current category, categories. 

TEST: At this point, when you start the application
you should see questions and categories generated,
ten questions per page and pagination at the bottom of the screen for three pages.
Clicking on the page numbers should update the questions. 
DONE
'''

'''
@TODO: 
Create an endpoint to DELETE question using a question ID. 

TEST: When you click the trash icon next to a question, the question will be removed.
This removal will persist in the database and when you refresh the page.
DONE
'''

'''
@TODO: 
Create an endpoint to POST a new question, 
which will require the question and answer text, 
category, and difficulty score.

TEST: When you submit a question on the "Add" tab, 
the form will clear and the question will appear at the end of the last page
of the questions list in the "List" tab.  
DONE
'''

'''
@TODO: 
Create a POST endpoint to get questions based on a search term. 
It should return any questions for whom the search term 
is a substring of the question. 

TEST: Search by any phrase. The questions list will update to include 
only question that include that string within their question. 
Try using the word "title" to start. 
DONE
'''

'''
@TODO: 
Create a GET endpoint to get questions based on category. 

TEST: In the "List" tab / main screen, clicking on one of the 
categories in the left column will cause only questions of that 
category to be shown.
DONE
'''

'''
@TODO: 
Create a POST endpoint to get questions to play the quiz. 
This endpoint should take category and previous question parameters 
and return a random questions within the given category, 
if provided, and that is not one of the previous questions. 

TEST: In the "Play" tab, after a user selects "All" or a category,
one question at a time is displayed, the user is allowed to answer
and shown whether they were correct or not. 
DONE
'''

'''
@TODO: 
Create error handlers for all expected errors 
including 404 and 422. 
DONE
'''
