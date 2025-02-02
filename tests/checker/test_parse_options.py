import argparse

import pytest

from flake8_aaa import Checker
from flake8_aaa.conf import ActBlockStyle, Config
from flake8_aaa.exceptions import UnexpectedConfigValue


def test() -> None:
    """
    Smoke test that Checker can parse options and keep the result in its config
    instance.

    Note:
        The "real" testing happens in `Config.load_options()` which is called
        by this method.
    """
    option_manager = None  # Fake because it's not used by SUT
    options = argparse.Namespace(aaa_act_block_style='default')

    result = Checker.parse_options(option_manager, options, [])

    assert result is None
    assert isinstance(Checker.config, Config)
    assert Checker.config.act_block_style == ActBlockStyle.DEFAULT


# --- FAILURES ---


def test_unknown() -> None:
    """
    Unknown value raises
    """
    options = argparse.Namespace(aaa_act_block_style='foobar')

    with pytest.raises(UnexpectedConfigValue):
        Checker.parse_options(None, options, [])
