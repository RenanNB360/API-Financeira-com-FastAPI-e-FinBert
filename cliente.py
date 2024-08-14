import requests

url = 'http://0.0.0.0:8787/analisa_sentimento/'


payload = {
    'text': 'Bank of Japan Reports Record Stock Gains for Last Financial Year.',
    'title': 'Economy'
}


response = requests.post(url, json= payload)


if response.status_code == 200:

    dados_resposta = response.json()

    sentimento_previsto = dados_resposta.get('sentimento_previsto')
    probabiblidades = dados_resposta.get('probabilidades_das_previsoes', {})


    print('\nIA com LLM (e Construção de API) Para Análise de Sentimento em Noticiário Financeiro\n')

    print(f'Texto Analisado: {payload['text']}\n')

    print(f'Sentimento Previsto: {sentimento_previsto}')

    print('\nProbabilidades das Previsões:')

    for sentimento, probabilidade in probabiblidades.items():
        
        percentual = probabilidade * 100
        print(f' {sentimento}: {percentual:.2f}%')
    
    print('\nObrigado Por Usar Este Analisador de Sentimento de Noticiário Financeiro, Baseado em IA e LLM.')

else:

    print(f'Erro: {response.text}')