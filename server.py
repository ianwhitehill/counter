from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'password'

@app.route('/')
def index():
    if not 'visits' in session:
        session['visits'] = 1
    else:
        session['visits'] = session['visits'] + 1
    return render_template("index.html", visits = session['visits'])

@app.route('/clear', methods=['POST'])
def clear():
    session.pop('visits')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
