# Agente WhatsApp - Envio Automatizado de Mensagens

Um sistema automatizado para envio de mensagens, imagens e outros tipos de mídia para grupos ou contatos do WhatsApp.

## 📋 Estrutura do Projeto

```
agente_whatsapp/
├── src/
│   ├── agente.py
│   ├── numeros.csv
│   ├── mensagens.csv
│   └── send_sandeco.py
├── media/
│   ├── imagens/
│   └── caption.txt
└── README.md
```

## 🚀 Funcionalidades

- Envio automatizado para múltiplos grupos/contatos
- Suporte para diferentes tipos de mídia:
  - Imagens (jpg, jpeg, png)
  - Vídeos (mp4)
  - Áudios (mp3)
  - Documentos (pdf)
  - Mensagens de texto (txt)
- Suporte para legendas personalizadas
- Controle de intervalo entre envios para evitar spam

## 📥 Pré-requisitos

- Python 3.7+
- Biblioteca send_sandeco
- WhatsApp Web conectado na Evolution API

## ⚙️ Configuração

### 1. Arquivo de Números (numeros.csv)
```csv
numero,nome
999999999999999999@g.us,Grupo1
```

### 2. Arquivo de Mensagens (mensagens.csv)
```csv
arquivo,tipo,legenda
imagem1.jpeg,imagem,caption.txt
```

### 3. Arquivo de Legenda (caption.txt)
Crie um arquivo de texto na pasta `media/` com sua legenda personalizada.

## 🛠️ Como Usar

1. Clone o repositório
2. Instale as dependências
3. Configure os arquivos CSV
4. Coloque suas mídias na pasta `media/`
5. Execute o script:

```bash
python src/agente.py
```

## ⚠️ Importantes Considerações

- O intervalo entre mensagens é de 2 segundos
- O intervalo entre números diferentes é de 10 segundos para evitar spam
- Certifique-se de que o WhatsApp Web esteja conectado antes de executar
- Verifique os caminhos das mídias antes de executar
- Mantenha os arquivos CSV corretamente formatados

## 🔒 Segurança

- Não compartilhe seus arquivos CSV com números de grupos privados
- Mantenha seu WhatsApp Web seguro
- Evite envios em massa que possam ser considerados spam

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar a documentação
- Enviar pull requests

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Autores

- Seu Nome
- [send_sandeco](https://github.com/ecodelearn) - Biblioteca base utilizada

## 📞 Suporte

Para suporte, abra uma issue no GitHub ou entre em contato através de [ecodelearn@outlook.com.com]
