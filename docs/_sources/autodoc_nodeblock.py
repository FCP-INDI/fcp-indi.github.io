from typing import TYPE_CHECKING, Any
from CPAC.pipeline.nodeblock import NodeBlockFunction
from docutils.statemachine import StringList
from sphinx.ext.autodoc import Documenter, FunctionDocumenter, bool_option


class NBFMixin(Documenter):
    def format_name(self) -> str:
        """Prepend "NodeBlockFunction" to the name"""
        return f'NodeBlockFunction: {super().format_name()}'


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
