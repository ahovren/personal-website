from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'temporary_secret_key'

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# About Me route
@app.route('/about')
def about():
    return render_template('about.html')

# Portfolio route
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

# Skills route
@app.route('/skills')
def skills():
    return render_template('skills.html')

# Contact route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            flash('Please fill out all fields.', 'error')
            return redirect(url_for('contact'))

        # Here, you could add logic to send the message via email or save it to a database.
        flash('Thank you for your message!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
