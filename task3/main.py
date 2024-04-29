#!/usr/bin/env python

import json
import sys
import xapian
import time
# import support

### Start of example code.
def search(dbpath, querystring, offset=0, pagesize=10):
    # offset - defines starting point within result set
    # pagesize - defines number of records to retrieve

    # Open the database we're going to search.
    db = xapian.Database(dbpath)

    # Set up a QueryParser with a stemmer and suitable prefixes
    queryparser = xapian.QueryParser()
    queryparser.set_stemmer(xapian.Stem("en"))
    queryparser.set_stemming_strategy(queryparser.STEM_SOME)
    # Start of prefix configuration.
    queryparser.add_prefix("title", "S")
    queryparser.add_prefix("description", "XD")
    # End of prefix configuration.

    # And parse the query
    query = queryparser.parse_query(querystring)

    # Use an Enquire object on the database to run the query
    enquire = xapian.Enquire(db)
    enquire.set_query(query)

    # And print out something about each match
    matches = []
    for match in enquire.get_mset(offset, pagesize):
        fields = json.loads(match.document.get_data().decode('utf8'))
        print(u"%(rank)i: #%(docid)3.3i %(title)s" % {
            'rank': match.rank + 1,
            'docid': match.docid,
            'title': fields.get('TITLE', u''),
            })
        matches.append(match.docid)

    # Finally, make sure we log the query and displayed results
    # support.log_matches(querystring, offset, pagesize, matches)
### End of example code.


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: %s DBPATH" % sys.argv[0])
        sys.exit(1)

    dbpath = sys.argv[1]

    queries = [
        'description:\"leather case\" AND title:sundial',
        # 'title:"Ansonia Sunwatch"',
        'title:"Ansonia Sunwatch" AND id_NUMBER:"Ansonia Clock Co."',
        'description:"Ship\'s log-glass in wooden mount"',
        'title:"Model of train of wheels" AND Chicago',
        'Chicago OR TITLE:Chicago OR description:Chicago',
        'DATE_MADE:[1920 TO 1940]',
        'description:"glass"',
        'id_NUMBER:"Ansonia Clock Co." OR id_NUMBER:"Abbot Horne"',
        'description:"glass"',
        'description:"SCM - Time Measurement"',
        'description:"vintage" AND description:"glass"',
        'description:"ancient" AND description:"wood"',
        'description:"modern" AND DATE_MADE:[2000 TO 2022]',
        'description:"handcrafted" AND description:"metal"',
        'description:"antique" AND id_NUMBER:"John Smith"',
        'description:"retro" AND title:"clock"',
        'description:"classic" AND description:"Antique Clocks Collection"',
        'description:"contemporary" AND description:"Modern Timepieces Collection"',
        'description:"unique" AND description:"Sundials Showcase"',
        'description:"collectible" AND description:"Glass Instruments Collection"',
        'description:"artistic" AND description:"Timepiece Artifacts Collection"'
    ]

    for query in queries:
        print(f"Results for query '{query}':")
        
        # Засекаем время перед выполнением запроса
        start_time = time.time()
        
        search(dbpath, query)
        
        # Засекаем время после выполнения запроса
        end_time = time.time()
        
        # Вычисляем время выполнения запроса
        duration = end_time - start_time
        
        # Выводим время выполнения запроса
        print(f"Query execution time: {duration} seconds")
        print()