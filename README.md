# 🎙️ Conversor de Voz e Tradutor

Um pequeno projeto em **Python** que transforma a sua voz em texto e depois traduz o que foi falado para o idioma escolhido. 🌎🗣️

O programa grava o áudio pelo microfone, reconhece a fala usando o Google e permite traduzir o texto para diferentes idiomas.

---

## ✨ O que o programa faz?

O funcionamento pode ser resumido assim:

```text
🎤 Você fala
     ↓
🎙️ O programa grava por 10 segundos
     ↓
💾 O áudio é salvo como output.wav
     ↓
🧠 O Google reconhece a fala
     ↓
📝 A fala vira texto
     ↓
🌍 O texto é traduzido
     ↓
💬 A tradução aparece no terminal
```

---

## 🚀 Funcionalidades

* 🎤 Gravação de áudio pelo microfone
* ⏱️ Gravação com duração de **10 segundos**
* 💾 Salvamento do áudio em `output.wav`
* 🗣️ Reconhecimento automático da fala
* 🇧🇷 Reconhecimento configurado para português do Brasil
* 🇺🇸 Tradução inicial para inglês
* 🌎 Escolha de outro idioma para tradução
* ⚠️ Tratamento de erros de reconhecimento e conexão

---

## 🧰 Tecnologias utilizadas

O projeto utiliza algumas bibliotecas Python:

| Biblioteca           | Função                            |
| -------------------- | --------------------------------- |
| `sounddevice`        | 🎤 Grava o áudio pelo microfone   |
| `numpy`              | 🔢 Trabalha com os dados do áudio |
| `scipy`              | 💾 Salva o áudio em formato WAV   |
| `speech_recognition` | 🧠 Converte a fala em texto       |
| `googletrans`        | 🌍 Faz a tradução do texto        |

---

## 📦 Instalação

Antes de executar o projeto, é necessário instalar as bibliotecas.

No terminal, execute:

```bash
pip install sounddevice numpy scipy SpeechRecognition googletrans==4.0.0-rc1
```

> 💡 Dependendo da instalação do Python no seu computador, pode ser necessário utilizar `python -m pip` no lugar de `pip`.

---

## ▶️ Como executar

Depois de instalar as bibliotecas, execute o arquivo Python:

```bash
python seu_arquivo.py
```

Assim que aparecer:

```text
Fale agora...
```

🎤 Comece a falar.

O programa irá gravar durante **10 segundos**.

Quando terminar, o áudio será salvo como:

```text
output.wav
```

Depois disso, o programa tentará reconhecer o que foi falado.

---

## 🌍 Escolhendo o idioma

Após reconhecer a fala, o programa pergunta:

```text
Para qual idioma devo traduzir?
```

Você pode informar o código do idioma.

### Alguns exemplos:

| Código    | Idioma    |
| --------- | --------- |
| `en` 🇺🇸 | Inglês    |
| `es` 🇪🇸 | Espanhol  |
| `fr` 🇫🇷 | Francês   |
| `de` 🇩🇪 | Alemão    |
| `it` 🇮🇹 | Italiano  |
| `pt` 🇧🇷 | Português |
| `ja` 🇯🇵 | Japonês   |
| `ko` 🇰🇷 | Coreano   |

Por exemplo:

```text
Para qual idioma devo traduzir? es
```

Resultado:

```text
🌍 Tradução para es: ...
```

---

## 🧠 Como o código funciona?

### 1. Importação das bibliotecas

O programa começa carregando as ferramentas necessárias:

```python
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
```

Cada biblioteca possui uma função específica no projeto.

---

### 2. Configuração da gravação

O programa define:

```python
duration = 10
sample_rate = 44100
```

Isso significa que a gravação terá **10 segundos** e utilizará uma taxa de amostragem de **44.100 Hz**.

---

### 3. Gravação 🎙️

O microfone é utilizado para capturar o áudio:

```python
recording = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="int16"
)
```

O valor:

```python
channels=1
```

indica que a gravação será **mono**.

Depois:

```python
sd.wait()
```

faz o programa esperar até a gravação terminar.

---

### 4. Salvando o áudio 💾

O áudio é salvo como um arquivo `.wav`:

```python
wav.write("output.wav", sample_rate, recording)
```

O arquivo ficará na mesma pasta onde o programa estiver sendo executado.

---

### 5. Reconhecimento da fala 🧠

O programa abre o arquivo de áudio:

```python
with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)
```

Depois utiliza o Google para tentar descobrir o que foi falado:

```python
text = recognizer.recognize_google(
    audio,
    language="pt-BR"
)
```

O `pt-BR` informa que a fala está em **português do Brasil**.

---

### 6. Primeira tradução 🌎

Depois que a fala é transformada em texto, o programa faz uma tradução para inglês:

```python
translator = Translator()

translated = translator.translate(
    text,
    dest="en"
)
```

E mostra o resultado:

```text
🌍 Tradução para o inglês: ...
```

---

### 7. Escolhendo outro idioma 🌐

O usuário também pode escolher outro idioma:

```python
dest_language = input(
    "Para qual idioma devo traduzir? "
)
```

Depois, o programa utiliza o código informado:

```python
translated = translator.translate(
    text,
    dest=dest_language
)
```

Assim, a mesma frase pode ser traduzida para diferentes idiomas.

---

## ⚠️ Tratamento de erros

O código possui dois tratamentos importantes.

### 🤔 Fala não reconhecida

```python
except sr.UnknownValueError:
    print("A fala não pôde ser reconhecida.")
```

Isso pode acontecer quando há muito ruído, silêncio ou quando a fala não consegue ser identificada corretamente.

### 🌐 Erro no serviço

```python
except sr.RequestError as e:
    print(f"Service error: {e}")
```

Esse erro pode aparecer quando existe algum problema de conexão ou com o serviço utilizado pelo reconhecimento de voz.

---

## 📁 Estrutura do projeto

Uma estrutura simples pode ser:

```text
📁 Projeto-Tradutor
│
├── 🐍 programa.py
│
└── 🎵 output.wav
```

O `output.wav` é criado automaticamente depois que o programa realiza uma gravação.

---

## 🔐 Precisa de Internet?

**Sim. 🌐**

O reconhecimento de voz e a tradução utilizam serviços online. Portanto, é necessário ter uma conexão com a Internet para que essas partes funcionem corretamente.

A gravação do áudio, por outro lado, acontece localmente no computador.

---

## 💡 Possíveis melhorias

Este projeto pode crescer bastante. Algumas ideias:

* ⏺️ Adicionar um botão para iniciar a gravação
* ⏹️ Permitir parar a gravação manualmente
* 🎧 Reproduzir o áudio gravado
* 🖥️ Criar uma interface gráfica
* 🌍 Mostrar o nome completo do idioma em vez do código
* 🔊 Fazer o computador falar a tradução em voz alta
* 📜 Manter um histórico das traduções
* 🗑️ Apagar automaticamente o `output.wav`
* 🔄 Permitir várias traduções sem reiniciar o programa

---

## 🏁 Conclusão

Este projeto combina **gravação de áudio, reconhecimento de voz e tradução automática** em um único programa Python.

Mesmo sendo relativamente simples, ele mostra como diferentes bibliotecas podem trabalhar juntas para transformar:

> 🎤 **Voz → Texto → Tradução → 🌎**

E isso já deixa uma ótima base para transformar o projeto em um tradutor de voz mais completo no futuro. 🚀

---

### 👨‍💻 Projeto

**Linguagem:** Python 🐍
**Tipo:** Reconhecimento de voz + Tradução 🌎
**Formato de áudio:** WAV 🎵
**Entrada:** Microfone 🎤
**Saída:** Texto traduzido 💬
