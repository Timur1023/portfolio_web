# # -*- coding: utf-8 -*-
# """
# Created on Sat Nov 27 19:24:37 2021

# @author: Tymur
# """

# from flask import Flask, render_template,request, redirect
# import csv

# app = Flask(__name__)

# @app.route("/")
# def main():
#     return render_template('index.html')

# @app.route("/<string:file>")
# def all_url_rendering(file):
#     return render_template(file)

# def write_to_csv(data):
#     with open('database.csv', newline='', mode='a') as database2:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         csv_writer.writerow([email,subject,message])

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#       try:
#         data = request.form.to_dict()
#         write_to_csv(data)
#         return redirect('/index.html')
#       except:
#         return 'did not save to database'
#     else:
#       return 'something went wrong. Try again!'
from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
  with open('database.txt', mode='a') as database:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database3.csv', newline='', mode='a') as database2:
        # Извлекаем данные из формы
        email = data["email"]
        # print(email)
        subject = data["subject"]
        message = data["message"]
        
        # Сохраняем данные в файле
        csv_writer = csv.writer(database2, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

            


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      
        data = request.form.to_dict()
        write_to_csv(data)
        return 'all have good done'
      
    # return 'did not save to database'
    else:
      return 'something went wrong. Try again!'

