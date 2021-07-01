import flask
from flask import request, jsonify, render_template
import sys
sys.path.insert(1, './platforms')
import leetcode
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/api/<platform>/<username>', methods=['GET'])
def api_all(platform, username):
    if platform == 'codechef':
        return get_codechef_details(username)
    elif platform == 'leetcode':
        return jsonify(leetcode.get_leetcode_details(username))
    elif platform == 'hackerrank':
        return get_hackerrank_details(username)
    elif platform == 'codeforces':
        return get_codeforces_details(username)
    elif platform == 'atcoder':
        return get_atcoder_details(username)
    elif platform == 'interviewbit':
        return get_interviewbit_details(username)
    elif platform == 'geeksforgeeks':
        return get_gfg_details(username)
    else:
        return render_template('error.html')

app.run()
