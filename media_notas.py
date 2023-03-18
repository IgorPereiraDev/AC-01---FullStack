from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main():

    nota_um = request.args.get('nota1')
    nota_dois = request.args.get('nota2')

    if nota_um and nota_dois:
        
        media = (float(nota_um) + float(nota_dois)) / 2

        if media >= 7:
            resposta = 'Parabéns, você foi aprovado, sua primeira nota é: ' + nota_um + ' e a segunda nota é: ' + nota_dois +  ' sendo assim, sua média é: ' + str(media) + ' :D'
        elif media >= 5 and media < 7:
            resposta = 'Você esta de DP, sua primeira nota é: ' + nota_um + ' e a segunda nota é: ' + nota_dois +  ' sendo assim, sua média é: ' + str(media)
        else:
            resposta = 'Que Pena, você foi reprovado, sua primeira nota é: ' + nota_um + ' e a segunda nota é: ' + nota_dois +  ' sendo assim, sua média é: ' + str(media) + ' :('

    else:
        resposta = 'Informe as notas na URL'
    
    return resposta

if __name__ == '__main__':
    app.run(debug=True)