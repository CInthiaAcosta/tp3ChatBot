from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    api_key: str = os.getenv("GEMINI_API_KEY")
    model: str = os.getenv("MODEL")
    maximo_intento: int=int(os.getenv("MAXIMO_INTENTO", 3))
    tiempo_restante: int=int(os.getenv("TIEMPO_RESTANTE", 30))
    max_historial: int=int(os.getenv("MAX_HISTORIAL", 12))

Settings=Settings()
