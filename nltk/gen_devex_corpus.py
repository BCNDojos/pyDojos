#!/usr/bin/env python

import os
import re
import json
from sqlalchemy import create_engine
from bs4 import BeautifulSoup


host = os.environ.get('KW_DB_HOST', 'localhost')
user = os.environ.get('KW_DB_USER', 'me')
password = os.environ.get('KW_DB_PASS', 'somepassword')

engine = create_engine(
            'postgresql://{}:{}@{}/neo_production'.format(user, password, host)
         )
connection = engine.connect()


def get_contract_descriptions(max_companies=10, max_contracts=1000):
    contracts_companies = connection.execute('''
        SELECT c_b.company_name as company_name,
               c.description_raw as contract_desc
        FROM contracts c
        JOIN bidders b ON b.contract_id = c.id
        JOIN (
              SELECT b.company_id as c_id, com.name as company_name,
                     COUNT(b.contract_id) as bidded_contracts
              FROM bidders b
              JOIN companies com ON b.company_id = com.id
              GROUP BY c_id, com.name
              ORDER BY bidded_contracts DESC
              LIMIT {}
             ) c_b ON c_id = b.company_id
        WHERE c.description_raw IS NOT NULL
        LIMIT {}'''.format(max_companies, max_contracts))

    results = []
    for row in contracts_companies:
        bs_contract_desc = BeautifulSoup(row['contract_desc'], 'html.parser')
        contract_desc = bs_contract_desc.get_text().strip().replace("\n", ' ')
        results.append((re.sub(' +', ' ', contract_desc), row['company_name']))
    return results


if __name__ == '__main__':
    corpus_dir = os.path.join('.', 'tmp')
    if not os.path.exists(corpus_dir):
        os.makedirs(corpus_dir)
    corpus_file = os.path.join(corpus_dir, 'devex-corpus.json')
    corpus_fh = open(corpus_file,'w')
    json.dump(get_contract_descriptions(10, 2500), corpus_fh)
