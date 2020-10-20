# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

## API Reference

#### Getting Started

- Base URL: this APP can be only run locally, the base url for the backend is http://127.0.0.1:5000/
- Authentication: This version of the application does not require authentication or API keys.

#### Error Handling

Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 404,
    "message": "Not Found"
}
```
The API will return three error types when requests fail:

- 404: Resource Not Found
- 422: Unprocessable Request
- 405: Method Not Allowed

#### Endpoints

GET /questions

- General:
    - Returns list of question objects, question categories, and total number of questions.
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.

- Sample: 
    - Request:```curl http://127.0.0.1:5000/questions```
    
    - Response: 
    ```
        {
      "categories": {
        "1": "Science", 
        "2": "Art", 
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment", 
        "6": "Sports"
      }, 
      "current_category": null, 
      "questions": [
        {
          "answer": "Apollo 13", 
          "category": 5, 
          "difficulty": 4, 
          "id": 2, 
          "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        }, 
        {
          "answer": "Tom Cruise", 
          "category": 5, 
          "difficulty": 4, 
          "id": 4, 
          "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        }, 
        {
          "answer": "Maya Angelou", 
          "category": 4, 
          "difficulty": 2, 
          "id": 5, 
          "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        }, 
        {
          "answer": "Edward Scissorhands", 
          "category": 5, 
          "difficulty": 3, 
          "id": 6, 
          "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }, 
        {
          "answer": "Muhammad Ali", 
          "category": 4, 
          "difficulty": 1, 
          "id": 9, 
          "question": "What boxer's original name is Cassius Clay?"
        }, 
        {
          "answer": "Brazil", 
          "category": 6, 
          "difficulty": 3, 
          "id": 10, 
          "question": "Which is the only team to play in every soccer World Cup tournament?"
        }, 
        {
          "answer": "Uruguay", 
          "category": 6, 
          "difficulty": 4, 
          "id": 11, 
          "question": "Which country won the first ever soccer World Cup in 1930?"
        }, 
        {
          "answer": "George Washington Carver", 
          "category": 4, 
          "difficulty": 2, 
          "id": 12, 
          "question": "Who invented Peanut Butter?"
        }, 
        {
          "answer": "Lake Victoria", 
          "category": 3, 
          "difficulty": 2, 
          "id": 13, 
          "question": "What is the largest lake in Africa?"
        }, 
        {
          "answer": "The Palace of Versailles", 
          "category": 3, 
          "difficulty": 3, 
          "id": 14, 
          "question": "In which royal palace would you find the Hall of Mirrors?"
        }
      ], 
      "success": true, 
      "total_questions": 20
        }
    ```


GET /categories

- General
    - Return list of catogray type and id objects in key:value pairs.

- Sample
    - Request: ```curl http://127.0.0.1:5000/categories```
    
    - Response: 
    ```
    {
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true
    } 
    ```

DELETE /questions/{question_id}

- General
    - Deletes the question of the given ID if it exists. 
    - Returns success value and message to conform the deleted question with it's ID.

- Sample:
    - Request: ```curl -X DELETE http://127.0.0.1:5000/questions/20```
    
    - Response: 
        ```
           {
            "message": "Question with ID 20 is deleted", 
            "success": true
           }
        ```

POST /questions

- General:
    - Creates a new question using the submitted question, answer, difficulty and category.
    - Returns success value and message to confirm the questions creation including the ID of the created question. 
    
- Sample:
    - Request: 
        ```
        curl -X POST -H "Content-Type: application/json" 
        -d '{"question":"What's the color of the sky ?","answer":"Blue", "difficulty":"1", "category":"1"}
        http://127.0.0.1:5000/questions
         ```
    
    - Response: 
        ```
        {
          "created": "New Question Created with ID 30", 
          "success": true
        }
        ```

POST /questions/search

- General:
    - Takes a string search term and retrieves all questions that includes this requested search term.
    - Returns success value, paginated result of the qualified questions, total questions and categories.
    
- Sample:
    - Request:
        ```
        curl -X POST -H "Content-Type: application/json" -d '{"searchTerm":"Which"}' http://127.0.0.1:5000/questions/search 
        ```
    -Response:
    
        ```
        {
          "categories": {
            "1": "Science", 
            "2": "Art", 
            "3": "Geography", 
            "4": "History", 
            "5": "Entertainment", 
            "6": "Sports"
          }, 
          "current_category": null, 
          "questions": [
            {
              "answer": "Brazil", 
              "category": 6, 
              "difficulty": 3, 
              "id": 10, 
              "question": "Which is the only team to play in every soccer World Cup tournament?"
            }, 
            {
              "answer": "Uruguay", 
              "category": 6, 
              "difficulty": 4, 
              "id": 11, 
              "question": "Which country won the first ever soccer World Cup in 1930?"
            }, 
            {
              "answer": "The Palace of Versailles", 
              "category": 3, 
              "difficulty": 3, 
              "id": 14, 
              "question": "In which royal palace would you find the Hall of Mirrors?"
            }, 
            {
              "answer": "Agra", 
              "category": 3, 
              "difficulty": 2, 
              "id": 15, 
              "question": "The Taj Mahal is located in which Indian city?"
            }, 
            {
              "answer": "Escher", 
              "category": 2, 
              "difficulty": 1, 
              "id": 16, 
              "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
            }, 
            {
              "answer": "Jackson Pollock", 
              "category": 2, 
              "difficulty": 2, 
              "id": 19, 
              "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
            }, 
            {
              "answer": "Scarab", 
              "category": 4, 
              "difficulty": 4, 
              "id": 23, 
              "question": "Which dung beetle was worshipped by the ancient Egyptians?"
            }
          ], 
          "success": true, 
          "total_questions": 7
        }
        ```
        
GET /categories/{category_id}/questions

- General:
    - Takes category ID and retrive all questions under that category.
    - Returns success value, paginated result of the qualified questions, total questions, categories and ID of selected category. 

- Sample:
    - Request: ``` curl http://127.0.0.1:5000/categories/6/questions ```
    
    - Response: 
       ```
        {
          "categories": {
            "1": "Science", 
            "2": "Art", 
            "3": "Geography", 
            "4": "History", 
            "5": "Entertainment", 
            "6": "Sports"
          }, 
          "current_category": "6", 
          "questions": [
            {
              "answer": "Brazil", 
              "category": 6, 
              "difficulty": 3, 
              "id": 10, 
              "question": "Which is the only team to play in every soccer World Cup tournament?"
            }, 
            {
              "answer": "Uruguay", 
              "category": 6, 
              "difficulty": 4, 
              "id": 11, 
              "question": "Which country won the first ever soccer World Cup in 1930?"
            }
          ], 
          "success": true, 
          "total_questions": 2
        }
       ``` 
    
POST /quizzes

- General:
    - Takes list of previous question and selected category and retrieves one question from that category and not within the previous question list.
    - Returns success value, and new question. 
    
- Sample:
    - Request: 
        ``` 
        curl -X POST -H "Content-Type: application/json" -d  '{"previous_questions": [], "quiz_category": {"type": "Sports", "id": "6"}}'  
        http://127.0.0.1:5000/quizzes
        ```
      
    - Response:
        ```
        {
          "question": {
            "answer": "Brazil", 
            "category": 6, 
            "difficulty": 3, 
            "id": 10, 
            "question": "Which is the only team to play in every soccer World Cup tournament?"
          }, 
          "success": true
        }
        ```

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```