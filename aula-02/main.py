from fastapi import FastAPI
from datetime import datetime, timedelta


app = FastAPI()


@app.get("/")
def hello():
    return {"hello": "World"}


@app.get("/diasemana")
def dia_semana():

    dias = {
        "0": "segunda-feira",
        "1": "terça-feira",
        "2": "quarta-feira",
        "3": "quinta-feira",
        "4": "sexta-feira",
        "5": "sábado",
        "6": "domingo"
    }

    return dias[str(datetime.now().weekday())]


@app.post("/number/")
def par_impar(num: int):

    res = "par" if num%2 == 0 else "impar"

    return {str(num): res}


@app.get("/hora/")
def horario(cidade: str):

    timezone_offsets = {
        'brasilia': -3,
        'tokyo': 9,
        'londres': 0,
    }

    if cidade.lower() not in timezone_offsets:
        return "Cidade não suportada"

    utc_now = datetime.utcnow()

    local_time = utc_now + timedelta(hours=timezone_offsets[cidade.lower()])

    hora = local_time.strftime('%Y-%m-%d %H:%M:%S')

    return {cidade: hora}

@app.get("/frase")
def frase():
    import json
    import requests

    url = "https://zenquotes.io/api/today"
    response = requests.get(url)
    nome_arquivo = "frase.json"

    if response.status_code == 200:
        data = response.json()

        with open(nome_arquivo, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    else:
        with open(nome_arquivo, "w") as f:
            json.dump({"erro": "Não foi possível selecionar uma frase"}, f, ensure_ascii=False, indent=4)

    with open(nome_arquivo) as f:
        return json.load(f)


@app.get("/{pais}")
def get_country(pais: str):

    import json

    with open("paises.json") as f:
        paises = json.load(f)

    for i in range(0, len(paises)):
        pais2 = paises[i]
        return pais2

@app.get("/{pais}/name")
def get_country_name(pais: str):
    pais = get_country(pais)

    return pais["name"]

@app.get("/{pais}/area")
def get_country_area(pais: str):
    pais = get_country(pais)
    return pais["country_code"]

@app.get("/{pais}/ISO")
def get_country_iso(pais: str):
    pais = get_country(pais)
    return pais["iso_codes"]





@app.get("/sortear/{quant}/{max}")
def sortear():
    pass



@app.get("/users")
def list_users():
    import json

    with open("users.json") as f:
        return json.load(f)
