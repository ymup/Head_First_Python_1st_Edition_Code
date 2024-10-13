##
import json
import yate
import athletemodel


def get_names_from_store():
    athletes = athletemodel.get_from_store()
    response = [athletes[each_ath].name for each_ath in athletes]
    return(response)


names = get_names_from_store()

print(yate.start_response("application/json"))
print(json.dumps(sorted(names)))
