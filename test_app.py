from webtest import TestApp as make_app
from server import app

app.catchall = False

testapp = make_app(app)


def test_1():
    index = testapp.get("/")
    assert "Bonjour" in index.ubody


def test_double():
    formulaire = testapp.get("/doubler")
    form = formulaire.form
    form["valeur"] = "32"
    res = form.submit()
    assert "64" in res.ubody  

def test_double_json():
    reponse = testapp.post_json("/doubler.json", {"valeur": 43} )

    assert reponse.json["double"] == 86


def test_formulaire():
    formulaire = testapp.get("/formulaire2")
    form = formulaire.form
    form["parametre1"] = "32"
    form["parametre2"] = "32"
    res = form.submit()
    assert int(res.ubody.split("<br/>")[-1]) == 64  # A remplacer


def test_formulaire_json():
    reponse = testapp.post_json("/formulaire2", {"parametre1": 43, "parametre2": 56})

    assert reponse.json["valeur"] == 43
    assert reponse.json["double"] == 86
