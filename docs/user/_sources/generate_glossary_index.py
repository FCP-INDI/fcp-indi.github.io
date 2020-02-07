import os

def generate():

    glossary_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "glossary"
    )

    glossary_files = [
        "/glossary/{}".format(fp) for fp in os.listdir(
            glossary_dir
        ) if fp!="index.txt"
    ]

    glossary_files.sort()

    with open(os.path.join(glossary_dir, "index.txt"), 'w+') as f:
        f.write(
            "\n".join([
                "Glossary",
                "########",
                "",
                "\n".join([
                    ".. toctree::",
                    "",
                    "\n".join([
                        "   {}".format(fp) for fp in glossary_files
                    ])
                ]),
                "",
                "\n".join([
                    ".. include:: {}".format(fp) for fp in glossary_files
                ])
            ])
        )
