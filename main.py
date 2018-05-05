from flask import Flask, render_template, request, jsonify
import aiml
import os

#bot kernel srarts here

kernel = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
	kernel.bootstrap(brainFile = "bot_brain.brn")
else:
	kernel.bootstrap(learnFiles = os.path.abspath("source/standard/std-startup.xml"), commands = "load aiml b")
	kernel.saveBrain("bot_brain.brn")
	
#*****************************************
		
#kernel is ready to use

#bot Info***********************
BOT_INFO = {
    "name": "Jarvis",
    "birthday": "April 27, 2018",
    "location": "Jhansi",
    "master": "Shazman Malik, Harsh Malik, Abhishek Gupta, Suraj Kamal",
    "website":"",
    "gender": "Male",
    "age": "0 year",
    "size": "",
    "religion": "Humanity",
    "party": "All night !"
}
for key,val in BOT_INFO.items():
	kernel.setBotPredicate(key,val)
#**************************

#Its returns response of questions

def answer(msg):
	bot_response = kernel.respond(msg)
	return bot_response
	
#*************************************

#flask starts here


application = app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
	message = str(request.form['messageText'])
	while True:
	    if message == "quit":
	        exit()
	    elif message == "save":
	        kernel.saveBrain("bot_brain.brn")
	    else:
	        bot_response = answer(message)  
		return jsonify({'status':'OK','answer':bot_response})

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
