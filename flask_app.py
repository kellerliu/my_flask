from flask import Flask, jsonify, redirect, render_template, request

app = Flask(__name__)

SUPPORTED_ROUTES_DOCUMENTATION = {}

# url_map for listing supported url
@app.route('/help')
def help():
    """help page"""
    doc = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            route = rule.rule
            if route in SUPPORTED_ROUTES_DOCUMENTATION:
                doc[route] = SUPPORTED_ROUTES_DOCUMENTATION[route]
            else:
                doc[route] = "Route Usage not documented yet!!"
    return jsonify(doc)

# simple get
@app.route('/')
def hello_world():
    return 'Hello, World!'

# redirect, code 307 to preserve request method and form if needed
@app.route('/main')
def route_main():
    return redirect("/",  code=307)

# render_template for get and post methods
@app.route('/shop', methods=['GET','POST'])
def low_stock():
    if request.method == 'GET':
        return render_template("shop.html",
                               id = request.args.get("id"),
                               my_choice = request.args.get("my_choice")
                        )
    elif request.method == 'POST':
        id_text = request.form["id_text"]
        my_choice = request.form["test_choice"]
        output_content = {
            "data": {
                "link": "http://www.google.com"
            }
        }
        return render_template("shop.html",
                                id = id_text,
                                my_choice = my_choice,
                                output_content = output_content,
                        )
    else:
        return "unsupported method %s" %(request.method)


