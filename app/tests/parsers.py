from unittest.mock import MagicMock

from currency.models import Rate
from currency.tasks import parse_privatbank, parse_monobank
from tests.fixtures.parser_data import payload_mono, payload_privat


def test_privatbank(mocker):
    initial_count = Rate.objects.count()
    request_get_mock = mocker.patch('requests.get', return_value=MagicMock(json=lambda: payload_privat))  # noqa: F841
    parse_privatbank()
    assert Rate.objects.count() == initial_count + 2
    parse_privatbank()
    assert Rate.objects.count() == initial_count + 2


def test_monobank(mocker):
    initial_count = Rate.objects.count()
    request_get_mock = mocker.patch('requests.get', return_value=MagicMock(json=lambda: payload_mono))  # noqa: F841
    parse_monobank()
    assert Rate.objects.count() == initial_count + 2
    parse_monobank()
    assert Rate.objects.count() == initial_count + 2
