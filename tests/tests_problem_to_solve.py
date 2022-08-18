import pytest

from test_data import given_json


class TestProblems:

    def test_01_validate_that_team_has_only_four_foreign_players(self, get_test_cases_data):
        log = self.getLogger()
        json = get_test_cases_data['json']

    @pytest.fixture(params=given_json.GivenJson)
    def get_test_cases_data(self, request):
        return request.param
