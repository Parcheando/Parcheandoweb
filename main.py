from flask import Flask, render_template
from models import Comic

app = Flask(__name__)

# Datos simulados (futuros datos de BD)
data = {
    "Marvel": {
        "Spider-Man": {
            "2020": ["Comic #1", "Comic #2", "Comic #3"],
            "2021": ["Comic #4", "Comic #5"]
        },
        "Captain America": {
            "2021": ["Comic #6", "Comic #7"]
        }
    },
    "DC": {
        "Batman": {
            "2020": ["Comic #8", "Comic #9"],
            "2022": ["Comic #10"]
        },
        "Superman": {
            "2021": ["Comic #11"]
        }
    }
}

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
    return render_template("home.html", data=data)

@app.route('/<empresa>/<heroe>/<anio>')
def mostrar_comics(empresa, heroe, anio):
    comics_filtrados = [
        c for c in comics
        if c.empresa.lower() == empresa.lower()
        and c.heroe.lower() == heroe.lower()
        and c.anio == anio
    ]
    return render_template("comics.html", comics=comics_filtrados, empresa=empresa, heroe=heroe, anio=anio)

if __name__ == "__main__":
    app.run()
