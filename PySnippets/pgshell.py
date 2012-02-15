## {{{ http://code.activestate.com/recipes/577468/ (r5)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Primitive shell for PostgreSQL database
## Usage:
##       pg                                (list all tables)
##       pg show databases                 (list all databases)
##       pg show schemas                   (list all schemas)
##       pg select * from some_table_name  (run query)
##
import sys
import psycopg2
import psycopg2.extras
import datetime

sql = """SELECT table_name FROM information_schema.tables where table_schema = 'postgres'"""
if len(sys.argv) > 1:
    sql = (" ".join(sys.argv[1:])).strip()
if sql == 'show databases':
    sql = 'select datname as database from pg_database'
if sql == 'show schemas':
    sql = 'select nspname as schema from pg_namespace'

#sql = 'select datname as database from pg_database'

dtstart = datetime.datetime.now()

print '\n>>>>Summary Query Starting at: %s <<<<\n' %dtstart.ctime()

sql = 'select nspname as schema from pg_namespace'
sql = 'select * from pg_summary_status'
con = psycopg2.connect(database="uroldb", host='127.0.0.1', user='postgres', password='postgres')
cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
cur.execute(sql)
rs = cur.fetchall()

if not len(rs):
    print 'No results.'
    sys.exit(-1)

first_row = rs[0]
# get sorted column names
column_names_with_indexes = [item for item in first_row._index.iteritems()]
sorted_column_names_pairs = sorted(column_names_with_indexes, key=lambda k: k[1])
sorted_column_names = [p[0] for p in sorted_column_names_pairs]

for row in rs:
    row_data =[]
    for idx, col in enumerate(row):
        row_data.append(sorted_column_names[idx].ljust(16) + ': ' + str(col).strip())
    if len(row) >1:
        print  '-'*40
    print "\n".join(row_data)

cur.close()
con.close()

dtend = datetime.datetime.now()        
elapsed = dtend - dtstart    

#print '\n >>>> Elapsed Time: <<<<<\n'
print '>>>>> Total Elapsed Time (in secs): ' + str (elapsed.seconds)
#print '>>>>> Total Elapsed Time (in microsecs): ' + str (elapsed.microseconds)
print '\n>>>>> Ending at: %s <<<<<' %dtend.ctime()
