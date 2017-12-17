# coding: utf8

from flask import Flask, render_template

app = Flask(__name__)

# Basic route to server the graph
@app.route('/')
def index():
    return render_template('graph.html')

if __name__ == '__main__':
    app.run()
