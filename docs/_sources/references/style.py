from pybtex.style.formatting import toplevel
from pybtex.style.formatting.plain import Style
from pybtex.style.names.lastfirst import NameStyle as LastFirst
from pybtex.style.sorting.none import SortingStyle as NoSort
from pybtex.style.template import field, href, join, optional, \
                                  optional_field, sentence, tag, words

date = words[field('year'), optional_field('month')]


class CPAC_DocsStyle(Style):
    def __init__(self, *args, **kwargs):
        super().__init__(
            abbreviate_names=True,
            name_style=LastFirst,
            sorting_style=NoSort
        )

    def get_book_template(self, entry):
        template = toplevel[optional[
            sentence[self.format_names('author')]],
            optional[sentence[date]],
            optional[sentence[href[
                field('url'),
                optional[tag('em')[self.format_title(entry, 'title')]]
            ]]] if entry.fields.get('url') else optional[sentence[
                tag('em')[self.format_title(entry, 'title')]
            ]],
            optional[sentence[
                join(sep=': ')[
                    optional_field('address'),
                    optional_field('publisher')
                ],
            ]],
            sentence[optional_field('note')],
        ]
        return template

    def get_misc_template(self, entry):
        template = toplevel[
            optional[sentence[self.format_names('author')]],
            optional[sentence[
                optional[field('howpublished')],
                optional[date],
            ]],
            optional[sentence[join(sep=', ')[href[
                optional_field('url'),
                optional[self.format_title(entry, 'title', as_sentence=False)]]
                if entry.fields.get('url') else optional[
                    self.format_title(entry, 'title')
                ],
                optional[tag('em')[self.format_title(entry, 'journal')]],
            ]]],
            sentence[optional_field('note')],
        ]
        return template
