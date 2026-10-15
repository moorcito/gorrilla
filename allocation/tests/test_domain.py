# SPDX-FileCopyrightText: 2026 moorcito
# SPDX-License-Identifier: AGPL-3.0-or-later

from datetime import date

from allocation.domain import day_weight

WEEKDAY_WEIGHTS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
DATE_WEIGHTS = {date(2026, 12, 25): 0, date(2026, 12, 30): 0}


def test_day_weight_uses_the_weekday_weight():
    assert day_weight(date(2026, 10, 21), WEEKDAY_WEIGHTS, DATE_WEIGHTS) == 0.3
    assert day_weight(date(2026, 11, 1), WEEKDAY_WEIGHTS, DATE_WEIGHTS) == 0.7
    assert day_weight(date(2026, 11, 30), WEEKDAY_WEIGHTS, DATE_WEIGHTS) == 0.1


def test_day_weight_uses_the_date_weights():
    assert (
        day_weight(
            date(2026, 12, 25),
            WEEKDAY_WEIGHTS,
            DATE_WEIGHTS,
        )
        == 0
    )
