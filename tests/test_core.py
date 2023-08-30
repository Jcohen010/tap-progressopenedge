"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_tap_test_class

from tap_progressopenedge.tap import TapProgressOpenEdge

SAMPLE_CONFIG = {
    'DRIVER':'DataDirect 7.1 OpenEdge Wire Protocol',
    'HOST':'HOST',
    'PORT':'0000',
    'DB':'TestDB',
    'UID':'username',
    'PWD':'pass'
}


# Run standard built-in tap tests from the SDK:
TestTapProgressOpenEdge = get_tap_test_class(
    tap_class=TapProgressOpenEdge,
    config=SAMPLE_CONFIG,
)


# TODO: Create additional tests as appropriate for your tap.
