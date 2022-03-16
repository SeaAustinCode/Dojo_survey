from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "cb0ca7e0-2af2-4c3b-851c-47de5056a4e5"

@app.route('/') #starts here
def homepage():
    return render_template('index.html')

@app.route('/success') #displays the submitted form from session
def return_form():
    return render_template('success.html')

@app.route('/process', methods=['post']) #think of this as a loading state
def process():
    # if 'submit' in request.form:
    if request.form['dojo_location'] =="0": #validation stuff
        return redirect('/') #validation stuff
    session['your_name'] = request.form['your_name'] #request.for,[] needs to be name in html 
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_language'] = request.form['favorite_language']
    return redirect('/success') #brings us to another page

if __name__=="__main__":
    app.run(debug=True)