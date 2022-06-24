from pybtex.style.formatting import toplevel
from pybtex.style.formatting.plain import Style
from pybtex.style.names.lastfirst import NameStyle as LastFirst
from pybtex.style.sorting.none import SortingStyle as NoSort
from pybtex.style.template import field, href, join, optional, \
                                  optional_field, sentence, tag, words

date = words[field('year'), optional_field('month')]


class CPAC_DocsStyle(Style):
    """
    Custom style for sphinxcontrib-bibtex references [1] in C-PAC documentation.

    References
    ----------
    .. [1] Troffaes, M.C.M. 2021. Custom Formatting, Sorting, and Labelling. *sphinxcontrib-bibtex 1.0.0 documentation*. https://sphinxcontrib-bibtex.readthedocs.io/en/1.0.0/usage.html#custom-formatting-sorting-and-labelling
    """  # pylint: disable=line-too-long  # noqa: E501
    # pylint: disable=no-value-for-parameter,invalid-name
    def __init__(self, *args, **kwargs):
        # pylint: disable=unused-argument
        super().__init__(
            abbreviate_names=True,
            name_style=LastFirst,
            sorting_style=NoSort
        )

    def format_doi(self, e):
        """
        Parameters
        ----------
        e : str
          digital object identifier
        """
        return join(sep=':')[
            words['doi'],
            href[join(sep='/')[
                'https://dx.doi.org',
                e
            ], e]
        ]

    def get_article_template(self, e):
        template = toplevel[optional[
            sentence[self.format_names('author')]],
            optional[sentence[date]],
            optional[
                href[
                    field('url'),
                    self.format_title(e, 'title')
                ] if e.fields.get('url') else
                self.format_title(e, 'title')
            ],
            join(sep=' ')[
                optional[tag('em')[join(sep=', ')[
                    self.format_title(e, 'journal', as_sentence=False),
                    optional_field('volume')
                ]]],
                optional[join(sep='')[
                    ':' if e.fields.get('volume') else '',
                    optional_field("number")
                ] if e.fields.get('number') else ''],
            ],
            optional[join(sep='')[
                ', pp. ', optional_field('pages')
            ] if e.fields.get('pages') else ''],
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
                optional[tag('em')[join(sep=', ')[
                    self.format_title(entry, 'title', as_sentence=False),
                    optional_field('edition')
                ]]]
            ]]] if entry.fields.get('url') else optional[sentence[
                tag('em')[join(sep=', ')[
                    self.format_title(entry, 'title', as_sentence=False),
                    optional_field('edition')
                ]]
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

    def get_incollection_template(self, entry):
        template = toplevel[optional[
            sentence[self.format_names('author')]],
            optional[sentence[date]],
            optional[sentence[href[
                field('url'),
                self.format_title(entry, 'title')
            ]]] if entry.fields.get('url') else optional[sentence[
                self.format_title(entry, 'title')
            ]],
            optional[tag('em')[join(sep=', ')[
                self.format_title(entry, 'booktitle', as_sentence=False),
                optional_field('edition')
            ]]],
            optional[sentence[
                join(sep=': ')[
                    optional_field('address'),
                    optional_field('publisher')
                ],
            ]],
            sentence[optional_field('note')],
        ]
        return template

    def get_misc_template(self, e):
        template = toplevel[
            optional[sentence[self.format_names('author')]],
            optional[sentence[
                optional[field('howpublished')],
                optional[date],
            ]],
            optional[sentence[join(sep=', ')[
                href[
                    optional_field('url'),
                    optional[self.format_title(e, 'title', as_sentence=False)]
                ] if e.fields.get('url') else optional[
                    self.format_title(e, 'title')
                ],
                optional[tag('em')[self.format_title(e, 'journal')]],
            ]]],
            optional[self.format_doi(optional_field('doi'))],
            sentence[optional_field('note')],
        ]
        return template

    def get_techreport_template(self, e):
        return self.get_article_template(e)
