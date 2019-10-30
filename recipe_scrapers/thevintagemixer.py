from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class TheVintageMixer(AbstractScraper):

    @classmethod
    def host(self):
        return 'thevintagemixer.com'

    def title(self):
        return self.soup.find(
            'h2',
            {'class': 'wprm-recipe-name'}
        ).get_text()

    def total_time(self):
        return get_minutes(self.soup.find(
            'span', {'class': 'wprm-recipe-total_time-minutes'}).parent
        )

    def yields(self):
        return ""

    def ingredients(self):
        ingredients = self.soup.findAll(
            'li', {'class': "wprm-recipe-ingredient"}
        )

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
            if len(normalize_string(ingredient.get_text())) > 0
        ]

    def instructions(self):
        instructions = self.soup.findAll(
            'div',
            {'class': 'wprm-recipe-instruction-text'}
        )

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])
