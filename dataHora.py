import requests
import json
import os

def main() :
    valConexao = 0

    while valConexao != 200:
        try:
            resposta = requests.get('https://timeapi.io/api/time/current/zone?timeZone=America%2FSao_Paulo')
            valConexao = resposta.status_code
            if valConexao == 200:
                dia = json.loads(resposta.text)["day"]
                mes = json.loads(resposta.text)["month"]
                ano = json.loads(resposta.text)["year"]
                hora = json.loads(resposta.text)["hour"]
                minuto = json.loads(resposta.text)["minute"]
                segundo = json.loads(resposta.text)["seconds"]
                os.system(f"date {dia}-{mes}-{ano}")
                os.system(f"time {hora}:{minuto}:{segundo}")
                
            
        except Exception as e:
            valConexao = 0


if __name__ == "__main__":
    main()