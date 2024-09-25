# Jason Chao
# SoftDev
# The Flying Mice
# K08 - Flask Teardown
# 2024 - 9 - 23
# Time spent: 0.5 hours

'''
DISCO:
 - __name__ is a variable built into Python that gives the name of the current active module, whether it be main or some other Python module.
 - $python3 -m venv [name] to make a Python virtual environment
 - $. path/to/env/bin/activate to activate the environment
 - $deactivate to leave the environment

QCC:
0. Initializing an object of a specific class in Java.
1. The "/" is the root directory in the terminal.
2. This print statement will print in the terminal.
3. It will print "__main__".
4. This will appear in a webpage, because the link is provided when the file is run in the terminal.
5. This is a function call in most languages like Java and C.
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
I first interpreted the program, then ran it in the terminal to see its output. Then, I used the knowledge
I got from both actions to answer the questions.
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?
