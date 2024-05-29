from flask import Flask, url_for, redirect  #import the class

app = Flask(__name__) #create object of the class

@app.route('/') #decorate defines the route
def hello():
    return "<h1> My first Flask Program </h1>"

@app.route('/sasa')
def salamu():
    return "<p> Habari gani?</p>"

#app routing - map to specific url with associated function

@app.route('/about')
def about():
    return "<h1> ABOUT US PAGE </h1>"

#valuable rules

@app.route('/user/<username>')
def showUser(username):
    return f'GOOD AFTERNOON, my name is {username}'

#pass int
@app.route('/about/<int:user_id>')
def showId(user_id):
    return f'Your User ID is, %d"%user_id'

# add us=rl_rule()
# add url_rule(<url rule, <endpoint>, <veiw function>)
def profile():
    return 'This is the way'

app.add_url_rule('/profile' , "profile",profile)

## building url
#url for()...dynamic building
@app.route('/director')
def director():
    return "<h1> THE DIRECTOR </h1>"

@app.route('/teacher')
def techer():
    return "<h1> THE TEACHER </h1>"

@app.route('/student')
def student():
    return "<h1> THE STUDENT </h1>"

@app.route('/personnel/<name>')
def personnel(name):
    if name ==  'director':
        return redirect(url_for('director'))
    if name ==  'teacher':
        return redirect(url_for('teacher'))
    if name ==  'student':
        return redirect(url_for('student'))



if __name__ == '__main__':
    app.run(debug =True)
