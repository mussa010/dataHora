import requests
import json
import subprocess
from datetime import datetime

def main() :
    valConexao = 0

    while valConexao != 200:
        try:
            resposta = requests.get('https://timeapi.io/api/time/current/zone?timeZone=America%2FSao_Paulo', timeout=5)
            valConexao = resposta.status_code
            if valConexao == 200:
                dia = json.loads(resposta.text)["day"]
                mes = json.loads(resposta.text)["month"]
                ano = json.loads(resposta.text)["year"]
                hora = json.loads(resposta.text)["hour"]
                minuto = json.loads(resposta.text)["minute"]
                segundo = json.loads(resposta.text)["seconds"]
                subprocess.run(f"date {dia}-{mes}-{ano}", shell= True)
                subprocess.run(f"time {hora}:{minuto}:{segundo}", shell= True)

                if datetime.now().day == dia and datetime.now().month == mes and datetime.now().year == ano and datetime.now().hour == hora and datetime.now().minute == minuto and datetime.now().second == segundo:
                    print("Atualizado com sucesso!")
                    return 0
                else:
                    print("Não foi possível atualizar!")
                    return 1
            
        except Exception as e:
            valConexao = 0


if __name__ == "__main__":
    main()