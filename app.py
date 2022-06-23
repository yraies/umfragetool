from enum import Enum
from flask import Flask
app = Flask(__name__)

class Formular:
    title : str
    description : str
    question_sets: List[QuestionSet]
    
class QuestionSet:
    title : str
    description : str
    questions : Question
    
class QuestionType(Enum):
    DISCRETE_NUMERIC = 1
    CONTINUOUS_NUMERIC = 1
    SINGLE_CHOICE = 2
    MULTIPLE_CHOICE = 3
    TEXT = 4
    
class Question:
    type : QuestionType
    title : str

class DiscreteNumericQuestion(Question):
    type = QuestionType.DISCRETE_NUMERIC
    min : int
    max : int 
    stepsize : int = 1
    descriptions : dict

@app.route('/')
def hello_world():
    return 'Hello World! <p>Foo<b>Bar</b></p>'

if __name__ == '__main__':
    app.run()