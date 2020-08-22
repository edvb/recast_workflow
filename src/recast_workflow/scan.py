import os
from string import Formatter
from typing import List, Dict

import recast_workflow.workflow as workflow

def build_multi(single_wf: dict, multi_params: List[str], name='') -> dict:
    """ Convert single stage workflow to multistage workflow given scan parameters. """
    param_arr = workflow.get_inputs(single_wf)
    params = {}

    for i in param_arr:
        params[i] = {'output': i, 'step': 'init'}
        if i in multi_params: params[i]['flatten'] = True

    multi_wf = {'stages': [{
        'dependencies': ['init'],
        'name': f'multi_{name if name else workflow.make_name(single_wf)}',
        'scheduler': {'parameters': params},
        'scheduler_type': 'multistep-stage',
        'scatter': {'method': 'zip', 'parameters': multi_params},
        'workflow' : single_wf
    }]}
    return multi_wf

def get_multi_params(tmpl_path: str):
    """ Get multiparameters from template file. """
    return [fname for _, fname, _, _ in Formatter().parse(yourstring) if fname]

def make_inputs(tmpl_path: str, output_dir_path: str, multi_params: Dict[str, List], prefix=''):
    """ Generate input files from template formatted with proper multi param values.
        multi_params is a dict that maps multi_params name to list of values. """
    tmpl_txt = ''
    with open(tmpl_path, 'r+') as tmpl_file:
        tmpl_txt = tmpl_file.read()

    output_dir_path = Path(output_dir_path)
    tmpl_name, tmpl_suffix = os.path.splitext(tmpl_path)[0]
    if not prefix: prefix = tmpl_name
    if not prefix.endswith('_'): prefix += '_'
    name_format = prefix + '_'.join(['{i}_{{{i}}}' for i in multi_params.keys()]) + tmpl_suffix

    toDo = [{k: 0 for k in multi_params.keys}]
    while len(toDo) > 0:
        # Create input file for current param combinations
        params = toDo[-1]
        for k, v in params.items(): params[k] = multi_params[k][v]

        out_filepath = name_format.format(params)
        with open(out_filepath, 'w+') as output_file:
            output_file.write(tmpl_txt.format(params))

        # Add next combinations to toDo
        for key in params.keys():
            if params[key] + 1 < len(multi_params[key]):
                toAdd = {k: v for k, v in params.items()}
                toAdd[key] += 1
                toDo.append(toAdd)
