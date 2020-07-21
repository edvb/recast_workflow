import os

import pytest
import shutil

import yaml

from recast_workflow import definitions
from recast_workflow import workflow

TEST_DIR = definitions.TESTS_DIR / 'scripts' / 'workflow'


class TestExpandWorkflow:
    def test_null_version(self):
        workflow_path = definitions.SUBWORKFLOWS_DIR / 'generation' / 'madgraph_pythia' / 'madgraph.yml'
        actual = workflow.expand_workflow(workflow_path, workflow_path,
                {'pythia_version': '8243', 'madgraph_version': '2.6.7'})
        print(actual)

    def test_simple(self):
        workflow_path = definitions.SUBWORKFLOWS_DIR / 'selection' / 'rivet' / 'workflow.yml'
        toplevel_path = workflow_path.parent
        actual = workflow.expand_workflow(workflow_path, toplevel_path,
                {'pythia_version': '8243', 'madgraph_version': '2.6.7'})


class TestMakeWorkflowFromYaml:
    @pytest.mark.skip(reason="not fully implemented.")
    def test_valid_args(self):
        input_path = os.path.join(TEST_DIR, 'valid_input.yml')
        expected = {}
        actual = workflow.make_workflow_from_yaml(input_path)
        assert actual == expected


class TestMakeWorkflow:
    def test_make_subworkflow(self):
        actual = workflow.make_subworkflow('generation',
                                           'madgraph_pythia',
                                           {'pythia_version': '8243', 'madgraph_version': '2.6.7'})
        text = yaml.dump(actual)
        print(text)

    def test_make_subworkflow_default_args(self):
        actual = workflow.make_subworkflow('generation',
                                           'madgraph_pythia',
                                           {})
        text = yaml.dump(actual)
        print(text)

    # Before running this test, remember to add your $DOCKER_USERNAME and $DOCKER_PASSWORD
    def test_valid_args_debug_generation(self):
        steps = ['generation']
        names = ['madgraph_pythia']
        env = [{}]
        actual = workflow.make_workflow(steps, names, env)
        print(yaml.dump(actual))

    def test_valid_args_debug_selection(self):
        steps = ['selection']
        names = ['rivet']
        env = [{}]
        actual = workflow.make_workflow(steps, names, env)
        print(yaml.dump(actual))

    def test_valid_args_debug_stat(self):
        steps = ['statistics']
        names = ['pyhf']
        env = [{}]
        actual = workflow.make_workflow(steps, names, env)
        print(yaml.dump(actual))

    def test_valid_args(self):
        steps = ['generation', 'selection', 'statistics']
        names = ['madgraph_pythia', 'rivet', 'pyhf']
        environment_settings = [{}, {}, {}]
        actual = workflow.make_workflow(steps, names, environment_settings)
        text = yaml.dump(actual)
        print(actual)
