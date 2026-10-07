"""Provided offline contract checks, not student implementations or live-service proof.

Run: python check.py LAB01
The optional --file path supports checking a separately located implementation.
All databases are isolated in memory; existing course databases are never opened.
"""
import argparse
import copy
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'checks' / 'lessons.json'
COUNT = 0


def equal(actual, expected, label='result'):
    global COUNT
    assert actual == expected, f'{label}: expected {expected!r}; got {actual!r}'
    COUNT += 1


def near(actual, expected, label='float'):
    global COUNT
    assert math.isfinite(actual) and math.isclose(actual, expected, abs_tol=1e-10), f'{label}: {actual!r} != {expected!r}'
    COUNT += 1


def bad(function, *args, exception=ValueError, **kwargs):
    global COUNT
    try:
        function(*args, **kwargs)
    except exception:
        COUNT += 1
    else:
        raise AssertionError(f'Expected {exception.__name__} for {args!r}')


def module(path):
    spec = importlib.util.spec_from_file_location('p5_student', path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def fixture(name):
    return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))


def sql_rows(conn, path, params=()):
    sql = path.read_text(encoding='utf-8')
    cursor = conn.execute(sql, params)
    assert cursor.description, 'Expected one SELECT returning columns; implement the SQL first.'
    return [dict(zip([x[0] for x in cursor.description], row)) for row in cursor.fetchall()]


def inventory_db():
    conn = sqlite3.connect(':memory:', isolation_level=None)
    conn.executescript('''
    CREATE TABLE products(product_id TEXT PRIMARY KEY, category TEXT);
    CREATE TABLE movements(event_id TEXT PRIMARY KEY, product_id TEXT, units INTEGER);
    CREATE TABLE audits(audit_id TEXT PRIMARY KEY, event_id TEXT);
    ''')
    data = fixture('inventory.json')
    conn.executemany('INSERT INTO products VALUES(:product_id,:category)', data['products'])
    conn.executemany('INSERT INTO movements VALUES(:event_id,:product_id,:units)', data['movements'])
    conn.executemany('INSERT INTO audits VALUES(:audit_id,:event_id)', data['audits'])
    return conn


def lab01(path):
    conn = inventory_db()
    expected = [dict(product_id='p01',total_units=10,event_count=2), dict(product_id='p02',total_units=5,event_count=1), dict(product_id='p03',total_units=0,event_count=0)]
    equal(sql_rows(conn,path), expected)
    conn.execute("INSERT INTO audits VALUES('extra','M1')")
    equal(sql_rows(conn,path), expected, 'extra audit must not affect movement totals')
    conn.execute("INSERT INTO movements VALUES('new','p03',7)")
    expected[-1].update(total_units=7,event_count=1)
    equal(sql_rows(conn,path), expected)
    conn.execute("INSERT INTO movements VALUES('same-units','p01',7)")
    expected[0].update(total_units=17,event_count=3)
    equal(sql_rows(conn,path), expected, 'equal units are separate facts')
    conn.close()


def lab02(m):
    f=m.normalize_stock
    inputs=[{'api_version':1,'item':{'sku':' A ','quantity':'007'}}, {'api_version':2,'product':{'sku':'A'},'stock':{'units':7}}]
    for item in inputs:
        old=copy.deepcopy(item)
        equal(f(item),{'sku':'A','units':7})
        equal(item,old,'input mutation')
    equal(f({'api_version':1,'item':{'sku':'x','quantity':' 0 '}}),{'sku':'x','units':0})
    equal(f({'api_version':2,'product':{'sku':' B '},'stock':{'units':10000}}),{'sku':'B','units':10000})
    for item in [None,{}, {'api_version':True,'item':{}}, {'api_version':3}, {'api_version':1,'item':None}]: bad(f,item)
    for quantity in ['7.0','-1','１２','',True,10001]: bad(f,{'api_version':1,'item':{'sku':'x','quantity':quantity}})
    for units in [True,-1,10001,'7',None]: bad(f,{'api_version':2,'product':{'sku':'x'},'stock':{'units':units}})
    bad(f,{'api_version':1,'item':{'sku':' ','quantity':'7'}})


def lab03(path):
    conn=sqlite3.connect(':memory:',isolation_level=None)
    conn.execute('CREATE TABLE items(item_id TEXT PRIMARY KEY, units INTEGER NOT NULL CHECK(units >= 0))')
    conn.executemany('INSERT INTO items VALUES(?,?)',[('p01',7),('p02',3),('p03',5)])
    conn.execute(path.read_text(encoding='utf-8'))
    equal(conn.execute('SELECT item_id,units,zone FROM items ORDER BY item_id').fetchall(),[('p01',7,'unknown'),('p02',3,'unknown'),('p03',5,'unknown')])
    conn.execute("INSERT INTO items(item_id,units) VALUES('old-writer',1)")
    equal(conn.execute("SELECT zone FROM items WHERE item_id='old-writer'").fetchone(),('unknown',))
    bad(conn.execute,"INSERT INTO items VALUES('null',1,NULL)",exception=sqlite3.IntegrityError)
    bad(conn.execute,"INSERT INTO items VALUES('p01',1,'x')",exception=sqlite3.IntegrityError)
    bad(conn.execute,"INSERT INTO items VALUES('negative',-1,'x')",exception=sqlite3.IntegrityError)
    conn.execute("INSERT INTO items VALUES('new-writer',2,'north')")
    equal(conn.execute("SELECT zone FROM items WHERE item_id='new-writer'").fetchone(),('north',))
    conn.close()


def lab04(m):
    f=m.plan_windows
    equal(f('2024-02-28T00:00:00+00:00','2024-03-03T00:00:00+00:00',3),[('2024-02-28T00:00:00+00:00','2024-03-02T00:00:00+00:00'),('2024-03-02T00:00:00+00:00','2024-03-03T00:00:00+00:00')])
    equal(f('2025-12-31T07:00:00+07:00','2026-01-02T07:00:00+07:00',1),[('2025-12-31T00:00:00+00:00','2026-01-01T00:00:00+00:00'),('2026-01-01T00:00:00+00:00','2026-01-02T00:00:00+00:00')])
    for start,end,days in [('2026-01-01','2026-01-02',1),('bad','2026-01-02T00:00:00+00:00',1),('2026-01-01T01:00:00+00:00','2026-01-02T00:00:00+00:00',1),('2026-01-02T00:00:00+00:00','2026-01-01T00:00:00+00:00',1)]: bad(f,start,end,days)
    for days in [0,-1,True,1.5]: bad(f,'2026-01-01T00:00:00+00:00','2026-01-02T00:00:00+00:00',days)


def stock_db():
    conn=sqlite3.connect(':memory:',isolation_level=None)
    conn.execute('CREATE TABLE items(item_id TEXT PRIMARY KEY, units INTEGER NOT NULL CHECK(units >= 0))')
    conn.execute('CREATE TABLE ledger(batch_id TEXT PRIMARY KEY, payload_sha TEXT NOT NULL)')
    conn.executemany('INSERT INTO items VALUES(?,?)',[('p01',10),('p02',5)])
    return conn


def stock_snapshot(conn):
    return (conn.execute('SELECT * FROM items ORDER BY item_id').fetchall(),conn.execute('SELECT * FROM ledger ORDER BY batch_id').fetchall())


def lab05(m):
    f=m.apply_batch
    conn=stock_db()
    changes=[{'item_id':'p01','delta':-3},{'item_id':'p02','delta':2}]
    old=copy.deepcopy(changes)
    initial=stock_snapshot(conn)
    bad(f,conn,'b1',changes,fail_after=1,exception=RuntimeError)
    equal(stock_snapshot(conn),initial,'crash rollback')
    equal(f(conn,'b1',changes),{'status':'applied','rows':2})
    equal(conn.execute('SELECT * FROM items ORDER BY item_id').fetchall(),[('p01',7),('p02',7)])
    after=stock_snapshot(conn)
    equal(f(conn,'b1',changes),{'status':'replay','rows':0})
    equal(stock_snapshot(conn),after,'replay')
    bad(f,conn,'b1',[{'item_id':'p01','delta':-2}])
    equal(stock_snapshot(conn),after,'conflict preserves both tables')
    for change in [[{'item_id':'missing','delta':1}],[{'item_id':'p01','delta':-999}],[{'item_id':'p01','delta':True}],[{'item_id':'p01','delta':1,'extra':0}]]:
        bad(f,conn,'bad',change)
        equal(stock_snapshot(conn),after)
    equal(f(conn,'empty',[]),{'status':'applied','rows':0})
    equal(f(conn,'twice',[{'item_id':'p02','delta':1},{'item_id':'p02','delta':1}]),{'status':'applied','rows':2})
    equal(conn.execute("SELECT units FROM items WHERE item_id='p02'").fetchone(),(9,))
    equal(changes,old,'input mutation')
    conn.execute('BEGIN')
    bad(f,conn,'borrowed',[])
    equal(conn.in_transaction,True,'caller transaction remains owned')
    conn.rollback()
    conn.close()


def lab06(m):
    f=m.enrich_movements
    rows=[{'sku':' p01 ','units':7},{'sku':'unknown','extra':2,'category':'old'}]
    products=[{'sku':'p01','category':'hardware'}]
    original=copy.deepcopy((rows,products))
    result=f(rows,products)
    equal(result,[{'sku':' p01 ','units':7,'category':'hardware'},{'sku':'unknown','extra':2,'category':None}])
    equal((rows,products),original,'mutation')
    result[0]['units']=99
    equal(rows[0]['units'],7,'result row must be copied')
    bad(f,rows,products+[{'sku':' p01 ','category':'hardware'}])
    bad(f,[{'sku':None}],products)
    bad(f,rows,[{'sku':' ','category':'x'}])
    equal(f([],products),[])
    equal(f([{'sku':'q9'}],[{'sku':'q9','category':'new'}]),[{'sku':'q9','category':'new'}])


def lab07(m):
    f=m.classify_run
    events=[{'stage':s,'attempt':1,'status':'succeeded'} for s in ['load','quality','publish']]
    events += [{'stage':'extract','attempt':2,'status':'succeeded'},{'stage':'extract','attempt':1,'status':'failed'}]
    old=copy.deepcopy(events)
    expected={'status':'succeeded','retry_count':1,'failed_stages':[],'missing_stages':[]}
    equal(f(events),expected)
    equal(f(list(reversed(events))+[events[0]]),expected)
    equal(events,old)
    equal(f([]),{'status':'incomplete','retry_count':0,'failed_stages':[],'missing_stages':['extract','load','publish','quality']})
    equal(f([{'stage':'load','attempt':3,'status':'failed'}]),{'status':'failed','retry_count':2,'failed_stages':['load'],'missing_stages':['extract','publish','quality']})
    bad(f,events+[{'stage':'extract','attempt':1,'status':'succeeded'}])
    for event in [{'stage':'x','attempt':1,'status':'failed'},{'stage':'load','attempt':True,'status':'failed'},{'stage':'load','attempt':1,'status':'running'}]: bad(f,[event])


def cl02(m):
    f=m.object_key
    equal(f('b-001','changes.jsonl'),'raw/b-001/changes.jsonl')
    equal(f('B_2','x.csv'),'raw/B_2/x.csv')
    for batch,filename in [('../x','x.json'),('','x.json'),('x','../x.json'),('x','a.b.json'),('x','x.JSON'),('x','x.txt'),('x','folder/x.json'),(True,'x.json'),('x'*65,'x.json')]: bad(f,batch,filename)


def cl03(m):
    f=m.validate_job_config
    config=dict(tasks=1,max_retries=1,timeout_seconds=120,memory_mib=512)
    result=f(config)
    equal(result,config)
    result['timeout_seconds']=1
    equal(config['timeout_seconds'],120,'copy')
    for key,value in [('tasks',2),('tasks',True),('max_retries',3),('max_retries',-1),('timeout_seconds',301),('timeout_seconds',0),('memory_mib',513)]:
        bad(f,dict(config,**{key:value}))
    bad(f,dict(config,extra=1))
    bad(f,{'tasks':1})
    equal(f(dict(tasks=1,max_retries=0,timeout_seconds=300,memory_mib=2048))['memory_mib'],2048)


def history_db():
    conn=sqlite3.connect(':memory:',isolation_level=None)
    conn.execute('CREATE TABLE history(event_id TEXT, sku TEXT, observed_at TEXT, version INTEGER, units INTEGER, op TEXT)')
    batches=fixture('batches.json')
    conn.executemany('INSERT INTO history VALUES(:event_id,:sku,:observed_at,:version,:units,:op)',batches['b1']+batches['b2'])
    return conn


def cl04(path):
    conn=history_db()
    batches=fixture('batches.json')
    expected=sorted([batches['b2'][0],batches['b2'][1],batches['b2'][2]],key=lambda r:r['event_id'])
    equal(sql_rows(conn,path),expected)
    conn.execute('INSERT INTO history VALUES(:event_id,:sku,:observed_at,:version,:units,:op)',batches['b1'][0])
    equal(sql_rows(conn,path),expected,'identical history replay')
    changed=dict(expected[0],version=3,units=9)
    conn.execute('INSERT INTO history VALUES(:event_id,:sku,:observed_at,:version,:units,:op)',changed)
    expected[0]=changed
    equal(sql_rows(conn,path),expected,'new version')
    conn.close()


def cl05(m):
    f=m.role_plan
    expected=[{'resource':'output_bucket','role':'roles/storage.objectCreator'},{'resource':'output_bucket','role':'roles/storage.objectViewer'},{'resource':'raw_bucket','role':'roles/storage.objectViewer'}]
    equal(f(['read_raw','write_output','read_raw']),expected)
    all_roles=[{'resource':'dataset','role':'roles/bigquery.dataEditor'}]+expected[:2]+[{'resource':'project','role':'roles/bigquery.jobUser'}]+expected[2:]
    equal(f(['load_warehouse','write_output','read_raw']),all_roles)
    equal(f([]),[])
    bad(f,['owner'])
    bad(f,'read_raw')
    bad(f,[None])


def cl06(m):
    f=m.build_scheduler_target
    expected={'uri':'https://run.googleapis.com/v2/projects/demo-p5/locations/asia-southeast1/jobs/p5-batch:run','httpMethod':'POST','headers':{'Content-Type':'application/json'},'body':'e30=','oauthToken':{'serviceAccountEmail':'p5-scheduler@demo-p5.iam.gserviceaccount.com'}}
    equal(f('demo-p5','asia-southeast1','p5-batch','p5-scheduler@demo-p5.iam.gserviceaccount.com'),expected)
    for args in [('Demo','asia-southeast1','p5-batch','p5-scheduler@Demo.iam.gserviceaccount.com'),('demo-p5','bad','p5-batch','p5-scheduler@demo-p5.iam.gserviceaccount.com'),('demo-p5','asia-southeast1','../job','p5-scheduler@demo-p5.iam.gserviceaccount.com'),('demo-p5','asia-southeast1','p5-batch','p5-scheduler@other.iam.gserviceaccount.com')]: bad(f,*args)
    result=f('demo-p5','us-central1','a','p5-runtime@demo-p5.iam.gserviceaccount.com')
    equal(result['uri'].endswith('/jobs/a:run'),True)


def cl07(m):
    f=m.allow_query
    equal(f(100,100),True)
    equal(f(101,100),False)
    equal(f(0,0),True)
    equal(type(f(100,100)),bool,'return a boolean, not an integer')
    for args in [(-1,100),(True,100),(100,False),(1.0,100),(1,-2),(None,1)]: bad(f,*args)


def ai01(m):
    f=m.canonical_document
    doc=fixture('documents.json')['b1'][0]
    raw=dict(doc,id=' d-ops ',source_uri=' local://ops.md ',extra='retained')
    original=copy.deepcopy(raw)
    equal(f(raw),doc)
    equal(raw,original)
    for key,value in [('id','../x'),('id',''),('version',True),('version',0),('source_uri','ftp://x'),('source_uri','https://'),('text',' '),('text','a'*100001)]: bad(f,dict(doc,**{key:value}))
    bad(f,{k:v for k,v in doc.items() if k!='source_uri'})


def ai02(m):
    f=m.normalize_text
    equal(f('  Alpha  \r\n\r\n\r\n Beta  '),'Alpha\n\nBeta')
    equal(f(' e\u0301 \r a  b \r\r z '),'é\na  b\n\nz')
    equal(f(' \t\r\n '),'')
    text=' é \n\n\n beta '
    equal(f(f(text)),f(text),'idempotence')
    bad(f,None)


def ai03(m):
    f=m.chunk_document
    expected=[dict(chunk_id=f'd:2:{s}:{e}',doc_id='d',version=2,start=s,end=e,text='abcdefghij'[s:e]) for s,e in [(0,4),(3,7),(6,10)]]
    equal(f('d',2,'abcdefghij',4,1),expected)
    equal(f('d',2,'abcd',4,1),expected[:1])
    equal(f('x',1,'',3,0),[])
    unicode=f('x',1,'aé🙂b',2,0)
    equal([c['text'] for c in unicode],['aé','🙂b'])
    for args in [('d',1,'x',0,0),('d',1,'x',4,4),('d',1,'x',4,-1),('d',True,'x',4,1),('d',1,'x',True,0),('d',1,None,4,0),('../x',1,'x',4,0)]: bad(f,*args)


def ai04(path):
    conn=sqlite3.connect(':memory:')
    conn.execute('CREATE VIRTUAL TABLE chunks USING fts5(chunk_id UNINDEXED,doc_id UNINDEXED,text)')
    docs=fixture('documents.json')['b1']
    conn.executemany('INSERT INTO chunks VALUES(?,?,?)',[(d['id']+':1',d['id'],d['text']) for d in docs])
    rows=sql_rows(conn,path,{'query':'cursor','limit':2})
    equal([r['doc_id'] for r in rows],['d-api'])
    equal(set(rows[0]),{'chunk_id','doc_id','text','score'})
    equal(sql_rows(conn,path,{'query':'absentzz','limit':2}),[])
    equal([r['doc_id'] for r in sql_rows(conn,path,{'query':'timezone','limit':1})],['d-time'])
    conn.executemany('INSERT INTO chunks VALUES(?,?,?)',[('z','tie','orbit'),('a','tie','orbit')])
    equal([r['chunk_id'] for r in sql_rows(conn,path,{'query':'orbit','limit':2})],['a','z'])
    conn.close()


def ai05(m):
    near(m.cosine([1,0,0],[-1,0,0]),-1)
    near(m.cosine([1e300,1e300],[1e300,1e300]),1)
    near(m.cosine([1.7e308,1.7e308],[1.7e308,1.7e308]),1)
    candidates=[{'chunk_id':'n3','vector':[-1,0,0]},{'chunk_id':'n2','vector':[0.8,0.6,0]},{'chunk_id':'n1','vector':[1,0,0]}]
    old=copy.deepcopy(candidates)
    result=m.rank_vectors([1,0,0],candidates,3)
    equal([r['chunk_id'] for r in result],['n1','n2','n3'])
    for r,v in zip(result,[1,0.8,-1]): near(r['score'],v)
    equal(m.rank_vectors([1,0],[{'chunk_id':'z','vector':[1,0]},{'chunk_id':'a','vector':[1,0]}],1)[0]['chunk_id'],'a')
    equal(candidates,old)
    for a,b in [([],[]),([0,0],[1,0]),([1],[1,2]),([True],[1]),([float('nan')],[1]),([1],[float('inf')])]: bad(m.cosine,a,b)
    bad(m.rank_vectors,[1,0],candidates,1)
    bad(m.rank_vectors,[1,0,0],candidates+[candidates[0]],1)
    bad(m.rank_vectors,[1,0,0],candidates,True)
    bad(m.rank_vectors,[0,0],[],1)
    equal(m.rank_vectors([1,0],[],1),[])


def ai06(m):
    f=m.index_actions
    old=dict(id='d-api',version=1,op='upsert',chunk_ids=['a','b'],content_sha='a'*64)
    new=dict(id='d-api',version=2,op='upsert',chunk_ids=['c'],content_sha='b'*64)
    original=copy.deepcopy((old,new))
    result=f(old,new)
    equal(result,{'state':new,'remove':['a','b'],'add':['c']})
    equal((old,new),original)
    result['state']['chunk_ids'].append('mutated')
    equal(new['chunk_ids'],['c'],'nested copy')
    deleted=dict(id='d-api',version=3,op='delete',chunk_ids=[],content_sha=None)
    equal(f(new,deleted),{'state':deleted,'remove':['c'],'add':[]})
    equal(f(deleted,new),{'state':deleted,'remove':[],'add':[]})
    equal(f(new,new),{'state':new,'remove':[],'add':[]})
    equal(f(None,new),{'state':new,'remove':[],'add':['c']})
    bad(f,new,dict(new,content_sha='c'*64))
    bad(f,new,dict(new,id='other'))
    bad(f,None,dict(new,chunk_ids=['c','c']))
    bad(f,None,dict(deleted,chunk_ids=['x']))
    bad(f,None,dict(new,version=True))


def ai07(m):
    f=m.score_ranking
    equal(f(['a','a','b','c'],['b'],2),{'precision_at_k':0.5,'recall_at_k':1.0,'mrr_at_k':0.5})
    equal({type(v) for v in f(['a'],['a'],1).values()},{float},'metric values are floats')
    equal(f(['a'],['a','b','b'],3),{'precision_at_k':1/3,'recall_at_k':0.5,'mrr_at_k':1.0})
    equal(f([],[],2),{'precision_at_k':0.0,'recall_at_k':0.0,'mrr_at_k':0.0})
    equal(f(['a'],['b'],1),{'precision_at_k':0.0,'recall_at_k':0.0,'mrr_at_k':0.0})
    for args in [(['a'],['a'],0),(['a'],['a'],True),([None],['a'],1),('a',['a'],1)]: bad(f,*args)


def st02(m):
    event=fixture('batches.json')['b1'][0]
    old=copy.deepcopy(event)
    expected=json.dumps(event,sort_keys=True,separators=(',',':')).encode('utf-8')
    equal(m.encode_event(event),expected)
    equal(m.encode_event(dict(reversed(list(event.items())))),expected)
    equal(m.event_key(event),b'M1')
    equal(event,old)
    for key,value in [('version',True),('units',True),('units',-1),('sku',' p01 '),('observed_at','2026-01-01'),('op','bad')]:
        for f in [m.encode_event,m.event_key]: bad(f,dict(event,**{key:value}))
    for f in [m.encode_event,m.event_key]:
        bad(f,dict(event,op='delete',units=7))
        bad(f,dict(event,extra=1))


def st03(m):
    f=m.safe_offsets
    records=[dict(topic='t',partition=0,offset=o,status=s) for o,s in [(3,'processed'),(4,'failed'),(5,'processed')]]
    records += [dict(topic='t',partition=1,offset=o,status='processed') for o in [0,1]]
    original=copy.deepcopy(records)
    equal(f(list(reversed(records))+[records[0]]),[dict(topic='t',partition=0,offset=4),dict(topic='t',partition=1,offset=2)])
    equal(f([dict(topic='t',partition=0,offset=o,status='processed') for o in [3,7]]),[dict(topic='t',partition=0,offset=8)])
    equal(f([dict(topic='t',partition=0,offset=3,status='failed')]),[])
    equal(f([]),[])
    bad(f,[records[0],dict(records[0],status='failed')])
    bad(f,[dict(records[0],offset=True)])
    bad(f,[dict(records[0],partition=-1)])
    equal(records,original)


def stream_db():
    conn=sqlite3.connect(':memory:',isolation_level=None)
    conn.executescript('''CREATE TABLE entity_state(event_id TEXT PRIMARY KEY,sku TEXT NOT NULL,observed_at TEXT NOT NULL,version INTEGER NOT NULL,units INTEGER NOT NULL,op TEXT NOT NULL);
    CREATE TABLE message_ledger(topic TEXT NOT NULL,partition_id INTEGER NOT NULL,offset_id INTEGER NOT NULL,payload_sha TEXT NOT NULL,PRIMARY KEY(topic,partition_id,offset_id));''')
    return conn


def stream_snapshot(conn):
    return (conn.execute('SELECT * FROM entity_state ORDER BY event_id').fetchall(),conn.execute('SELECT * FROM message_ledger ORDER BY topic,partition_id,offset_id').fetchall())


def st04(m):
    f=m.apply_event
    conn=stream_db()
    b=fixture('batches.json')
    events=b['b1']+b['b2']
    for offset,event in enumerate(events): equal(f(conn,event,dict(topic='t',partition=0,offset=offset)),{'status':'applied'})
    equal(conn.execute("SELECT SUM(units) FROM entity_state WHERE op='upsert'").fetchone(),(13,))
    after=stream_snapshot(conn)
    equal(f(conn,events[-1],dict(topic='t',partition=0,offset=4)),{'status':'replay'})
    equal(stream_snapshot(conn),after)
    bad(f,conn,dict(events[-1],units=6),dict(topic='t',partition=0,offset=4))
    bad(f,conn,dict(events[-1],units=6),dict(topic='t',partition=0,offset=5))
    equal(stream_snapshot(conn),after,'conflicts rollback')
    equal(f(conn,events[0],dict(topic='t',partition=0,offset=5)),{'status':'stale'})
    equal(f(conn,events[-1],dict(topic='t',partition=0,offset=6)),{'status':'replay'})
    checkpoint=stream_snapshot(conn)
    bad(f,conn,dict(events[-1],version=2,units=6),dict(topic='t',partition=0,offset=7),fail_before_commit=True,exception=RuntimeError)
    equal(stream_snapshot(conn),checkpoint,'both tables rollback')
    bad(f,conn,dict(events[-1],version=True),dict(topic='t',partition=0,offset=7))
    bad(f,conn,events[-1],dict(topic='t',partition=0,offset=True))
    conn.execute('BEGIN')
    bad(f,conn,events[-1],dict(topic='t',partition=0,offset=7))
    equal(conn.in_transaction,True)
    conn.rollback()
    conn.close()


def st05(m):
    f=m.build_rejection
    position=dict(topic='t',partition=0,offset=4)
    equal(f(position,b'bad','invalid JSON'),dict(position,payload_sha=hashlib.sha256(b'bad').hexdigest(),reason='invalid JSON'))
    equal(position,dict(topic='t',partition=0,offset=4))
    for pos,payload,reason in [(dict(position,offset=True),b'x','bad'),(position,'bad','bad'),(position,bytearray(b'x'),'bad'),(position,b'x',' bad '),(position,b'x','bad\nline'),(position,b'x','x'*121),(position,b'x'*1048577,'bad')]: bad(f,pos,payload,reason)
    equal(f(position,b'','empty')['payload_sha'],hashlib.sha256(b'').hexdigest())


def st06(m):
    f=m.decode_cdc
    events=fixture('cdc.json')
    expected=[dict(kind='upsert',event_id='M1',row=dict(event_id='M1',sku='p01',units=7),source_lsn=100),dict(kind='upsert',event_id='M1',row=dict(event_id='M1',sku='p01',units=8),source_lsn=110),dict(kind='delete',event_id='M2',row=None,source_lsn=120),dict(kind='tombstone',event_id=None,row=None,source_lsn=None)]
    old=copy.deepcopy(events)
    equal([f(x) for x in events],expected)
    equal(f({'schema':{},'payload':events[0]}),expected[0])
    equal(f({'payload':None}),expected[-1])
    equal(events,old)
    result=f(events[0])
    result['row']['units']=99
    equal(events[0]['after']['units'],7,'row copy')
    bad(f,dict(events[0],op='t'))
    bad(f,dict(events[0],after=dict(events[0]['after'],units=True)))
    bad(f,dict(events[0],source={'lsn':True}))
    bad(f,dict(events[2],before={}))
    equal(f(dict(events[0],source={}))['source_lsn'],None)


CHECKS={
    'LAB01':lab01,'LAB02':lab02,'LAB03':lab03,'LAB04':lab04,'LAB05':lab05,'LAB06':lab06,'LAB07':lab07,
    'CL02':cl02,'CL03':cl03,'CL04':cl04,'CL05':cl05,'CL06':cl06,'CL07':cl07,
    'AI01':ai01,'AI02':ai02,'AI03':ai03,'AI04':ai04,'AI05':ai05,'AI06':ai06,'AI07':ai07,
    'ST02':st02,'ST03':st03,'ST04':st04,'ST05':st05,'ST06':st06,
}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('lesson',choices=sorted(CHECKS))
    parser.add_argument('--file',type=Path,help='Alternate implementation for this same contract')
    args=parser.parse_args()
    entries=json.loads(MANIFEST.read_text(encoding='utf-8'))
    entry=next(x for x in entries if x['id']==args.lesson)
    path=args.file or ROOT/entry['path']/entry['file']
    try:
        target=path if path.suffix=='.sql' else module(path)
        CHECKS[args.lesson](target)
    except NotImplementedError as exc:
        print(f'FAIL {args.lesson}: {exc}')
        return 1
    except Exception as exc:
        print(f'FAIL {args.lesson}: {type(exc).__name__}: {exc}')
        return 1
    print(f'PASS {args.lesson}: {COUNT} offline assertions; live evidence is separate.')
    return 0


if __name__=='__main__':
    sys.exit(main())
