from flask import Flask as FL

# Create FL obj
application = FL(__name__)

# URL for routing
@application.route('/')
# Homepage
def home():
    return "Tan.com testpage"

@application.route('/contact/')
# Contact page
def contact():
    return "tjai8597@gmail.com"



# __main__ means script being executed is current file
if __name__ == "__main__":
    application.run(debug=True)