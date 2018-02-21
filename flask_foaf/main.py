from flask import Flask, render_template
from rdflib import Graph
from rdflib.namespace import FOAF

app = Flask(__name__)

foaf = Graph()
foaf.parse("flask_foaf/static/rdf/foaf.rdf")


def get_me():
    res = foaf.query("""SELECT DISTINCT ?fname
                     WHERE {
                     ?me a foaf:Person .
                     ?me foaf:givenname ?fname .
                     }
                     """, initNs={"foaf": FOAF})
    return list(res)[0]

@app.route("/")
def home_page():
    return render_template("index.html",
                           me= get_me()
                           )
