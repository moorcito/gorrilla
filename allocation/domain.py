# SPDX-FileCopyrightText: 2026 moorcito
# SPDX-License-Identifier: AGPL-3.0-or-later

from datetime import date


def day_weight(day: date, weekday_weights, date_weights):
    if day in date_weights:
        return date_weights[day]
    else:
        return weekday_weights[day.weekday()]
