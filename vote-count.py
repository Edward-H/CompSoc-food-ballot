import json
from pprint import pprint

with open('sanitised-results.json') as data_file:
    data = json.load(data_file)

# We apply the Positional Voting system to find the winners: the ones with the
# lowest sum of ranks win.
for section in [u'pizza', u'sides', u'non-alcoholic drinks', u'alcoholic drinks',
                u'cookies', u'non-cookie food', u'pizza/unhealthy food supplier']:
    section_prefs = [ballot[section] for ballot in data]
    section_totals = {}
    total_votes = 0;
    for i in range(len(section_prefs)):
        prefs = section_prefs[i]
        for option in prefs:
            votes = sum([(option in prefs and prefs[option])
                         or len(prefs)])
            total_votes += len(prefs)
            if option in section_totals:
                section_totals[option] += votes
            else:
                section_totals[option] = votes + total_votes
    pprint(sorted(section_totals.items(), key = lambda x: x[1]))
