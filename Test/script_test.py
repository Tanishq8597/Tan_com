from flask import Flask,render_template 

# Create FL obj
application = Flask(__name__)

# URL for routing has to be followed by its function
@application.route('/')
# Homepage
def home():
    return render_template("home.html")

@application.route('/contact/')
# Contact page
def contact():
    return render_template("contact.html")



# __main__ means script being executed is current file
if __name__ == "__main__":
    application.run(debug=True)