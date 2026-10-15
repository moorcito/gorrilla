# SPDX-FileCopyrightText: 2026 moorcito
# SPDX-License-Identifier: AGPL-3.0-or-later

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Spot:
    floor: int
    number: int
    assignable: bool
    default_free: bool


def day_weight(
    day: date, weekday_weights: list[float], date_weights: dict[date, float]
) -> float:
    if day in date_weights:
        return date_weights[day]
    else:
        return weekday_weights[day.weekday()]


def free_spots(
    spots: list[Spot], owners_coming: set[Spot], week_confirmed: bool
) -> list[Spot]:
    free = []
    for spot in spots:
        if (
            spot.assignable
            and spot not in owners_coming
            and (spot.default_free or week_confirmed)
        ):
            free.append(spot)
    return free
