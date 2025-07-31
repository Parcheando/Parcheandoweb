from flask import Flask, render_template

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

@app.route("/")
def home():
    return render_template("home.html", data=data)

@app.route("/<empresa>/<heroe>/<anio>")
def mostrar_comics(empresa, heroe, anio):
    comics = data.get(empresa, {}).get(heroe, {}).get(anio, [])
    return render_template("comics.html", empresa=empresa, heroe=heroe, anio=anio, comics=comics)

if __name__ == "__main__":
    app.run()
