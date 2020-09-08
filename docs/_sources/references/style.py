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

    def format_doi(self, doi):
        return join(sep=':')[
            words['doi'],
            href[join(sep='/')[
                'https://dx.doi.org', doi
            ], doi]
        ]

    def get_article_template(self, entry):
        template = toplevel[optional[
            sentence[self.format_names('author')]],
            optional[sentence[date]],
            optional[
                href[
                    field('url'),
                    self.format_title(entry, 'title')
                ] if entry.fields.get('url') else
                self.format_title(entry, 'title')
            ],
            sentence[join(sep=' ')[
                optional[tag('em')[join(sep=', ')[
                    self.format_title(entry, 'journal', as_sentence=False),
                    optional_field('volume')
                ]]],
                optional[join(sep='')[
                    ':' if entry.fields.get('volume') else '',
                    optional_field("number")
                ] if entry.fields.get('number') else ''],
            ]],
            optional[join(sep='')[
                ', pp. ', optional_field('pages')
            ] if entry.fields.get('pages') else ''],
            optional[self.format_doi(optional_field('doi'))],
            sentence[optional_field('note')],
        ]
        return template

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
