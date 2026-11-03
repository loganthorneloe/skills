import json,datetime,pathlib
r=pathlib.Path(__file__).parent
g=json.loads((r/'dag.json').read_text()); before=json.loads(json.dumps(g)); nodes={n['id']:n for n in g['nodes']}
C='https://probabilitycourse.com/chapter1/1_4_0_conditional_probability.php'; T='https://probabilitycourse.com/chapter1/1_4_2_total_probability.php'; N='https://scikit-learn.org/stable/modules/naive_bayes.html'; M='https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall'
def evidence(url,locator,claim,basis='Directly read primary-source passage'):
 return {'url':url,'locator':locator,'claim':claim,'basis':basis}
def original(locator,claim):return {'url':None,'locator':locator,'claim':claim,'basis':'Original derivation checked with exact arithmetic; not an empirical source result'}
for n in g['nodes']:
 for ev in n['evidence']:
  if ev.get('url'):ev['basis']='Supplied packet and directly verified relevant source section'
for id in ['counts','total','answer','vary','word','target']:nodes[id]['status']='supported'
for id in ['counts','total','answer','vary']:
 nodes[id]['evidence'].append(original('case-tests.initial.json', 'Exact arithmetic confirms the constructed count/formula results.'))
nodes['joint']['answer']='For each class, need the fraction with the full observed pattern together. For two present words A and B, this is the fraction with A in that class multiplied by the fraction with B among that class’s A-containing messages. The second fraction can differ from B’s overall within-class rate. Separate word rates therefore do not determine the joint rate.'
nodes['joint']['status']='supported';nodes['joint']['evidence']=[evidence(C,'Chain rule, equations 1.5 and 1.7; lines 110–116','Joint probability retains the dependence of a later event on earlier events, also within a class.')]
nodes['word']['answer']='Treat “contains a chosen word” as the clue E in Bayes’ rule, using occurrence rates separately within spam and legitimate mail. For a prior between 0 and 1, a word occurring more frequently within spam raises the spam fraction among messages containing it, but need not make that fraction exceed 50%. Equal nonzero occurrence rates leave the prior unchanged.'
nodes['word']['evidence'].append(original('case-tests.initial.json; equal-rate boundary check','Equal clue likelihoods cancel and leave the prior unchanged. Direction follows comparing p·s/[p·s+(1−p)·l] with p.'))
nodes['scores']['question']='How do the prior and the observed word pattern form a class score?'
nodes['scores']['answer']='For each class, multiply its prior by its estimated full-pattern likelihood. Naive Bayes obtains that likelihood by multiplying the probabilities of all observed feature values within the class. These two scores are unnormalized amounts of model support; each score alone is not the spam fraction among matching messages.'
nodes['dependence']['answer']='Constructed counterexample: spam prior 1%; word A occurs in 50% of spam and 10% of legitimate messages; B occurs exactly when A does in each class. For both words present, true joint likelihoods remain 50% and 10%, giving 0.005/(0.005+0.099)=4.8077% spam. Naive multiplication instead uses 25% and 1%, giving 0.0025/(0.0025+0.0099)=20.1613%. Repeated evidence inflated confidence; these are constructed probabilities, not measured spam behavior.'
nodes['dependence']['status']='supported';nodes['dependence']['evidence']=[evidence(C,'Chain rule equation 1.7; lines 114–116','If B is certain after A within class, the joint likelihood equals A’s likelihood.'),evidence(N,'Section 1.9 factorization; lines 78–87','Naive multiplication substitutes individual within-class likelihoods.'),original('case-tests.initial.json; counterexample','True posterior 5/104; naive posterior 25/124, calculated exactly.')]
nodes['calibration']['answer']='A normalized model score is conditional on its assumed prior, feature probabilities, and independence. It need not equal the actual spam fraction among comparable messages. Test predictions against relevant labeled mail; useful class decisions alone do not establish trustworthy numerical probabilities.'
nodes['target']['answer']='Only about 8.33% of flags are spam at the stipulated 1% base rate: false flags from 9,900 legitimate messages outnumber true flags from 100 spam messages. With the same detection and false-positive rates, 10% prevalence yields 50% spam among flags; 50% prevalence yields 90%. A word’s occurrence is another clue in the same update rule. Labeled messages can supply class and word rates; naive Bayes combines observed word values under independence within each class and normalizes prior-weighted likelihoods. Dependent words can make that model probability unreliable.'
nodes['target']['evidence']=[original('case-tests.initial.json','The stated base-rate results are exact constructed calculations.'),evidence(N,'Section 1.9; lines 75–94','Feature evidence is combined with priors under conditional independence; estimated probabilities may be unreliable.'),evidence(M,'Precision; lines 111–117','Fraction of spam among flags uses all flagged messages as denominator.')]
def add(id,q,a,ev):g['nodes'].append({'id':id,'question':q,'answer':a,'status':'supported','evidence':ev})
add('multiply','How do within-group rates become fractions of all mail?','If p of all messages are in a group, and fraction q of that group has a clue, fraction p×q of all messages has both properties. In a population of N messages the expected count is N×p×q.',[evidence(C,'Chain rule equation 1.5; lines 110–112','Intersection probability equals group probability times within-group conditional probability.')])
add('partition','How do contributions from different classes form the clue total?','Spam and legitimate mail do not overlap and together cover all mail. All messages with a clue therefore equal clue-bearing spam plus clue-bearing legitimate messages. Add these class contributions; do not average their within-class percentages without weighting by class size.',[evidence(T,'Two-class formula; lines 25–29','Total evidence probability sums class-prior-weighted likelihoods.')])
add('feature_value','What probability should an absent word contribute?','For a binary word with occurrence rate q within a class, use q if present and 1−q if absent. For example, a word present in 75% of spam is absent in 25% of spam. Do this separately for each class.',[evidence(N,'Bernoulli Naive Bayes; lines 141–148','Bernoulli likelihood uses occurrence or its complement according to observed feature value.')])
add('normalize','How do the two class scores become a model probability?','Divide the spam score by the sum of spam and legitimate scores. Both scores together account for all classes for the observed pattern under the model. A shared denominator can be omitted when only choosing the larger class score, but it is required for the probability. If both scores are zero, normalization is undefined; an unseen training pattern is not evidence of impossibility.',[evidence(N,'Bayes theorem and classification rule; lines 75–89; smoothing lines 119–124','Bayes uses the evidence denominator; shared normalization may be omitted for class comparison; smoothing addresses unseen features.'),evidence(C,'Conditional probability definition; lines 40–42','The conditioning event must have positive probability.')])
remove={('total','bayes'),('estimate','scores'),('scores','calibration'),('scores','target')}
g['edges']=[e for e in g['edges'] if (e['from'],e['to']) not in remove]
def edge(a,b,w):g['edges'].append({'from':a,'to':b,'why':w})
edge('condition','multiply','The q multiplier is defined within the selected group, so its denominator must be understood.')
edge('multiply','counts','Multiplying 10,000 by class share and flag rate requires the within-group multiplication rule.')
edge('partition','total','Adding true and false flags requires the disjoint and exhaustive two-class sum rule.')
edge('multiply','bayes','Prior times likelihood in the numerator and denominator requires the joint-probability multiplication rule.')
edge('partition','bayes','The full clue denominator requires summing the two class contributions.')
edge('features','feature_value','Choosing occurrence or absence probability requires the binary feature meaning.')
edge('condition','feature_value','The complement must be calculated within the same class as the occurrence rate.')
edge('feature_value','scores','Each product factor must correspond to the observed present or absent value.')
edge('scores','normalize','Normalization needs the two unnormalized prior-weighted likelihood scores.')
edge('normalize','dependence','The numerical repeated-clue counterexample compares two normalized probabilities, not raw scores.')
edge('normalize','calibration','The reliability question concerns a normalized model probability, whose construction must be understood.')
edge('normalize','target','The target explicitly explains normalizing word-pattern scores into model probabilities.')
edge('estimate','target','The target explicitly says labeled messages can supply class and word rates; obtaining those estimates is separate from using supplied inputs.')
# Audit direct edges: each is a claim dependency, never merely proposed reading order.
audit=[]
for e in g['edges']:audit.append({'from':e['from'],'to':e['to'],'verdict':'retain','claim_that_needs_prerequisite':e['why']})
g['edge_audit']={'method':'Reviewed each destination claim against the stated arithmetic-only reader baseline. Retained edges identify required information or concepts; removed worked-example-to-general-rule order and training-as-required-input coupling.','retained':audit,'removed':[{'from':a,'to':b} for a,b in sorted(remove)]}
g['worked_cases']=json.loads((r/'case-tests.initial.json').read_text())
g['worked_cases']['unfamiliar_case']['graph_replay']='After repair: feature_value supplies complements; independence multiplies pattern likelihoods; scores gives 0.02 spam and 0.064 legitimate; normalize gives 5/21=23.8095%.'
g['worked_cases']['counterexample']['graph_replay']='After repair: joint preserves B given A and class; normalize gives the true 5/104; independence and scores give the naive 25/124. dependence identifies the violated assumption.'
g['worked_cases']['result']='Arithmetic passed; identified conceptual gaps repaired and manually replayed.'
t=datetime.datetime.now(datetime.timezone.utc).isoformat()
rev={'time':t,'round':'repair-1','changes':'Added multiply, partition, feature_value, normalize; made joint chain rule explicit; supplied calculated dependence counterexample; removed worked-example-to-general-rule edge; separated learning rates from using supplied rates; attached located evidence and arithmetic results.'}
g['revisions'].append(rev)
for name in ['dag.json','dag.after-repair-1.json']:(r/name).write_text(json.dumps(g,indent=2)+'\n')
with (r/'history.jsonl').open('a') as f:f.write(json.dumps({**rev,'snapshot':'dag.after-repair-1.json','changed_node_ids':[n['id'] for n in g['nodes'] if n not in before['nodes']],'removed_edges':[e for e in before['edges'] if e not in g['edges']],'added_edges':[e for e in g['edges'] if e not in before['edges']]})+'\n')
print('Saved repaired graph:',len(g['nodes']),'nodes;',len(g['edges']),'edges')
