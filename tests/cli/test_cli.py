from click.testing import CliRunner

class TestShellComplete:
    def test_shellcomplete_cli(self):
        from recast_workflow.cli.complete import cli

        runner = CliRunner()
        result = runner.invoke(cli, ['bash'])
        assert 'complete -F _recast-wf_completion -o default recast-wf' in result.output
