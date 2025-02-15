import requests

url = "http://localhost:8000/predict"
dados_nota = {
    "id_supplier": 7101.0,
    "iss_retention": True,
    "iss_tax_rate": 2.0,
    "csll_tax_rate": 0.0,
    "ir_tax_rate": 0.0,
    "cofins_tax_rate": 0.0,
    "pis_tax_rate": 0.0,
    "opting_for_simples_nacional": True,
}

response = requests.post(url, json=dados_nota)

# Verificar o status da resposta
print("Status code:", response.status_code)

# Verificar o conteúdo da resposta
print("Response text:", response.text)
