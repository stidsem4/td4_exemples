from bottle import Bottle, template, request

app = Bottle()


@app.route("/")
def bonjour():
    return "Bonjour !"


@app.route("/hello/<name>")
def greet(name="Stranger"):
    return template("Hello {{name}}, how are you?", name=name)


@app.get("/formulaire2")
def afficher_formulaire():
    return """
        <form action="/formulaire2" method="post">
            Texte1 <input name="parametre1" type="text" />
            Texte2 <input name="parametre2" type="text" />
            <input value="Ajouter" type="submit" />
        </form>
    """

@app.post("/formulaire2")
def traiter_formulaire():
   
    is_json = request.content_type == "application/json"
    data = request.json if is_json else request.forms

    valeur = int(data.get("parametre1"))
    double = valeur *2
    
    res = {"valeur": valeur, "double": valeur * 2}
    import ipdb
    ipdb.set_trace()
    if is_json:
        return res
    else:
        return template("{{valeur}} * 2 = <br/> {{double}}", **res)

@app.get("/doubler")
def calcul():
    return """
     <form action="/doubler" method="post">
            valeur <input name="valeur" type="text" />
        <input value="Ajouter" type="submit" />
        </form>
    """


@app.post("/doubler")
def doubler_valeur():
    data = request.forms
    valeur = int(data.get("valeur"))
    double = valeur * 2
    res = {"valeur": valeur, "double": double}
    return template("{{valeur}} * 2 = <br/> {{double}}", valeur=valeur, double=double)


@app.post('/doubler.json')
def doubler_valeur_json():
    data = request.json 
    valeur = int(data.get("valeur"))
    res = {'double': valeur*2}
    return res


@app.post("/formulaire")
def traiter_formulaire():
    valeur = request.forms.get("parametre1")
    return valeur




from bottle import static_file


@app.get("/image")
def afficher_image():
    nom_image = "logo_nav.png"
    return static_file(nom_image, root="images")


@app.get("/demo_template")
def demo_template():
    items = list(zip("abc", "123"))
    tmpl = """
    <ul>
  % for key, value in items:
    <li>{{key}}: {{ value }}</li>
  % end
    </ul>
    """
    return template(tmpl, items=items)
