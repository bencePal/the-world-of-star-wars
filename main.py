from flask import Flask, render_template, request, session, redirect, url_for, escape
from werkzeug.security import generate_password_hash, check_password_hash
import data_manager
import queries

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    title = 'Star Wars universe planets'
    logged_in = False
    username = ''

    if 'username' in session:
        username = escape(session['username'])
        logged_in = True

    if request.args.get('page') and request.args.get('page') != 'None':
        page_id = request.args.get('page')
    else:
        page_id = 1

    all_data = data_manager.parse_planets_data(page_id)

    response = all_data['response']
    result_list = all_data['result_list']
    prev_page_id = all_data['prev_page_id']
    next_page_id = all_data['next_page_id']

    if request.method == 'POST':
        user_id = request.json['userId']
        planet_id = request.json['planetId']
        queries.insert_vote(planet_id, user_id)

    return render_template('index.html', result_list=result_list,
                           prev_page_id=prev_page_id, next_page_id=next_page_id,
                           username=username, logged_in=logged_in, title=title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Login Page'
    error_message = False
    if request.method == 'POST':
        request_username = request.form['username']
        request_password = request.form['password']
        if queries.get_userdata(request_username) != []:
            query_username = queries.get_userdata(request_username)[0][0]
            query_password = queries.get_userdata(request_username)[0][1]
            if request_username == query_username and check_password_hash(query_password, request_password):
                session['username'] = request_username
                return redirect(url_for('home_page'))
            else:
                error_message = 'Wrong password'
                return render_template('form_page.html', title=title,
                                       request_username=request_username, error_message=error_message)
        else:
            error_message = 'This username doesn\'t exist'
            return render_template('form_page.html', title=title,
                                   request_username=request_username, error_message=error_message)
    return render_template('form_page.html', title=title)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    title = 'Registration Page'
    error_message = False
    if request.method == 'POST':
        request_username = request.form['username']
        request_password = request.form['password']
        if len(request_username) < 4 or len(request_password) < 4:
            error_message = 'Please fill out the fields (min. 4 character length)'
            return render_template('form_page.html', title=title,
                                   request_username=request_username, error_message=error_message)
        elif queries.get_userdata(request_username) != []:
            error_message = 'This username is already in use'
            return render_template('form_page.html', title=title,
                                   request_username=request_username, error_message=error_message)
        else:
            hashed_pw = generate_password_hash(request_password, method='pbkdf2:sha256', salt_length=8)
            queries.save_user(request_username, hashed_pw)
            session['username'] = request_username
            return redirect(url_for('home_page'))
    return render_template('form_page.html', title=title)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home_page'))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(debug=True)
