import pdfkit
import jinja2
import os


class PDF:
    def __init__(self):
        self.environment = jinja2.Environment(
            loader=jinja2.FileSystemLoader(searchpath='./'))

    def create_pdf(self, data: dict, template_file: str, output_file: str, css_file: str) -> None:
        with open(template_file, 'r') as f:
            template = f.read()
        template = self._populate_template(data, template, css_file)
        options = {
            'page-size': 'A4',
            'margin-top': '0',
            'margin-right': '0',
            'margin-bottom': '0',
            'margin-left': '0',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'debug-javascript': True,
        }
        pdfkit.from_string(template, output_file, options=options)

    def _populate_template(self, data: dict, template: str, css_file: str) -> str:
        """Populates the template with the needed data and CSS."""
        jinja_template = self.environment.from_string(template)
        with open(css_file, 'r') as f:
            css_content = f.read()
        data_with_css = {**data, 'style': css_content}
        return jinja_template.render(**data_with_css)

# pdf = PDF()
# try:
#     input_folder = os.path.join(os.getcwd(), 'input')
#     output_folder = os.path.join(os.getcwd(), 'output')
#     pdf.create_pdf(
#         data={},
#         template_file='./input/index.html',
#         output_file='./output/meu_arquivo.pdf'
#     )
#     with open('./output/meu_arquivo.pdf', 'rb') as f:
#         print("O arquivo foi gerado com sucesso!")
# except OSError:
#     print("Houve um problema ao gerar o arquivo.")
# except Exception as e:
#     print(f"Ocorreu um erro: {e}")


pdf = PDF()
try:
    input_folder = os.path.join(os.getcwd(), 'input')
    output_folder = os.path.join(os.getcwd(), 'output')
    css_file = os.path.join(input_folder, 'style.css')
    pdf.create_pdf(
        data={},
        template_file='./input/index.html',
        output_file='./output/meu_arquivo.pdf',
        css_file=css_file
    )
    with open('./output/meu_arquivo.pdf', 'rb') as f:
        print("O arquivo foi gerado com sucesso!")
except FileNotFoundError:
    print("Arquivo não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
