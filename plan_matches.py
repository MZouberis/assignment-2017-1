import sys
import pprint

given_file = sys.argv[1]
file = open(given_file, "r")

fixtures = {}
matches = []

with file as input_file:
  for line in input_file:
    matches.append(line.split())

for match in matches:
  if len(fixtures) == 0:
    fixtures[0] = match
  else:
    for day in fixtures:
      teams_per_day = [y for x in fixtures[day] for y in x]
      if match[0] not in teams_per_day and match[1] not in teams_per_day:
        if match not in [y for x in fixtures.values() for y in x]:
          # import code; code.interact(local=dict(globals(), **locals()))
          fixtures[day] = fixtures[day] + [match]
    if match not in [y for x in fixtures.values() for y in x]:
      fixtures[len(fixtures)] = match
file.close()
pprint.pprint(fixtures)
