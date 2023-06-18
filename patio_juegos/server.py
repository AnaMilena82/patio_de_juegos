from flask import Flask, render_template, url_for  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"


@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def index():
    return 'Patio de Juegos!'  

@app.route('/play')
def play():
    return render_template("play.html")

@app.route('/play/<int:x>')
def playx(x):
    return render_template("play.html",x=x)
   
@app.route('/play/<int:x>/<string:color>')
def playxcolor(x,color):
    return render_template("play.html",x=x,color=color)



@app.route('/<path:path>') #Asegúrate de que si el usuario escribe cualquier ruta distinta a las especificadas, reciba un mensaje de error que diga "¡Lo siento! No hay respuesta. Inténtalo otra vez.”.
def error(path):
    return '¡Lo siento! No hay respuesta. Inténtalo otra vez.'

    






if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

