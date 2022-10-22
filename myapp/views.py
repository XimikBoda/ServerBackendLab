from flask import jsonify, request

from myapp import app

@app.route("/test")
def test():
    return "<p>Test page</p>"

