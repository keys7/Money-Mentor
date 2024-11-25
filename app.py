from flask import Flask, render_template, request, redirect, url_for, jsonify
import google.generativeai as genai
import textwrap
import mysql.connector
import os
import numpy as np
import pandas as pd
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, check_password_hash
from markdown import markdown

app = Flask(__name__)

# mysql connection:-
# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_DB_PASSWORD",
    database="YOUR_DB_DATABASE_NAME"
)

cursor = db.cursor()

# Configure the Gemini API key
genai.configure(api_key='YOUR_API_KEY')

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-pro')

def generate_response(prompt):
    """
    Generates a response using the Gemini API.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {e}"

@app.route('/')
def index():
    """
    Displays the loan application form.
    """
    return render_template('index.html')

@app.route('/loan_form', methods = ['GET'])
def loan_form():
    return render_template('loan_form.html')

# Register endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    country = data.get("country")
    hashed_password = generate_password_hash(password)

    cursor.execute("INSERT INTO users (username, password, country) VALUES (%s, %s, %s)", (username, hashed_password, country))
    db.commit()

    # Redirect to the sign-in page after successful registration
    return render_template('sign_in_page.html')

@app.route('/register', methods=['GET'])
def register_in_page():
    # Here you might render a sign-in form if using HTML templates
    return render_template('register.html')

# Sign In page (display form or simulate it)
@app.route('/sign_in', methods=['GET'])
def sign_in_page():
    # Here you might render a sign-in form if using HTML templates
    return render_template('sign_in_page.html')

# Sign In endpoint
@app.route('/sign_in', methods=['POST'])
def sign_in():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result and check_password_hash(result[0], password):
        # Render the services page after successful sign-in
        return render_template('index.html')
    else:
        return jsonify({"error": "Invalid username or password"}), 401
    
@app.route('/services', methods=["GET", "POST"])
def services():
    return render_template('services.html')




@app.route('/submit_loan_form', methods=['POST'])
def submit_form():
    """
    Processes the loan application form and generates the initial prompt.
    """

    # sending the data into the MySql Server
    username = request.form.get('username')
    dependents = request.form.get('depend')
    education = request.form.get('education')
    employment = request.form.get('employment')
    income = request.form.get('income')
    loan_amount = request.form.get('loan_amount')
    loan_term = request.form.get('loan_term')
    credit_score = request.form.get('score')
    resident_assets = request.form.get('resident')
    commercial_assets = request.form.get('commercial')
    luxury_assets = request.form.get('luxury')
    bank_assets = request.form.get('bank')

    # Check if username exists in the users table
    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    user_id = user[0]

    # Insert form data into the loans table
    query = """
        INSERT INTO loans (user_id, dependents, education, employment, income, loan_amount, 
                           loan_term, credit_score, resident_assets, commercial_assets, 
                           luxury_assets, bank_assets)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = (
        user_id, dependents, education, employment, income, loan_amount, loan_term, 
        credit_score, resident_assets, commercial_assets, luxury_assets, bank_assets
    )

    cursor.execute(query, data)
    db.commit()

    # Extract form data
    name = request.form['username']
    dependents = request.form['depend']
    education = request.form['education']
    employment = request.form['employment']
    income = request.form['income']
    loan_amount = request.form['loan_amount']
    loan_term = request.form['loan_term']
    credit_score = request.form['score']
    resident_assets = request.form['resident']
    commercial_assets = request.form['commercial']
    luxury_assets = request.form['luxury']
    bank_assets = request.form['bank']

    # Generate initial prompt
    prompt = (
        f"Loan application details:\n"
        f"Name: {name}, Dependents: {dependents}, Income: {income}, Loan Amount: {loan_amount}, Loan Term: {loan_term}, "
        f"Credit Score: {credit_score}.\n"
        f"Commercial Assets: {commercial_assets}.\n"
        f"Luxury Assets: {luxury_assets}.\n"
        f"Bank Assets: {bank_assets}.\n"
        f"Should this loan application be Accepted or Rejected?, Short summary line 100 words"
    )

    # Generate response
    initial_response = generate_response(prompt)

    # Redirect to loan_chat page with initial response
    return redirect(url_for('loan_chat', initial_response=initial_response))


@app.route('/submit_financial_advice_form', methods=['POST'])
def submit_advice_form():
    """
    Processes the loan application form and generates the initial prompt.
    """

    # Extract form data
    username = request.form['Username']
    description = request.form['description']  
    country = request.form['country']
    capital_loan = request.form['capital_loan']  
    amount = request.form['amount']  
    loan_pay_month = request.form['loan_pay_month']  

    # Generate initial prompt
    prompt = (
    f"Financial advice request:\n"
    f"Name: {username}\n"
    f"Business Description: {description}\n"
    f"Country: {country}\n"
    f"Funding Type: {capital_loan} (Capital/Loan)\n"
    f"Funding Amount: {amount} USD\n"
    f"Repayment Period (if loan): {loan_pay_month} months\n\n"
    f"Based on these details, provide tailored financial advice to optimize the use of funds, "
    f"ensure financial stability, and achieve business goals effectively. Short summary line 100 words"
    )

    # Generate response
    initial_response = generate_response(prompt)

    # Redirect to loan_chat page with initial response
    return redirect(url_for('loan_chat', initial_response=initial_response))

@app.route('/submit_business_idea_form', methods=['POST'])
def submit_idea_form():
    """
    Processes the loan application form and generates the initial prompt.
    """

    # Extract form data
    username = request.form['Username']
    country = request.form['country']
    capital_loan = request.form['capital_loan']
    amount = request.form['amount']
    loan_pay_month = request.form['loan_pay_month']

    # Generate initial prompt
    prompt = (
    f"Financial advice request:\n"
    f"Username: {username}\n"
    f"Country: {country}\n"
    f"Funding Type: {capital_loan} (Capital/Loan)\n"
    f"Funding Amount: {amount} USD\n"
    f"Repayment Period (if loan): {loan_pay_month} months\n\n"
    f"Based on these details, provide tailored financial advice to optimize the use of funds, "
    f"ensure financial stability, and achieve business goals effectively. "
    f"Consider the financial landscape of {country}, analyze the repayment capacity, "
    f"and suggest strategies for both short-term sustainability and long-term growth. "
    f"Short summary line (100 words max)."
    )

    # Generate response
    initial_response = generate_response(prompt)

    # Redirect to loan_chat page with initial response
    return redirect(url_for('loan_chat', initial_response=initial_response))

@app.route('/form_financial_advice', methods=["GET", "POST"])
def form_financial_advice():
    return render_template('form_financial_advice.html')

@app.route('/form_business_idea', methods=["GET", "POST"])
def form_idea_advice():
    return render_template('form_business_idea.html')

@app.route('/loan_chat')
def loan_chat():
    """
    Displays the loan_chat interface with the initial response.
    """
    initial_response = request.args.get('initial_response', 'No response available.')
    return render_template('loan_chat.html', initial_response=initial_response)

@app.route('/ask', methods=['POST'])
def ask_question():
    """
    Handles user questions in the loan_chat.
    """
    question = request.json.get('question', '')
    response = generate_response(question)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
