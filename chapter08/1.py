##
##import json
##names = ["John", ["Johnny", "Jack"], "Michael", ["Mike", "Mikey", "Mick"]]
##print(names)
##
##to_transfer = json.dumps(names)
##print(to_transfer)
##
##from_transfer = json.loads(to_transfer)
##print(from_transfer)


def get_names_from_store():
    athletes = get_from_store()
    response = [athletes[each_ath].name for each_ath in athletes]
    return(response)


