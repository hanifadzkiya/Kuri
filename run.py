from flask import Flask,request
from ciphertext import caesar_cipher,vigenere_cipher
import json

app = Flask(__name__)

@app.route('/caesarcipher',methods = ["POST"])
def get_caesar_cipher():
	plaintext = request.args["plaintext"]
	key = int(request.args["key"])
	result = {}
	result["ciphertext"] = caesar_cipher(plaintext,key)
	return json.dumps(result)

@app.route('/vigenerecipher',methods = ["POST"])
def get_vigenere_cipher():
	plaintext = request.args["plaintext"]
	key = request.args["key"]
	result = {
		"ciphertext" : vigenere_cipher(plaintext,key),
	}
	return json.dumps(result)

if __name__ == '__main__':
   app.run()
