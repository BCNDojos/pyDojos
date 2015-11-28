#!/usr/bin/env python
import os
import json
from sqlalchemy import create_engine


def get_connection():
    host = os.environ.get('KW_DB_HOST', 'localhost')
    user = os.environ.get('KW_DB_USER', 'me')
    password = os.environ.get('KW_DB_PASS', 'somepassword')
    connection_string = 'postgresql://{}:{}@{}/neo_production'
    engine = create_engine(connection_string.format(user, password, host))
    return engine.connect()


def get_contract_descriptions(n_comps=10, n_conts=1000):
    connection = get_connection()
    contracts_companies = connection.execute('''
        SELECT c_b.company_name as company_name,
               c.description_raw as contract_desc
        FROM contracts c JOIN bidders b ON b.contract_id = c.id
        JOIN (SELECT b.company_id as c_id, com.name as company_name,
                     COUNT(b.contract_id) as bidded_contracts
              FROM bidders b JOIN companies com ON b.company_id = com.id
              WHERE b.is_contract_awardee = true
              GROUP BY c_id, com.name
              ORDER BY bidded_contracts DESC LIMIT {}
             ) c_b ON c_id = b.company_id
        WHERE c.description_raw IS NOT NULL
        AND b.is_contract_awardee = true LIMIT {}'''.format(n_comps, n_conts))
    results = []
    for row in contracts_companies:
        results.append((row['contract_desc'], row['company_name']))
    return results


def get_corpus_fh():
    corpus_dir = os.path.join('.', 'tmp')
    if not os.path.exists(corpus_dir):
        os.makedirs(corpus_dir)
    corpus_file = os.path.join(corpus_dir, 'devex-corpus.json')
    return open(corpus_file,'w')


if __name__ == '__main__':
    corpus_fh = get_corpus_fh()
    contract_descriptions = get_contract_descriptions(10, 2500)
    json.dump(contract_descriptions, corpus_fh)
