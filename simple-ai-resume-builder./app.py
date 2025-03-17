from flask import Flask, render_template, request

import os

 

app = Flask(__name__)

 

@app.route("/", methods=["GET", "POST"])

def home():

    if request.method == "POST":

        name = request.form.get("name")

        email = request.form.get("email")

        phone = request.form.get("phone")

        skills = request.form.get("skills")

        education = request.form.get("education")

        experience = request.form.get("experience")

       

        # This can be expanded to use AI tools, e.g., using OpenAI GPT for generating content

        resume = {

            "name": name,

            "email": email,

            "phone": phone,

            "skills": skills,

            "education": education,

            "experience": experience

        }

       

        return render_template("resume_template.html", resume=resume)

   

    return render_template("index.html")

 

if __name__ == "__main__":

    app.run(debug=True)