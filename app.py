from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# MySQL Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:anji2004@localhost/expense_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Expense {self.title}>'

# Home route
@app.route('/')
def index():
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    return render_template('index.html', expenses=expenses)

# Add expense
@app.route('/add', methods=['POST'])
def add_expense():
    title = request.form['title']
    amount = float(request.form['amount'])
    category = request.form['category']
    date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()

    new_expense = Expense(title=title, amount=amount, category=category, date=date)
    db.session.add(new_expense)
    db.session.commit()
    return redirect('/')

# Delete expense
@app.route('/delete/<int:id>')
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect('/')

# Chart data
@app.route('/chart-data')
def chart_data():
    expenses = Expense.query.all()
    data = {}
    for exp in expenses:
        if exp.category in data:
            data[exp.category] += exp.amount
        else:
            data[exp.category] = exp.amount
    return jsonify(data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if not exist
    app.run(debug=True)
