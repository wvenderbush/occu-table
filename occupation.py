#!/usr/bin/python
import random
from flask import Flask, render_template


#Winston Venderbush
#9/22/16

app = Flask(__name__) 


@app.route("/")
def root():
	return render_template('redir.html', title = "Redirect")

@app.route("/occupations")
def randSelect():
	f = open("occupations.csv", "r")
	d = {}
	flag = False

	for line in f:
		if flag == False:
			flag = True
		else:
			ind = line.rfind(',');
			rem = line[:ind]
			link = line[ind+1:]
			#print(rem)
			ind = rem.rfind(',');
			key = rem[:ind]
			val = rem[ind+1:]
			val = float(val)
			lst = []
			lst.insert(0, val)
			lst.insert(1, link)
			d[key] = lst
	d.pop(key)
	f = random.random() * 100
	randJob = "";
	percentctr = 0.0
	for key in d:
		if f < percentctr + d[key][0]:
			randJob = key
			jlink = d[key][1]
			break
		else:
			percentctr += d[key][0]
	return render_template('sample.html', title = "Occu-table", collection = d, job = randJob, link = jlink)


if __name__ == "__main__":
    app.debug = True 
    app.run()
