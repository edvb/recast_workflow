from typing import List

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
