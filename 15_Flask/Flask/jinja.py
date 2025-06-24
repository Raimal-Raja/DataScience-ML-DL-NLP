from flask import Flask, render_template, request


## WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    # return '<html><H1>Welcome to the flask app<H1><html>'
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method =='POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')
## variable rule
@app.route('/success/<int:score>')
def success(score):
    # return 'The marks you got is '+ str(score)
    res = ''
    if score>=50:
        res= 'Pass'
    else:
        res = "Fail"
        
    return render_template('result.html', result=res)
        


if __name__ =='__main__':
    app.run(debug=True)
