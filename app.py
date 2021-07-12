import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
  return "Bienvenido  a mi nueva app!!!"
  
@app.route('/como estas')
def hola():
  return 'Estoy bien, gracias'
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)
