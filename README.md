# Introduction

This is a very simple Python-Flask app which can be used as a playground to try out Github Copilot, Ponicode, and CodeGuru.

Once cloned, please create a unique branch name (I suggest using your name)

---

## Install VS code extensions

Sign up for free trials, and install the VS code extension:

Github copilot: [https://github.com/features/copilot](https://github.com/features/copilot)

Ponicode: [https://www.ponicode.com/developers](https://www.ponicode.com/developers)

⚠️ **Note: Please make sure to remove these extensions once the workshop is over, as we are not necessarily allowed to use these extensions for case work!** ⚠️

---

## To run locally

```
brew install python3
pip3 install flask_sqlalchemy
pip3 install flask
python3 run.py
```

Your app will launch at [http://localhost:5000](http://localhost:5000)

---

## Things to try with Copilot & Ponicode

Some suggested very simple tasks to complete/enhance the app, which will allow you to explore Copilot's features.

- Create a new endpoint to list all products
- Create a new endpoint to delete a product by id
- Try to improve/simplify get_client_score_py(client) in functions.py
- Create unit tests for functions.py with Ponicode and play a little

## Using Ponicode

To generate unit tests using Ponicode, click inside the function body, and then select "Unit Test".

![Ponicode 1](/docs/ponicode-1.jpg)

To use one of the unit test suggestions, click the play icon (1) to run the test and generate an expected result, click the lightning icon (2) to accept this result as the value to assert in the test, then click the plus icon (3) to accept this as a unit test.

![Ponicode 2](/docs/ponicode-2.jpg)

Your tests will be generated inside the `ponicode` folder.

---

## Make a pull request to try out AWS CodeGuru

- Make sure you have created a unique branch name for your code (e.g. your name). Please avoid using slashes etc in the name - it should be URL safe!
- Commit your code and push your branch
- Run a full repo CodeGuru scan with the help of one of the facilitators
