from flask import Flask, request #import main Flask class and request object

app = Flask(__name__) #create the Flask app

@app.route('/query-example')
#def query_example():
#    return 'Todo...'
def query_example():
    language = request.args.get('language') #if key doesn't exist, returns None

    return '''<h1>The language value is: {}</h1>'''.format(language)

@app.route('/form-example')
def form_example():
    return 'Todo...'

@app.route('/json-example', methods=['POST']) #GET requests will be blocked
def json_example():
    req_data = request.get_json()
    print("request_Data",req_data)
    language = req_data['language']
    framework = req_data['framework']
    python_version = req_data['version_info']['python'] #two keys are needed because of the nested object
    example = req_data['examples'][0] #an index is needed because of the array
    boolean_test = req_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)


if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000