=menufrom flask import Flask, render_template
from models import Comic

app = Flask(__name__)

comics = [
    Comic("Spiderman #1", "Marvel", "Spiderman", "2001", 1, "Primer número de Spiderman en 2001"),
    Comic("Spiderman #2", "Marvel", "Spiderman", "2001", 2, "Segundo número de Spiderman"),
    Comic("Batman Begins", "DC", "Batman", "2005", 1, "Batman reinicia la saga"),
    Comic("Batman: Year One", "DC", "Batman", "2005", 2, "Origen moderno del Caballero Oscuro"),
    Comic("Captain America Lives Again", "Marvel", "Captain America", "2002", 1, "Cap despierta en el siglo XXI"),
    Comic("The Winter Soldier", "Marvel", "Captain America", "2002", 2, "Bucky regresa como enemigo"),
    Comic("Iron Man Reboot", "Marvel", "Iron Man", "2010", 1, "Nueva era para Tony Stark"),
    Comic("Green Lantern Corps", "DC", "Green Lantern", "2003", 1, "Expansión del universo"),
    Comic("Wonder Woman Origin", "DC", "Wonder Woman", "2001", 1, "El origen de Diana"),
    Comic("Avengers Assemble", "Marvel", "Avengers", "2012", 1, "Los héroes se unen")
]

@app.route("/")
def home():
    empresas = list(set(comic.empresa for comic in comics))
    return render_template("menu.html", menu=menu)

def index():
    menu = {}

    for comic in comics:
        empresa = comic.empresa
        heroe = comic.heroe
        anio = comic.anio

        if empresa not in menu:
            menu[empresa] = {}
        if heroe not in menu[empresa]:
            menu[empresa][heroe] = set()

        menu[empresa][heroe].add(anio)

    # Convierte los sets a listas ordenadas
    for empresa in menu:
        for heroe in menu[empresa]:
            menu[empresa][heroe] = sorted(menu[empresa][heroe])

    return render_template("menu.html", menu=menu)    

@app.route("/<empresa>")
def por_empresa(empresa):
    heroes = list(set(comic.heroe for comic in comics if comic.empresa == empresa))
    return render_template("menu.html", heroes=heroes, empresa=empresa)

@app.route("/<empresa>/<heroe>")
def por_heroe(empresa, heroe):
    anios = list(set(comic.anio for comic in comics if comic.empresa == empresa and comic.heroe == heroe))
    return render_template("menu.html", anios=anios, empresa=empresa, heroe=heroe)
    
@app.route("/<empresa>/<heroe>/<anio>")
def por_anio(empresa, heroe, anio):
    filtrados = [comic for comic in comics if comic.empresa == empresa and comic.heroe == heroe and comic.anio == anio]
    return render_template("comics.html", comics=filtrados)
    
if __name__ == "__main__":
    app.run()
