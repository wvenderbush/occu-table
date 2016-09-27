#!/usr/bin/python
import random
from utils import occupation
from flask import Flask, render_template


#Winston Venderbush
#9/22/16

app = Flask(__name__) 


@app.route("/")
def root():
	return render_template('redir.html', title = "Redirect")

@app.route("/occupations/")
def occupations():
	randJob = occupation.getJob()
	jlink = occupation.getLink()
	d = occupation.getCollection()
	return render_template('sample.html', title = "Occu-table", collection = d, job = randJob, link = jlink)


if __name__ == "__main__":
    app.debug = True 
    app.run()
