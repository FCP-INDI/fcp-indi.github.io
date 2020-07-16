import os
import sys
from os.path import basename
from io import StringIO ## for Python 3

from docutils.parsers.rst import Directive
from docutils import nodes

class ExecDirective(Directive):
    """Execute the specified python code and insert the output into the document"""
    has_content = True

    def run(self):
        oldStdout, sys.stdout = sys.stdout, StringIO()
        oldCwd = os.getcwd()

        try:
            os.makedirs(os.path.join(
               os.path.dirname(self.state.document.settings.env.doctreedir),
                os.path.dirname(self.state.document.settings.env.docname)
            ))
        except:
            pass

        os.chdir(os.path.join(
            os.path.dirname(self.state.document.settings.env.doctreedir),
            os.path.dirname(self.state.document.settings.env.docname)
        ))

        try:
            exec('\n'.join(self.content))
            return [nodes.literal_block(sys.stdout.getvalue())]
        except Exception as e:
            _, _, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            error_message = nodes.paragraph(
                text="Unable to execute python code at %s:%d:" % (
                    os.path.basename(fname), exc_tb.tb_lineno
                )
            )
            stack_message = nodes.paragraph(text=str(e))
            return [
                nodes.error(None, error_message, stack_message)
            ]
        finally:
            sys.stdout = oldStdout
            os.chdir(oldCwd)

def setup(app):
    app.add_directive('exec', ExecDirective)
