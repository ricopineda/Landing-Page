from flask import Flask, render_template  
                                          
app = Flask(__name__)                     
                                          
@app.route('/')                           
                                          
def my_portfolio():
  return render_template('index.html')    


@app.route('/ninjas')                           
                                          
def my_projects():
  return render_template('ninjas.html') 

@app.route('/dojos')                           
                                          
def about_me():
  return render_template('dojos.html') 

app.run(debug=True)