from datetime import datetime
from pydantic import typing

from src.graphql.aphorism import Aphorism
from src.graphql.session import client

def get_aphorisms(info) -> typing.List[Aphorism]:
    result = client.table('aphorisms').select('*').execute()
    print("HIHIHIHIHIHIHIHIHHHIHHIHIHIHIHIHHIHIHIHHHIHIHIHHIHIH")

    # TODO: Figure out error handling
    #if result.status_code != 200:
        #raise Exception("Supabase request failed.")
    
    aphorisms = []

    for row in result.data:
        aphorism = Aphorism(
            id=str(row['id']),
            title=row['title'],
            content=row['content'],
            createdAt=datetime.fromisoformat(row['created_at']),
            presentedAt=datetime.fromisoformat(row.get('presented_at')) if row.get('presented_at') else None
        )
        aphorisms.append(aphorism)

    print(result.data)
    print("to")
    print(aphorisms)

    return aphorisms