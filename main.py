from fastapi import FastAPI
from pydantic import BaseModel
import openai
from fastapi.middleware.cors import CORSMiddleware

openai.api_key = "sk-...tu_api_key_aqui..."

app = FastAPI()

# Configura CORS para aceptar peticiones de cualquier origen (para probar)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción pon el dominio exacto de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    message: str  # Cambié 'question' por 'message' para que coincida con el frontend

@app.post("/chat")
async def chat(question: Question):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question.message}]
    )
    answer = response.choices[0].message.content
    return {"response": answer}  # Cambié 'answer' por 'response' para que coincida con frontend
