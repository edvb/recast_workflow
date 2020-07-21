from collections import OrderedDict
from typing import List, OrderedDict
import pytest

from recast_workflow import catalogue


class TestGetInvalidInputs:
    def test_no_input(self):
        assert catalogue.get_invalid_inputs(
            'generation', 'madgraph_pythia', {}) == {}

    def test_invalid_step(self):
        with pytest.raises(FileNotFoundError):
            assert catalogue.get_invalid_inputs(
                'fakestep', 'madgraph_pythia', {})

    def test_invalid_workflow_name(self):
        with pytest.raises(FileNotFoundError):
            assert catalogue.get_invalid_inputs(
                'generation', 'fakeworkflow', {})

    def test_one_invalid_input(self):
        assert catalogue.get_invalid_inputs('generation', 'madgraph_pythia', {
            'fakekey': 'foofum'}) == {'fakekey': 'foofum'}

    def test_two_invalid_input(self):
        assert catalogue.get_invalid_inputs('generation', 'madgraph_pythia', {
            'fakekey1': 'foofum', 'fakekey2': 'foofi'}) == {
                   'fakekey1': 'foofum', 'fakekey2': 'foofi'}

    def test_valid_input(self):
        assert catalogue.get_invalid_inputs('generation', 'madgraph_pythia', {
            'fakekey1': 'foofum', 'n_events': 10}) == {
                   'fakekey1': 'foofum'}


class TestGetMissingInputs:
    def test_all_missing(self):
        assert catalogue.get_missing_inputs(
            'generation', 'madgraph_pythia', {}) == set(['n_events', 'proc_card'])

    def test_invalid_step(self):
        with pytest.raises(FileNotFoundError):
            assert catalogue.get_missing_inputs(
                'fakestep', 'madgraph_pythia', {})

    def test_invalid_workflow_name(self):
        with pytest.raises(FileNotFoundError):
            assert catalogue.get_missing_inputs(
                'generation', 'fakeworkflow', {})

    def test_no_missing(self):
        assert catalogue.get_missing_inputs('generation', 'madgraph_pythia', {
            'n_events': 10, 'proc_card': 'path/to/proc_card', 'ufotar': 'path/to/ufotar'}) == set()


class TestGetAllCombinations:
    @pytest.mark.timeout(10)
    def test_no_loops(self):
        catalogue.get_all_combinations()
        assert True

    @pytest.mark.timeout(10)
    def test_correctness(self):
        def unordered_comp(x: List[OrderedDict]):
            sorted(x, key=lambda x: next(iter(x)))
        assert unordered_comp(catalogue.get_all_combinations()) == unordered_comp([
            OrderedDict([('generation', 'madgraph_pythia'), ('analysis', 'madanalysis')]), 
            OrderedDict({'generation': 'madgraph_pythia', 'selection': 'rivet', 'statistics': 'pyhf'}),
            OrderedDict({'generation': 'madgraph_pythia', 'selection': 'rivet', 'statistics': 'contur'}),
            ])


class TestGetValidCombination:
    @pytest.mark.timeout(10)
    def test_valid_analysis_sample(self):
        catalogue.get_valid_combinations({
            'analysis_id': '1609448'
        })
        assert True


class TestGetEnvSetting:
    @pytest.mark.timeout(10)
    def test_get_environment_settings(self):
        actual = catalogue.get_environment_settings(step='generation', subworkflow_name='madgraph_pythia')
        assert (actual == ['madgraph_version', 'pythia_version'])
