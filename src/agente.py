import csv
import time
import os
from pathlib import Path
from typing import Dict
from send_sandeco import SendSandeco

class WhatsAppSender:
    def __init__(self, numeros_csv: str, mensagens_csv: str, media_folder: str):
        self.numeros_csv = Path(numeros_csv).resolve()
        self.mensagens_csv = Path(mensagens_csv).resolve()
        self.media_folder = Path(media_folder).resolve()
        self.media_types = {
            ".mp3": "audio",
            ".mp4": "video",
            ".jpg": "image",
            ".png": "image",
            ".pdf": "document",
            ".txt": "textMessage"
        }

    def send_media(self, sender: SendSandeco, celular: str, arquivo: str, legenda: str = None) -> None:
        try:
            file_path = os.path.join(self.media_folder, arquivo)
            
            # Tratar legenda se for arquivo .txt
            caption_text = ""
            if legenda and legenda.endswith('.txt'):
                caption_path = os.path.join(self.media_folder, legenda)
                print(f"Lendo arquivo de legenda: {caption_path}")
                try:
                    with open(caption_path, 'r', encoding='utf-8') as f:
                        caption_text = f.read().strip()
                    print(f"Legenda carregada com sucesso: {caption_text[:50]}...")
                except Exception as caption_error:
                    print(f"Erro ao ler arquivo de legenda: {caption_error}")
                    return
            else:
                caption_text = legenda if legenda else ""

            print(f"\nProcessando arquivo: {file_path}")
            
            if not os.path.exists(file_path):
                print(f"Arquivo não encontrado: {file_path}")
                return

            file_extension = Path(file_path).suffix.lower()

            if file_extension == '.txt':
                with open(file_path, 'r', encoding='utf-8') as f:
                    message = f.read().strip()
                sender.textMessage(celular, message)
                print(f"Mensagem de texto enviada: {message[:30]}...")
            elif file_extension in ['.jpg', '.jpeg', '.png']:
                print(f"Enviando imagem para {celular}")
                print(f"Caminho da imagem: {file_path}")
                print(f"Usando legenda carregada do arquivo: {caption_text[:50]}...")
                
                sender.image(
                    number=celular,
                    image_file=str(file_path),
                    caption=caption_text
                )
                print("Imagem enviada com sucesso!")
            else:
                media_type = self.media_types.get(file_extension)
                if not media_type:
                    print(f"Extensão não suportada: {file_extension}")
                    return
                method = getattr(sender, media_type)
                method(celular, str(file_path))

        except Exception as e:
            print(f"Erro ao enviar {arquivo} para {celular}: {e}")
            print(f"Tipo do erro: {type(e)}")
            import traceback
            print(traceback.format_exc())

    def process_files(self) -> None:
        try:
            # Ler números
            with open(self.numeros_csv, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                numeros = list(reader)
                print(f"\nNúmeros carregados: {len(numeros)}")

            # Ler mensagens
            with open(self.mensagens_csv, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                mensagens = list(reader)
                print(f"Mensagens carregadas: {len(mensagens)}")

            # Processar envios
            for numero in numeros:
                print(f"\nProcessando número: {numero['numero']}")
                sender = SendSandeco()
                for mensagem in mensagens:
                    print(f"\nEnviando mensagem: {mensagem}")
                    self.send_media(
                        sender=sender,
                        celular=numero['numero'],
                        arquivo=mensagem['arquivo'],
                        legenda=mensagem.get('legenda', '')
                    )
                    time.sleep(2)  # Intervalo entre mensagens para o mesmo número
                print(f"Aguardando 10 segundos antes do próximo número...")
                time.sleep(10)  # Intervalo maior entre números diferentes

        except Exception as e:
            print(f"Erro ao processar arquivos: {e}")
            import traceback
            print(traceback.format_exc())

def main():
    base_dir = Path(__file__).parent.parent.resolve()
    numeros_csv = base_dir / 'src' / 'numeros.csv'
    mensagens_csv = base_dir / 'src' / 'mensagens.csv'
    media_folder = base_dir / 'media'
    
    sender = WhatsAppSender(
        str(numeros_csv),
        str(mensagens_csv),
        str(media_folder)
    )
    sender.process_files()

if __name__ == "__main__":
    main()
