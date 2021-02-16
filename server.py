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
        # c'est équivalent a faire template('xxxx', valeur = valeur, double = double)

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
  % for key, value in items:  #attention aux : à la fin
    <li>{{key}}: {{ value }}</li>
  % end
    </ul>
    """
    return template(tmpl, items=items)


# 16 Février

@app.get("/saisie")
def afficher_formulaire():
    return """
     <p> Dans ce formulaire saisissez une série de valeurs elle sera enregistee pour etre stockée </p>
        <form action="/saisie" method="post">
            valeurs <input name="parametre1" type="text" />
            <input value="Ajouter" type="submit" />
        </form>
    """

#Créez  une strcuture de donnée pour stocker les valeurs saisies



@app.post("/saisie")
def traiter_formulaire():
   
    is_json = request.content_type == "application/json"
    data = request.json if is_json else request.forms

    #ici creer une liste de valeurs et enregistez la   

    # calculez un identifiant un identifiant

    res = {}

    if is_json:
        return res
    else:
        return template("""<p>A remplir {}</p>""", **res)

    # attention si chaine "simple" il va chercher un gabarit de ce nom là
    # dans la vraie vie nous ferions une 'redirection pour'

@app.get("/calcul/<identifiant>")
def afficher_formulaire(identifiant):
    
    # afficher la série (dans la console et sur a page)
    texte = 'lorem ipsum'
    return """
     <p>  le texte vaut %s </p>
        <form action="/calcul/%s" method="post">
            fonction <input name="fname" type="text" />
            <input value="Ajouter" type="submit" />
        </form>
    """ % (texte, identifiant)

#Créez  une strcuture de donnée pour stocker les valeurs saisies

@app.get('/select')
def demo_select():
    options = ['somme', 'moyenne']

    templ = """
    <form method="post" action="/select">
  <select name="select_name">
     % for option_name in options:
        <option value="{{option_name}}">{{option_name.title()}}</option>
     % end
  </select>
  <input type="submit" value="Envoyer"/>
</form>
"""
    return template(templ, options=options)


@app.post("/select")
def traiter_formulaire():
   
    is_json = request.content_type == "application/json"
    data = request.json if is_json else request.forms

    res = data

    if is_json:
        return res
    else:
        return template("""<p>A remplir {{str(dict(res))}}</p>""", res=res)

    # attention si chaine "simple" il va chercher un gabarit de ce nom là
    # dans la vraie vie nous ferions une 'redirection pour'
