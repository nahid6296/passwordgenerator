from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# Password generator function
def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    upper = string.ascii_uppercase if use_uppercase else ""
    lower = string.ascii_lowercase if use_lowercase else ""
    digits = string.digits if use_digits else ""
    symbols = string.punctuation if use_symbols else ""

    if not (upper or lower or digits or symbols):
        return "Error: Select at least one character type"

    all_characters = upper + lower + digits + symbols
    password = [random.choice(upper), random.choice(lower), random.choice(digits), random.choice(symbols)]
    
    while len(password) < length:
        password.append(random.choice(all_characters))
    
    random.shuffle(password)
    return ''.join(password)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['length'])
    use_uppercase = 'uppercase' in request.form
    use_lowercase = 'lowercase' in request.form
    use_digits = 'digits' in request.form
    use_symbols = 'symbols' in request.form

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
