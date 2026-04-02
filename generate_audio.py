import asyncio, edge_tts
async def amain():
      communicate = edge_tts.Communicate("Ola, bem-vindo ao guia de treinamento.", "pt-BR-AntonioNeural")
      await communicate.save("intro.mp3")
  if __name__ == "__main__": asyncio.run(amain())
