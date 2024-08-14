from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import uvicorn


app = FastAPI()

finan_model = 'ProsusAI/finbert'

tokenizer = AutoTokenizer.from_pretrained(finan_model)

modelo_llm = AutoModelForSequenceClassification.from_pretrained(finan_model)

class Item(BaseModel):
    text: str
    title: str


async def preve_sentimento(input_text):

    inputs = tokenizer(input_text,
                       return_tensors= 'pt',
                       truncation= True,
                       padding= True,
                       max_length= 512)
    
    with torch.no_grad():
        outputs = modelo_llm(**inputs)
    
    probabilidades_previstas = torch.softmax(outputs.logits, dim = 1).squeeze().tolist()

    return probabilidades_previstas


@app.get('/')
async def index():
    return {'App de IA com LLM Para Analisar o Sentimento de Notícias Financeiras'}


@app.post('/analisa_sentimento')
async def analisa_sentimento(item: Item):

    input_text = f'{item.title} {item.text}'

    probabilidades_previstas = await preve_sentimento(input_text)

    sentimento_mapping = {0: 'Negativo', 1: 'Neutro', 2: 'Positivo'}

    sentimento_previsto = sentimento_mapping[probabilidades_previstas.index(max(probabilidades_previstas))]

    response_body = {
        'Sentimento Previsto': sentimento_previsto,
        'Probabilidades das Previsões': {
            'Negativo': probabilidades_previstas[0],
            'Neutro': probabilidades_previstas[1],
            'Positivo': probabilidades_previstas[2]
        }
    }

    return response_body


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)