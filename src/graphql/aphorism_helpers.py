from datetime import datetime, timedelta, timezone
import random

from src.graphql.aphorism import Aphorism

def __calculate_weight(item: Aphorism, current_datetime: datetime):
     # Calculate a weight based on the time since it was last shown

    if item.presented_at is None:
        return 10.0

    time_difference = (current_datetime - item.presented_at).total_seconds()

    # from at least 1 year old, all items will be given the max weight for an item that has been presented
    max_time_difference = timedelta(days=365).total_seconds()

    result = min(time_difference, max_time_difference) / max_time_difference
    return result


def select_random_aphorism_weighted(list: list[Aphorism]):
    current_datetime = datetime.now(timezone.utc)

    presented_ats = []
    weights = []

    for item in list:
        weight = __calculate_weight(item, current_datetime)

        presented_ats.append('none' if item.presented_at is None else f'{item.presented_at.year}-{item.presented_at.day}')
        weights.append(weight) 

    print("items:", presented_ats, "w:", weights)

    selected_item = random.choices(list, weights=weights, k=1)[0]

    return selected_item