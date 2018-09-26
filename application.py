import os
import requests
from flask import Flask, session, render_template, request
from flask_session import Session

app = Flask(__name__)
channel_sys =

@app.route("/")
def index():
    ## Refresh User Info
    session['username'] = ''
    session['password'] = ''
    session['id'] = ''
    return render_template("login.html")


# @app.route("/authenticate",methods=["POST"])
# def authenticate():
#     session['username'] = request.form.get("username")
#     session['password'] = request.form.get("password")
#     if '=' in session['password']:
#         return render_template("login.html",message='''Your password contains illegal symbols like "=",or "'", please try again later''')
#     else:
#         user = db.execute("SELECT * FROM users WHERE :username = username AND :password = password"
#                    ,{"username":session['username'],"password":session['password']}).fetchone()
#         if not user:
#             return render_template("login.html", message = "Wrong Password. Please try again.")
#         else:
#             session['id'] = user[0]
#             return render_template("redirect.html",
#                                   id= session['id'],
#                                   username=session['username'],
#                                   message="Congratulations! Successfully registered! ")
#
# @app.route("/register",methods=["POST"])
# def register():
#     session['username'] = request.form.get("new_username")
#     session['password'] = request.form.get("new_password")
#     session['password_check'] = request.form.get("new_password_check")
#
#     if '=' in session['password']:
#         return render_template("login.html",message='''Your password contains illegal symbols like "=", please use another one.''')
#
#     elif session['password'] == "":
#         return render_template("login.html",message='''You didn't set your password , please try again.''')
#
#     elif session['password'] != session['password_check']:
#         return render_template("login.html",message='''Re-input password differ from password, please try again.''')
#
#     else:
#         db.execute("INSERT INTO users(username,password) VALUES(:username,:password)"
#                           , {"username": session['username'], "password": session['password']})
#         db.commit()
#
#         user = db.execute("SELECT * FROM users WHERE :username = username AND :password = password"
#                          , {"username": session['username'], "password": session['password']}).fetchone()
#         session['id'] = user[0]
#         return render_template("redirect.html",
#                                id= session['id'],
#                                username=session['username'],
#                                message="Congratulations! Successfully registered! ")

# @app.route("/homepage",methods= ["GET","POST"])
# def homepage():
#     session['isbn'] = request.form.get("isbn")
#     session['title'] = request.form.get("title")
#     session['author'] = request.form.get("author")
#     if session['isbn'] != '':
#         results = (db.execute("SELECT * FROM books WHERE :isbn=isbn"
#                                  , {"isbn": session['isbn']}).fetchall())
#     elif session['title'] != '':
#         results = (db.execute("SELECT * FROM books WHERE :title=title"
#                                  , {"title": session['title']}).fetchall())
#     elif session['author'] != '':
#         results = (db.execute("SELECT * FROM books WHERE :author=author"
#                                  , {"author": session['author']}).fetchall())
#     else:
#         results = []
#     session["search_result"] = results
#     return render_template("homepage.html", username = session['username'],search_results = session["search_result"])
#
# @app.route("/information/<isbn>",methods= ["GET","POST"])
# def information(isbn):
#     # refresh newly added remarks
#     session['new_rate'] = request.form.get("new_rate")
#     session['remark'] = request.form.get("remark")
#     res = requests.get("https://www.goodreads.com/book/review_counts.json",
#                        params={"key": "B9E9ItQRTwdqwdMVAZsw", "isbns": isbn})
#     res = res.json()
#     if session['new_rate'] != None:
#         db.execute("INSERT INTO remarks(book_isbn,remarker_id,book_rate,remark_content) VALUES (:book_isbn,:remarker_id, :book_rate,:remark_content);"
#                    , {"book_isbn": isbn,
#                       "remarker_id": session['id'],
#                       "book_rate": session['new_rate'],
#                       "remark_content": session['remark']})
#         db.commit()
#     #get info from GoodReads
#         #get basic book info, and remarks for that book
#     book_info = db.execute("SELECT * FROM books WHERE :isbn=isbn"
#                           , {"isbn": isbn}).fetchall()
#     book_remarks = db.execute("SELECT username,book_rate,remark_content FROM users JOIN remarks ON users.id = remarks.remarker_id WHERE :book_isbn=book_isbn",
#                               {"book_isbn": isbn}).fetchall()
#     # Reset
#     session['new_rate'] = None
#     session['remark'] = None
#
#     return render_template("information.html",
#                            book_info = book_info[0],
#                            book_remarks=book_remarks,
#                            good_read_rate = res["books"][0]["average_rating"])

# @app.route('/api/<isbn>',methods=['GET'])
# def api_book_info(isbn):
#     book_info = db.execute("SELECT * FROM books WHERE:isbn=isbn"
#                           , {"isbn": isbn}).fetchall()
#     res = requests.get("https://www.goodreads.com/book/review_counts.json",
#                        params={"key": "B9E9ItQRTwdqwdMVAZsw", "isbns": isbn})
#     return render_template("api.html",)