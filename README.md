# Lajihavaintoja-bot

Python script that retreives species observations from api.laji.fi (api by Finnish Biodiversity Info Facility). Requested info includes vernacular species name (in Finnish), notes written by the citizen observer, place and date.

Requested page is randomly selected and the data is parsed in a for loop. If conditions applied include whether the retreived item includes vernacular name in Finnish, the item includes notes and notes are longer than 5 characters long (to exclude uninteresting technical data)

Applicable items are stored in a list object and one list item is chosen randomly for Tweepy push.
