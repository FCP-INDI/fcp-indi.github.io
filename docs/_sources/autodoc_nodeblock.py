from typing import TYPE_CHECKING, Any
from CPAC.pipeline.nodeblock import NodeBlockFunction
from docutils.statemachine import StringList
from sphinx.ext.autodoc import Documenter, FunctionDocumenter, bool_option


class NBFMixin(Documenter):
    def add_directive_header(self, sig: str) -> None:
        """Prepend "NodeBlockFunction" to the name & add the directive
        header and options to the generated content."""
        domain = getattr(self, 'domain', 'py')
        directive = getattr(self, 'directivetype', self.objtype)
        name = self.format_name()
        sourcename = self.get_sourcename()

        # Prepend NodeBlockFunction pseudoheader
        self.add_line(f'*NodeBlockFunction*: **{self.object.name}**',
                      sourcename)
        self.add_line('', sourcename)
        # one signature per line, indented by column
        prefix = f'.. {domain}:{directive}:: '
        for i, sig_line in enumerate(sig.split("\n")):
            self.add_line(f'{prefix}{name}{sig_line}',
                          sourcename)
            if i == 0:
                prefix = " " * len(prefix)

        if self.options.no_index or self.options.noindex:
            self.add_line('   :no-index:', sourcename)
        if self.objpath:
            # Be explicit about the module, this is necessary since .. class::
            # etc. don't support a prepended module name
            self.add_line('   :module: %s' % self.modname, sourcename)


class NodeBlockFunctionDocumenter(NBFMixin, FunctionDocumenter):
    """Sphinx Documenter for NodeBlockFunction"""
    objtype = 'NodeBlockFunction'
    directivetype = FunctionDocumenter.objtype
    priority = 10 + FunctionDocumenter.priority
    option_spec = dict(FunctionDocumenter.option_spec)
    option_spec['hex'] = bool_option

    @classmethod
    def can_document_member(cls, member: Any, membername: str, isattr: bool,
                            parent: Any) -> bool:
        """Determine if a member is a NodeBlockFunction"""
        return isinstance(member, NodeBlockFunction)

    def add_content(self,
                    more_content: StringList | None
                    ) -> None:

        super().add_content(more_content)

        source_name = self.get_sourcename()
        # nbf_object: NodeBlockFunction = self.object
        self.add_line('', source_name)
    


def setup(app: 'Sphinx') -> dict[str, Any]:
    app.setup_extension('sphinx.ext.autodoc')  # Require autodoc extension
    app.add_autodocumenter(NodeBlockFunctionDocumenter)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
