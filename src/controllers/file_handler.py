import pdfplumber
import json

class FileHandler:
    @staticmethod
    def extract_text(file_path):
        """Extrae texto de archivos PDF, TXT o JSON."""
        extension = file_path.split('.')[-1].lower()
        
        try:
            if extension == 'pdf':
                return FileHandler._read_pdf(file_path)
            elif extension == 'txt':
                return FileHandler._read_txt(file_path)
            elif extension == 'json':
                return FileHandler._read_json(file_path)
            else:
                return "Error: Formato no soportado."
        except Exception as e:
            return f"Error al leer archivo: {str(e)}"

    @staticmethod
    def _read_pdf(path):
        text = ""
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text.strip()

    @staticmethod
    def _read_txt(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def _read_json(path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return json.dumps(data, indent=2)