from flask import Flask, jsonify, redirect, render_template, request
import datetime


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
def do_shop():
    #print("method", request.method)
    if request.method == 'GET':
        #print("args", request.args)
        return render_template("shop.html",
                               id = request.args.get("id"),
                               wrap = request.args.get("wrap")
                        )
    elif request.method == 'POST':
        #print("form", request.form)
        id_text = request.form["id_text"]
        wrap_choice = request.form["wrap_choice"]
        color_choice = request.form["color_choice"]
        start_text = request.form["start_text"]

        if start_text == "":
            start_text = "start_at_%s" %(datetime.datetime.now().strftime("%Y/%m/%d_%H:%M:%S"))

        output_content = {
            "data": {
                "link": "http://www.google.com/search?q=%s" %(id_text)
            }
        }
        return render_template("shop.html",
                                id = id_text,
                                wrap = wrap_choice,
                                color = color_choice,
                                start = start_text,
                                output_content = output_content,
                        )
    else:
        return "unsupported method %s" %(request.method)


