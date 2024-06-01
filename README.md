# PDF to Text and Translation
This repository contains a Python script that extracts text from a PDF file, saves it to a text file, and translates the content into English using the DeepL API.

## Features
- Extract text from a PDF file.
- Translate the extracted text into English.
   Save the translated text to a file.

## Requirements
- Python 3.6+
- pdfminer.six library for extracting text from PDFs.
- deepl library for translation.
- A valid DeepL API authentication key.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/pdf-to-text-translation.git
cd pdf-to-text-translation
```
2. Install the required Python packages:
```bash
pip install pdfminer.six deepl
```

## Usage
1. Place the PDF file you want to translate in the project directory.

2. Update the authentication_key variable in the script with your DeepL API key.

3. Run the script:

```python
import deepl
from pdfminer.high_level import extract_text

# Extract text from PDF
text = extract_text("ファイル.pdf")
with open('input.txt', 'w') as input_file:
    input_file.write(text)

# DeepL API key
authentication_key = "your-authentication-key-here"
translator = deepl.Translator(authentication_key)

# Translate the document
input_path = "input.txt"
output_path = "output.txt"
translator.translate_document_from_filepath(input_path, output_path, target_lang='EN-US')
```
The translated text will be saved in output.txt.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
