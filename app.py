from flask import Flask, render_template, jsonify

app = Flask(__name__)

## Simulate a database:
JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Kinshasa, Congo',
    'salary': '$2500'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Kinshasa, Congo',
    'salary': '$2500'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'San francisco, USA',
    'salary': '$2500'
}, {
    'id': 4,
    'title': 'Statistician',
    'location': 'Rome, Italy',
    'salary': '$2500'
}]


@app.route('/')
def hello_world():
  ## If you want to return the html file, use:
  return render_template('home.html', jobs=JOBS, company_name='Jeremie')
  #return 'Salut, Jeremie!'

  ## We can also use json to return some dynamic data, use the helper function jsonify. Create a new function


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  #print("Im inside if")
  ## You can also use the following code
  app.run(host='0.0.0.0', debug=True)
