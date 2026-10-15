# SPDX-FileCopyrightText: 2026 moorcito
# SPDX-License-Identifier: AGPL-3.0-or-later

from datetime import date

from allocation.domain import Spot, day_weight, free_spots

WEEKDAY_WEIGHTS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
DATE_WEIGHTS = {date(2026, 12, 25): 0, date(2026, 12, 30): 0}
UNASSIGNABLE_SPOT = [Spot(floor=0, number=2, assignable=False, default_free=False)]
ASSIGNABLE_SPOT = [Spot(floor=0, number=2, assignable=True, default_free=False)]
ASSIGNABLE_FREE_SPOT = [Spot(floor=0, number=2, assignable=True, default_free=True)]


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


def test_free_spots_unassignable_spot():
    assert free_spots(UNASSIGNABLE_SPOT, set(), True) == []


def test_free_spots_owner_coming_to_assignable_spot():
    assert free_spots(ASSIGNABLE_SPOT, {ASSIGNABLE_SPOT[0]}, True) == []


def test_free_spots_default_free_spot_needs_no_confirmation():
    assert free_spots(ASSIGNABLE_FREE_SPOT, set(), False) == ASSIGNABLE_FREE_SPOT


def test_free_spots_other_spots_wait_for_confirmation():
    assert free_spots(ASSIGNABLE_SPOT, set(), False) == []
    assert free_spots(ASSIGNABLE_SPOT, set(), True) == ASSIGNABLE_SPOT
