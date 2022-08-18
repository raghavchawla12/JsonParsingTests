import pytest

from test_data.given_json import GivenJson
from utilities.utils_class import utilsClass


class TestProblems(utilsClass):

    @pytest.mark.parametrize("count_exp", [4])
    def test_01_validate_that_team_has_only_four_foreign_players(self, count_exp):
        log = self.getLogger()
        players_list = GivenJson.needed_json
        log.debug("Got Json through Test Data Package using PyTest Fixtures in Test 01")
        count = 0
        try:
            for i in range(0, len(players_list)):
                countries = players_list[i]['country']
                if countries != "India":
                    count = count + 1
            assert count == count_exp
            log.info("Test Case Passed with correct Foreign Player Count i.e. 4")
        except Exception as e:
            log.error("Test Case Failed")
            raise e

    def test_02_validate_that_team_has_atleast_one_wicket_keeper(self):
        log = self.getLogger()
        players_list = GivenJson.needed_json
        log.debug("Got Json through Test Data Package using PyTest Fixtures in Test 02")
        count = 0
        try:
            for i in range(0, len(players_list)):
                role = players_list[i]['role']
                if role == "Wicket-keeper":
                    count = count + 1
            assert count >= 1
            log.info("Test Case Passed, There is atleast one wicket keeper present. "
                     "Total Wicketkeepers are " + str(count))
        except Exception as e:
            log.error("Test Case Failed")
            raise e
