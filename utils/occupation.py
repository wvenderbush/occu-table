#!/usr/bin/python
import random
from flask import Flask, render_template


#Winston Venderbush
#9/22/16

link = "";
d = {};

def getLink():
	return link

def getCollection():
	return d

def getJob():
	f = open("data/occupations.csv", "r")
	global d
	global link
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
	return randJob


