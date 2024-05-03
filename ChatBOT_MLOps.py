import speech_recognition as sr
import pygame
import time
from pathlib import Path
import warnings
from openai import OpenAI
import pandas as pd
warnings.filterwarnings("ignore")
client = OpenAI(api_key="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")

def generate_a(texto):
    """
    Modifica la descripción de interés del usuario para incluir recomendaciones basadas en el CSV.
    """
    template = f"Tu nombre es xbot. Tu eres un ejecutivo de créditos. Tu mision es solucionar preguntas acerca del nivel y probabilidad de financiamiento de los clientes."
    prompt = f"Aqui viene la pregunta del cliente: " + texto

    message_content = prompt
    information = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": template},
            {"role": "user", "content": message_content},
        ]
    )

    return information.choices[0].message.content


# texto='que es la vida'
# generate_a(texto)
#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
#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