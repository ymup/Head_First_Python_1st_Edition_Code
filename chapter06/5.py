


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return str(sorted(set([sanitize(t) for t in self]))[0:3])


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs



vera = AthleteList("Vera Vi")
vera.append("1.31")
print(vera.top3())
vera.extend(["2.22", "1-21", "2:22"])
print(vera.top3())

