import os
import pytest
from pytest_mock import MockerFixture
from unittest.mock import call

from pipeline.steps.step1 import Step1


@pytest.fixture(autouse=True)
def run_before_and_after_tests(mocker: MockerFixture):
    """Fixture to execute asserts before and after a test is run"""
    # Setup: fill with any logic you want
    mocker.resetall()

    yield  # this is where the testing happens

    # Teardown : fill with any logic you want


@pytest.fixture
def csv_file():
    test_dir = os.path.dirname(__file__)
    return os.path.abspath(test_dir + "/fixtures/example_data.csv")


def describe_step1() -> None:
    def test_loading_csv_to_snirf(mocker: MockerFixture, csv_file):
        step1 = Step1(csv_file)
        snirf = step1.run()

        assert snirf.nirs[0].data[0].dataTimeSeries.all() == step1.data.all()

        # assert snirf.validate == True
