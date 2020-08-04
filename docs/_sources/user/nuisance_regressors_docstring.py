from CPAC import nuisance

nstring = nuisance.create_regressor_workflow.__doc__[
    nuisance.create_regressor_workflow.__doc__.find(
        "selector = "
    ) + len("selector = ") + 1:nuisance.create_regressor_workflow.__doc__.find(
        "Workflow Outputs"
    )
].rstrip()[:-1].lstrip('\n')

print('\n'.join([
    '{',
    '\n'.join([
        n[nstring.find('aCompCor')-4:] for n in nstring.split('\n')
    ]),
    '}'
]))
