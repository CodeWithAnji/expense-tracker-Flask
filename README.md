# Personal Expense Tracker

A simple web application built with **Flask**, **MySQL**, and **Chart.js** to track personal expenses. Users can add, view, and delete expenses, as well as see a pie chart of expenses by category.


## Features

- Add new expenses with title, amount, category, and date.
- View all expenses in a table.
- Delete expenses.
- Visualize expenses by category using a pie chart.
- Fully responsive and easy-to-use interface.


## Technologies Used

- **Backend:** Python, Flask, Flask-SQLAlchemy  
- **Database:** MySQL  
- **Frontend:** HTML, CSS, JavaScript, Chart.js  
- **Template Engine:** Jinja2  


## Installation

1. **Clone the repository:**

git clone https://github.com/your-username/personal-expense-tracker.git

2. **Create a virtual environment and activate it:**

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3.  **Install dependencies:**

pip install flask flask_sqlalchemy mysql-connector-python

4.  **Create MSQL database:**

   CREATE DATABASE expense_db

5. **Run the Flask application**

python app.py

6. **Open with live server at index.html**
   

