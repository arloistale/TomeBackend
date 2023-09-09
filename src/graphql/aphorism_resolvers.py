from datetime import datetime, timezone
from typing import List, Optional
from src.graphql.aphorism_helpers import select_random_aphorism_weighted

from src.graphql.aphorism import Aphorism
from src.graphql.session import client

def get_aphorisms() -> List[Aphorism]:
    result = client.table('aphorisms').select('*').execute()

    # TODO: Figure out error handling
    #if result.status_code != 200:
        #raise Exception("Supabase request failed.")
    
    aphorisms = []

    for row in result.data:
        aphorism = Aphorism(
            id=str(row['id']),
            title=row['title'],
            content=row['content'],
            created_at=datetime.fromisoformat(row['created_at']),
            presented_at=datetime.fromisoformat(row.get('presented_at')) if row.get('presented_at') else None
        )
        aphorisms.append(aphorism)

    print("fetched", len(aphorisms), "aphorisms")

    return aphorisms

def present_random_aphorism() -> (Optional[Aphorism], Optional[any]):
        current_datetime = datetime.now(timezone.utc)

        aphorisms = get_aphorisms()

        if any(item.presented_at is not None and item.presented_at.date() == current_datetime.date() for item in aphorisms):
            return None, "Already presented an aphorism today."

        aphorism = select_random_aphorism_weighted(aphorisms)

        print("selected", aphorism.id, ":", aphorism.title)

        current_date_iso = current_datetime.isoformat()

        client\
            .table('aphorisms')\
            .update({'presented_at': current_date_iso})\
            .eq('id', aphorism.id)\
            .execute()

        print("set presented", aphorism.id, ":", aphorism.title)
    
        return aphorism, None