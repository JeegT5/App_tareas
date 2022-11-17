from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

@app.route("/")
def home():
	
	with open("tareas") as tareas:
		tareas = json.load(tareas)
	
	return render_template("index.html", tareas=tareas["tareas"])

@app.route("/agregar", methods=["post", "GET"])
def agregar():
	if request.method == "GET":
		return render_template("agregar.html")
	else:
		with open("tareas") as tareas:
			tareas = json.load(tareas)
			
		tarea = request.form.get("tarea")
		
		tareas["tareas"].append(tarea)
		
		datos = json.dumps(tareas, indent=4)
		
		file = open("tareas", "w")
		
		file.write(datos)
		
		file.close()
		
		return redirect("/")
		
@app.route("/eliminar", methods=["post","GET"])
def eliminar():
	if request.method == "GET":
		
		return render_template("eliminar.html")
		
	else:
		
		try:
			with open("tareas") as tareas:
				tareas = json.load(tareas)
		
			tarea = request.form.get("tarea")
		
			tareas["tareas"].remove(tarea)
		
			datos = json.dumps(tareas, indent=4)
				
			file = open("tareas", "w")
		
			file.write(datos)
				
			file.close()
		
			return redirect("/")
			
		except:
			return redirect("/")
		
		