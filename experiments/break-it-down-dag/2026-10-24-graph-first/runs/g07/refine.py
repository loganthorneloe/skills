import json,pathlib,copy
p=pathlib.Path(__file__).parent
d=json.loads((p/'dag.json').read_text()); old=copy.deepcopy(d)
pg='https://www.postgresql.org/docs/current/transaction-iso.html'
tr='https://www.postgresql.org/docs/current/tutorial-transactions.html'
my='https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html'
sq='https://www.sqlite.org/isolation.html'
def ev(url,loc,claim,kind='source paraphrase'):return {'url':url,'locator':loc,'exact_claim':claim,'kind':kind}
n={x['id']:x for x in d['nodes']}
locations={
'invariant':[(tr,'3.4, bank transfer, lines 21–32','The banking example requires both sides of a transfer to succeed together.'),(pg,'13.2.2, lines 102–103','Stable reads alone do not ensure application business rules.')],
 'transaction':[(tr,'3.4, lines 20, 37–45','BEGIN groups statements; COMMIT retains the result; ROLLBACK cancels updates.')],
 'atomicity':[(tr,'3.4, lines 31–32','Partial transfer updates must not survive a transaction failure.')],
 'concurrency':[(sq,'Isolation And Concurrency, lines 38–42','One connection may retain a read transaction while another updates and commits.')],
 'serial':[(pg,'13.2, lines 23–24; 13.2.3, line 110','Serial execution runs whole transactions one after another.')],
 'dependency':[(pg,'13.2.3, SUM example, lines 113–134','A transaction reads one class total and uses the result in another class; reversing execution order changes the other transaction’s read.')],
 'snapshot':[(pg,'13.2.1, lines 62–63; 13.2.2, lines 91–93','Snapshot reads exclude later commits while permitting the reader’s own prior updates.'),(sq,'Isolation And Concurrency, lines 38–41','A WAL read transaction retains its earlier view even after another connection commits.')],
 'anomaly':[(pg,'13.2.2, lines 95–104; 13.2.3, lines 113–134','Snapshot isolation can allow both read-dependent transactions to commit even when neither serial ordering matches. Updates to rows changed since the snapshot are separately rejected.')],
 'atomicity_limit':[(tr,'3.4, lines 20–32','Atomicity requires each transaction’s updates to succeed together.'),(pg,'13.2.3, lines 128–134','Both complete transactions may commit at Repeatable Read with results incompatible with serial execution.')],
 'serializable':[(pg,'13.2, line 23; 13.2.3, lines 110–112','Serializable constrains committed results to serial equivalence while allowing concurrent execution.')],
 'dirty':[(pg,'13.2, dirty read definition, line 30','A dirty read consumes a different transaction’s not-yet-committed data.')],
 'nonrepeatable':[(pg,'13.2, nonrepeatable read definition, line 35','A repeated read observes a value changed by another transaction’s intervening commit.')],
 'phantom':[(pg,'13.2, phantom read definition, line 38','A repeated condition returns a changed matching set after another transaction commits.')],
 'levels':[(pg,'13.2, Table 13.1 and lines 54–55','The table distinguishes four standard levels; PostgreSQL strengthens Read Uncommitted and Repeatable Read relative to their standard minima.')],
 'read_committed':[(pg,'13.2.1, lines 62–65','Ordinary SELECT uses a new statement snapshot; UPDATE may wait for and then use an updated row.')],
 'repeatable_read':[(pg,'13.2.2, lines 91–104','The first non-control statement establishes the retained snapshot; serialization anomalies remain possible and some updates require retries.')],
 'mechanisms':[(sq,'Isolation And Concurrency, lines 36–42','SQLite can block access or preserve older reads using WAL and reject stale snapshot promotion.'),(my,'17.7.2.1, REPEATABLE READ, lines 379–385','InnoDB distinguishes nonlocking snapshot reads from locking statements.'),(pg,'13.2.3, lines 110–112, 137–138','PostgreSQL detects unsafe dependency combinations; its dependency-tracking predicate locks do not block.')],
 'retry':[(pg,'13.2.2, line 100; 13.2.3, lines 135–144','Restart the whole failed transaction and do not rely on results from an aborted attempt.')],
 'choice':[(my,'17.7.2.1, lines 371–390, 457–459','Isolation levels and statement type change snapshot and locking behavior.'),(pg,'13.2.3, lines 142–145','Serializability helps preserve correct transaction logic but entails monitoring and possible restarts.')],
 'target':[(tr,'3.4, lines 20–32','Transactions group changes atomically.'),(pg,'13.2, Table 13.1; 13.2.2, lines 102–104; 13.2.3, lines 110–145','Isolation levels constrain anomalies; serial equivalence is stronger than stable snapshots and may require whole-transaction retries.')]
}
for id,entries in locations.items():
 n[id]['evidence']=[ev(*entry) for entry in entries];n[id]['status']='supported'
for id in ['invariant','dependency','anomaly','atomicity_limit','mechanisms','choice','target']:
 n[id]['claim_type']='Synthesis from cited passages; worked-example claims are explicitly constructed.'
n['concurrency']['answer']='A connection is one client’s conversation with the database. Two connections can each have a transaction in progress: one reads, the other writes and commits, then the first reads again. Concurrency means these transaction lifetimes overlap; CPU instructions need not execute at exactly the same instant.'
n['snapshot']['answer']='A snapshot fixes which committed row versions a read can see. Later commits can remain outside that view. PostgreSQL also lets a transaction read its own earlier writes. The snapshot’s duration depends on the isolation level; it is not automatically the whole transaction.'
n['dependency']['answer']='An application may read balances, decide whether a withdrawal is allowed, then update one balance. The decision relies on everything read, including rows it does not update. A concurrent change to those other rows can invalidate the decision.'
n['levels']['question']='How do the four named isolation levels compare?'
n['levels']['answer']='At the standard minimum: Read Uncommitted permits dirty reads; Read Committed forbids them but permits changed rereads and matching sets; Repeatable Read also forbids changed rereads but may permit phantoms; Serializable forbids all three and serialization anomalies. PostgreSQL Read Uncommitted behaves as Read Committed, and its Repeatable Read also prevents phantoms. Engine names therefore matter.'
n['read_committed']['answer']+=' PostgreSQL UPDATE is different: after waiting for a concurrent writer, it can recheck its condition against that writer’s updated row.'
n['repeatable_read']['answer']+=' An update of a row changed since the snapshot can fail and require a whole-transaction retry.'
n['retry']['answer']='In PostgreSQL, restart a transaction rejected for serialization failure, including its reads and decisions. Repeating only the write would keep the old decision. Results from an aborted attempt must not be treated as valid.'
n['target']['answer']+=' The individual transaction logic must itself preserve the application’s rules; serializable isolation cannot repair incorrect logic. Its guarantee assumes the relevant transactions participate in serializable execution.'
n['target']['evidence'].append(ev(pg,'13.2.3, lines 142–144','Preserving correctness through serializability assumes individually correct transactions and consistent Serializable use.'))
# Constructed explanation is separate from prerequisite vertices.
d['examples']=[{'id':'withdrawal','supports':['dependency','anomaly','atomicity_limit'],'type':'Original constructed schedule, not an executed database test','assumptions':['Two accounts start at 100 each.','Application rule: combined balance must remain nonnegative; individual account balances may be negative.','Both transactions use ordinary snapshot reads and update distinct existing account rows.','No extra locks or database constraint enforces the combined-total rule.','Each transaction subtracts 150 from its own account only if the total it reads is at least 150.'], 'steps':['A reads total 200.','B reads total 200 from the same starting state.','A passes its check and changes account A from 100 to -50.','B passes its check and changes account B from 100 to -50.','Both commit: total -100 violates the rule.'],'serial_comparison':'A then B leaves (-50,100): B sees total 50 and declines. B then A leaves (100,-50): A declines. Neither serial ordering yields (-50,-50).','evidence':[ev(pg,'13.2.2, lines 91–104; 13.2.3, lines 113–134','Retained snapshots can permit read-dependent writes to different rows to produce a result impossible under serial ordering.','Source semantics plus original arithmetic deduction')]}]
# Remove recommendation branch and weak motivational dependency; retain material outside graph.
choice=n['choice'];d['optional_material']=[{'role':'Application consequence, not conceptual prerequisite','material':choice}]
d['nodes']=[x for x in d['nodes'] if x['id']!='choice']
remove={('invariant','atomicity'),('concurrency','serial'),('levels','read_committed'),('levels','repeatable_read'),('read_committed','choice'),('repeatable_read','choice'),('retry','choice'),('choice','target'),('serializable','mechanisms'),('mechanisms','retry')}
d['edges']=[e for e in d['edges'] if (e['from'],e['to']) not in remove]
def edge(a,b,w):d['edges'].append({'from':a,'to':b,'why':w})
edge('transaction','serial','Whole transaction boundaries must be known before specifying noninterleaving transaction order.')
edge('read_committed','levels','The comparison explicitly uses statement-level visibility to explain Read Committed protections.')
edge('repeatable_read','levels','The comparison explicitly distinguishes stable reads and PostgreSQL’s phantom protection from serial equivalence.')
edge('concurrency','mechanisms','Blocking or rejecting an operation requires identifying the other overlapping operation whose interaction is controlled.')
edge('serializable','retry','The retry consequence follows from rejecting transactions to preserve serial equivalence.')
edge('mechanisms','target','The requested distinction between guarantees and implementations requires explaining version retention, blocking, and dependency checking.')
edge('retry','target','Serializable helps only if the application handles rejected attempts and recomputes its decisions.')
d['scope']['examples']='Original withdrawal schedule is separate from prerequisites; supported by PostgreSQL snapshot semantics and checked arithmetic.'
d['sources']=[{'url':tr,'used_sections':'3.4 transaction grouping, transfer, BEGIN/COMMIT/ROLLBACK','identity':'Official PostgreSQL 18 tutorial; scope is PostgreSQL transactional behavior.'},{'url':pg,'used_sections':'13.2 definitions and Table 13.1; 13.2.1–13.2.3','identity':'Official PostgreSQL 18 manual; standard summaries are as described by PostgreSQL, not a direct reading of the SQL standard.'},{'url':my,'used_sections':'17.7.2.1 introduction, REPEATABLE READ, READ COMMITTED, SERIALIZABLE','identity':'Official MySQL 8.4 InnoDB manual; engine-specific semantics.'},{'url':sq,'used_sections':'Isolation Between Database Connections; Isolation And Concurrency; same-connection distinction','identity':'Official SQLite project documentation, page last updated 2022-04-18; read for stable conceptual mechanisms, no performance inference.'}]
round1={'round':1,'type':'Supplemental primary-source research and reconciliation','gaps_before':['dependency','anomaly','atomicity_limit','All partial nodes needed located passage confirmation.'],'searches':[],'retrievals':[{'url':tr,'calls':'Open full tutorial'},{'url':pg,'calls':'Open initial page; open near lines 82 and 123 for complete relevant isolation sections'},{'url':my,'calls':'Open page; open near lines 336 and 470 to traverse navigation and read behavior sections'},{'url':sq,'calls':'Open page; open near line 42 for snapshot promotion and same-connection qualifications'}],'evidence':'Located passages attached to every non-assumed node. Supplied paraphrases remain the starting material. Supplemental documentation establishes read/write-dependency mechanism and precise statement exceptions.','changes':{'updated_nodes':[i for i in locations if i!='choice'],'moved_optional':['choice'],'removed_edges':[list(t) for t in sorted(remove)],'added_edges':[e for e in d['edges'] if e not in old['edges']],'added_fields':['examples','sources','optional_material'],'snapshot':'history/round-1-dag.json'},'remaining_gaps':[],'access_limits':'No relevant page access failure. No live database execution or direct SQL standard access.'}
d['revisions'].append(round1)
(p/'history/round-1.json').write_text(json.dumps(round1,indent=2)+'\n')
for path in ['dag.json','history/round-1-dag.json']:(p/path).write_text(json.dumps(d,indent=2)+'\n')
print('Round 1 saved: evidence attached; initial preserved.')
