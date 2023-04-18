import pytest
from pytest_mock import MockerFixture
from unittest.mock import call

from pipeline.utils.snirf import open_snirf


@pytest.fixture(autouse=True)
def run_before_and_after_tests(mocker: MockerFixture):
    """Fixture to execute asserts before and after a test is run"""
    # Setup: fill with any logic you want
    mocker.resetall()

    yield  # this is where the testing happens

    # Teardown : fill with any logic you want


def describe_open_snirf() -> None:
    def test_with_no_path_argument(mocker: MockerFixture) -> None:
        mocked_Snirf = mocker.patch("pipeline.utils.snirf.Snirf", autospec=True)

        open_snirf()

        assert mocked_Snirf.call_args.args == ()

    def test_with_path_argument(mocker: MockerFixture) -> None:
        snirf_path = "some/path/to/snirf"
        mocked_Snirf = mocker.patch("pipeline.utils.snirf.Snirf", autospec=True)

        open_snirf(snirf_path)

        assert mocked_Snirf.call_args.args == (snirf_path, "r")

        context_snirf = mocked_Snirf.return_value.__enter__.return_value

        assert context_snirf.method_calls[0] == call.copy()
