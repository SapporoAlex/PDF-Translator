from pdfminer.high_level import extract_text
import deepl


text = extract_text("your file here.pdf")
with open('input.txt', 'w') as input_file:
    input_file.write(text)

authentication_key = "****"
translator = deepl.Translator(authentication_key)
tt = open("output.txt", 'w', encoding='utf-8')
input_path = "input.txt"
output_path = "output.txt"
excel_file_path = 'test.xlsx'


translator.translate_document_from_filepath(input_path, output_path, target_lang='EN-US')
