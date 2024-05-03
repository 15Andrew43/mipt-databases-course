#!/usr/bin/env python

import csv
import sys
import xapian
import json

def index(datapath, dbpath):
    # Create or open the database we're going to be writing to.
    db = xapian.WritableDatabase(dbpath, xapian.DB_CREATE_OR_OPEN)

    # Set up a TermGenerator that we'll use in indexing.
    termgenerator = xapian.TermGenerator()
    termgenerator.set_stemmer(xapian.Stem("en"))

    with open(datapath, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            # Pick out the fields we're going to index.
            description = item.get('DESCRIPTION', u'')
            title = item.get('TITLE', u'')
            identifier = item.get('id_NUMBER', u'')
            # date_made = item.get('DATE_MADE', u'')

            # We make a document and tell the term generator to use this.
            doc = xapian.Document()
            termgenerator.set_document(doc)

            # Index each field with a suitable prefix.
            termgenerator.index_text(title, 1, 'S')
            termgenerator.index_text(description, 1, 'XD')

            # Index fields without prefixes for general search.
            termgenerator.index_text(title)
            termgenerator.increase_termpos()
            termgenerator.index_text(description)

            # Index date field
            # doc.add_value(0, date_made)

            # Store all the fields for display purposes.
            doc.set_data(json.dumps(item))

            # We use the identifier to ensure each object ends up in the
            # database only once no matter how many times we run the
            # indexer.
            idterm = u"Q" + identifier
            doc.add_boolean_term(idterm)
            db.replace_document(idterm, doc)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: %s DATAPATH DBPATH" % sys.argv[0])
        sys.exit(1)

    index(datapath=sys.argv[1], dbpath=sys.argv[2])
