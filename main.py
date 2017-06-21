from flask import Flask, render_template, request, Markup
import data_manager
app = Flask(__name__)


@app.route('/')
def home_page():

    # if none delete button jquery
    if request.args.get('page') and request.args.get('page') != 'None':
        page_id = request.args.get('page')
    else:
        page_id = 1

    all_data = data_manager.parse_planets_data(page_id)

    response = all_data['response']
    result_list = all_data['result_list']
    prev_page_id = all_data['prev_page_id']
    next_page_id = all_data['next_page_id']

    return render_template('index.html',
                           result_list=result_list,
                           prev_page_id=prev_page_id,
                           next_page_id=next_page_id)

if __name__ == '__main__':
    app.run(debug=True)
