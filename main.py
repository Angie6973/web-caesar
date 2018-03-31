from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True

encrypt_form="""
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      
       
            <form action="/" method="post">
                 <label>
                    Rotate by: 
                    <input type="text" name="rot" value="0"/>
                 </label>
                 <textarea name="text" >{0}</textarea>
                 <input type="submit" value="Submit Query"/>
            </form>
            

    
    </body>
</html>
"""
    

@app.route("/")
def index():
   

    return encrypt_form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form["text"]
    rot=request.form["rot"]
    encrypted = rotate_string(text, int(rot))
    return encrypt_form.format(encrypted)
app.run()




