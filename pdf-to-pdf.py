from PyPDF2 import PdfReader
from gtts import gTTS
from unidecode import unidecode
from tqdm import tqdm

# Abrir archivo pdf
pdf_file = open('doc.pdf', 'rb')

# Crear un objeto pdf reader
pdf_reader = PdfReader(pdf_file)

# Obtener el numero de paginas
num_pages = len(pdf_reader.pages)

# Iterar sobre las paginas
text = ""
for page_num in tqdm(range(num_pages), "Extracting Pages"):
    page = pdf_reader.pages[page_num]
    text += unidecode(page.extract_text())

# Cerrar el archivo pdf
pdf_file.close()

# Crear un objeto gTTS
tts = gTTS(text, lang='es')

# Guardar el archivo de audio
with tqdm(total=100, unit="KB", desc="Saving audio") as pbar:
    tts.save('audio.mp3')
    pbar.update(100)
