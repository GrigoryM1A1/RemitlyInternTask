# Remitly Intern Task
## Simple AWS policy verifier <br>
Repository contains:
- demo program and instruction how to run it in `main.py`
- policy_verification package which contains main parts of the task which are:
  - PolicyVerifier class with crucial `verify` method which returns true/false value
  - PolicyReaderService class
- unit tests for classes and methods from policy_verification package


Some assumptions I made because task was very general in my opinion:
- If "Statement" is of type list and there is at least one statement in the list with "Resource": "*" False is returned
- If file doesn't have a proper structure an error is raised and printed in terminal and no boolean value is returned
- By proper structure I mean (based on documentation):
  - JSON contains keys: "PolicyName" and "PolicyDocument"
  - PolicyDocument contains keys: "Version" and "Statement"
  - Statement is either a list of documents or a single document
  - If a single statement doesn't have "Resource" key then True is returned
- If an error occurred with loading the json file then proper error is raised and no boolean value is returned

## Requirements
Python 3.11 installed

## How to run demo program
- I assume that requirements are fulfilled. If on Widows use `python` and on Linux/MAC use `python3`
  when writing every command below.
- Create virtual environment <br> `python -m venv venv`
- Activate the environment
  - Windows: <br>`.\venv\Scripts\activate`
  - Linux/MAC: <br>`source venv/bin/activate`
- Navigate to `/RemitlyInternTask/src/main`
- In the terminal run <br> `python main.py`
- The program demo now will ask you to pass an absolute path to the policy json file and
  all you have to do is pass the path you want and click `Enter`. <br>
  - If error occurs it will be printed to the terminal and False will be returned. <br>
  - If json doesn't fulfill requirements False will be returned and printed. <br>
  - If verification was successful True will be returned and printed.

## Author
- Grzegorz Piśkorski