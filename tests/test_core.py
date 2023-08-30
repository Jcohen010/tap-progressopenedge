"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_tap_test_class

from tap_progressopenedge.tap import TapProgressOpenEdge



# Run standard built-in tap tests from the SDK:
TestTapProgressOpenEdge = get_tap_test_class(
    tap_class=TapProgressOpenEdge,
    config=".test_config",
)


