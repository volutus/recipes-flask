import string
from pathlib import Path


class Recipe:
    def __init__(self, slug):
        self.slug = slug
        self.title = self.guess_title()
        self.image = self.guess_image()
        self.url = "/p/" + slug

    def guess_title(self):
        title = self.slug.replace("-", " ")
        title = string.capwords(title)
        return title

    def guess_image(self):
        return "/static/images/" + self.slug + ".jpg"


def recipes_list():
    recipes = []
    for child in Path('templates/generated').iterdir():
        if child.is_file() and child.suffix == '.html':
            recipes.append(Recipe(str(child.stem)))
    return sorted(recipes, key=lambda x: x.title)
