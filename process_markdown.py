import markdown
from pathlib import Path


def process():
    for child in Path('recipes').iterdir():
        if not child.is_file() or child.suffix != '.md':
            continue
        stem = child.stem
        text = child.read_text(encoding="utf-8")
        html = markdown.markdown(text)

        # Add Flask prefix + suffix
        html = "{% extends 'layout.html' %} \n {% block content %} \n" + html
        html = html + "\n {% endblock content %}"
        if html is not None:
            html_filename = stem + ".html"
            with open('templates/generated/' + html_filename, 'w', encoding="utf-8") as output:
                output.write(html)


process()
