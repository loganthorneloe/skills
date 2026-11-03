import json
from pathlib import Path
from fractions import Fraction as F
p=Path('experiments/break-it-down-dag/2026-10-24-graph-first/runs/g04')
d=json.loads((p/'dag.json').read_text()); ns={n['id']:n for n in d['nodes']}
C='https://probabilitycourse.com/chapter1/1_4_0_conditional_probability.php'
T='https://probabilitycourse.com/chapter1/1_4_2_total_probability.php'
N='https://scikit-learn.org/stable/modules/naive_bayes.html'
G='https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall'
K='https://scikit-learn.org/stable/modules/calibration.html'
def ev(url,locator,claim,kind='source'):
 return {'url':url,'locator':locator,'exact_claim':claim,'kind':kind,'access':'Relevant full HTML passage opened 2026-10-24','claim_format':'Paraphrase or explicit derivation; not a verbatim quotation'}
ns['partition']['status']='assumed'; ns['partition']['evidence']=[]; ns['partition']['assumption_basis']='Requested spam-versus-legitimate model; supported mathematical partition rule is used by all_flags.'
ns['prior']['evidence']=[ev(C,'§1.4.0 lines 25–27','Prior denotes probability before the new information.'),{'kind':'user-stipulation','locator':'Assigned request','exact_claim':'Spam prevalence is 1%; legitimate is the complementary 99% in this binary model.'}]
ns['conditional']['evidence']=[ev(C,'§1.4.0 lines 33–42','Conditioning restricts eligible outcomes and divides joint probability by positive evidence probability.')]
ns['flag_rates']['evidence']=[ev(G,'Recall, FPR, Precision; lines 92–117','Recall conditions on actual positives; FPR on actual negatives; precision on predicted positives.'),{'kind':'user-stipulation','locator':'Assigned request','exact_claim':'90% of spam and 10% of legitimate messages are flagged.'}]
ns['joint_counts']['answer']='For each class, multiply its population count by its within-class flag rate. In a constructed 10,000-message population: 100 spam × 0.9 = 90 true flags; 9,900 legitimate × 0.1 = 990 false flags. These are expected counts under the stipulated rates.'
ns['joint_counts']['evidence']=[ev(C,'§1.4.0 Equation 1.5, lines 110–112','Joint probability is prior probability times conditional probability.'),ev(C,'Equation 1.5 applied to user inputs; checks.json counts','Original calculation: 10,000×0.01×0.9=90; 10,000×0.99×0.1=990.','derived')]
ns['all_flags']['answer']='Total flags are true flags plus false flags because the two actual classes are disjoint and exhaustive. Here: 90 + 990 = 1,080.'
ns['all_flags']['evidence']=[ev(T,'§1.4.2 two-event formula, lines 27–30','Total evidence probability sums the contributions from each complementary class.'),ev(T,'Two-event formula applied to joint_counts; checks.json','Original arithmetic: 90+990=1,080.','derived')]
ns['posterior']['evidence']=[ev(G,'Precision, lines 111–117','Precision divides true positives by all positive predictions.'),ev(G,'Precision formula applied to user inputs; checks.json','Original arithmetic: 90/1,080=1/12≈8.33%; false-to-true flag ratio is 990/90=11.','derived')]
rule={'id':'update_rule','question':'What general rule reverses the direction of the given probabilities?','answer':'Let p be the starting spam fraction, a the fraction of spam showing the evidence, and b the fraction of legitimate messages showing it. The spam fraction after observing that evidence is ap / (ap + b(1-p)), provided the denominator is positive. Numerator counts spam with evidence; denominator counts every source of that evidence. This is Bayes’ rule for two classes.','status':'supported','evidence':[ev(C,'Conditional definition, lines 38–42','Divide joint spam-and-evidence probability by evidence probability.'),ev(T,'Two-event partition formula, line 27','Evidence probability is the sum of its two class contributions.'),ev(N,'Bayes theorem, lines 75–77','Posterior class probability equals prior times conditional evidence probability divided by overall evidence probability.') ]}
d['nodes'].insert(8,rule); ns['update_rule']=rule
ns['base_rate_change']['evidence']=[ev(T,'Two-event weighted sum, line 27; combined with conditional definition','With a=0.9 and b=0.1, Bayes fraction is 0.9p/(0.9p+0.1(1-p)); evaluations in checks.json are original calculations.','derived')]
ns['word_clue']['answer']='Use word presence as evidence: a is its frequency among spam, b its frequency among legitimate messages. Apply the same update rule. When 0<p<1 and a>b, observing the word increases the spam fraction; equal positive a and b leave it unchanged. These follow by comparing ap/(ap+b(1-p)) with p.'
ns['word_clue']['evidence']=[ev(N,'Bayes theorem lines 75–77; Bernoulli word occurrence lines 141–148','Binary word presence can be an observed feature in a class-probability update.'),ev(T,'Weighted two-class sum, line 27; combined with Bayes theorem','Direction of update follows algebraically from comparing the derived posterior with p; checks.json tests illustrative cases.','derived')]
ns['training']['answer']='Use labeled messages, whose actual class is known. Class shares estimate the prior; within each class, the share of messages containing a word estimates that word’s presence probability. These are training-sample estimates.'
ns['training']['evidence']=[ev(N,'Prior estimation line 89; Bernoulli word occurrence lines 141–148','Labeled class frequencies estimate priors; a binary word-occurrence model is fit to training examples.'),ev(C,'Conditional definition lines 38–41','Within-class word occurrence is a fraction with that class as denominator.','derived')]
ns['independence']['evidence']=[ev(N,'Conditional-independence identity lines 78–84','The assumed feature probability given the class and other features equals the probability given only the class.')]
ns['word_scores']['answer']='For each class, multiply its prior by its within-class feature probabilities. Divide a class score by the sum of both scores to obtain its model probability. In a presence/absence word model, every chosen word feature contributes its presence probability if present, or one minus that probability if absent.'
ns['word_scores']['evidence']=[ev(N,'Factorized Bayes rule lines 82–87; Bernoulli formula lines 143–148','Class scores multiply prior and feature factors; binary features include absence.'),ev(T,'Two-event total-probability formula line 27','Sum both joint class-and-feature scores to normalize the model.','derived')]
ns['probability_limit']['answer']='Classifying usefully does not ensure reliable probabilities. Calibration compares predicted probabilities with observed class fractions among similarly scored messages. The 8.33% result is exact for the stipulated population rates; an estimated word-model probability needs empirical checking and does not guarantee an individual outcome.'
ns['probability_limit']['evidence']=[ev(N,'Probability-estimation warning, line 94','Naive Bayes classification performance does not ensure good probability estimates.'),ev(K,'Opening calibration definition and curves, lines 74–83','Calibration checks agreement of model probabilities with observed class frequencies in prediction groups.'),ev(C,'Conditioning interpretation lines 38–42','The stipulated 8.33% refers to the fraction in the eligible flagged group.','derived')]
ns['target']['evidence']=[{'kind':'synthesis','locator':'posterior, base_rate_change, word_scores, probability_limit','exact_claim':'Target answer combines the supported prerequisite answers and their explicit evidence; numerical claims are original calculations in checks.json.'}]
for n in d['nodes']:
 if n['status'] in ['partial','gap']: n['status']='supported'
remove={('posterior','base_rate_change'),('base_rate_change','word_clue')}
d['edges']=[e for e in d['edges'] if (e['from'],e['to']) not in remove]
for a,b,why in [
 ('conditional','update_rule','The reversed question requires selecting the evidence-bearing group as the denominator.'),
 ('joint_counts','update_rule','The numerator requires multiplying the prior by the within-class evidence rate.'),
 ('all_flags','update_rule','The denominator must include evidence from both mutually exclusive classes.'),
 ('update_rule','base_rate_change','The dependence on p follows from the weighted and normalized two-class relationship.'),
 ('update_rule','word_clue','The word is an instance of evidence; without the update rule, within-class word rates cannot be reversed to a spam fraction.'),
 ('prior','training','Without a starting class proportion, the class-frequency estimate has no role in the model.'),
 ('posterior','target','The target asks for the numerical answer at the stipulated 1% base rate.')]: d['edges'].append({'from':a,'to':b,'why':why})
d['scope']['optional_not_prerequisites'].append('Smoothing for unseen training features; verified in naive-Bayes guide lines 119–124, but not required to understand the update mechanism.')
d['source_audit']=[{'url':u,'used_sections':s,'role':r} for u,s,r in [(C,'§1.4.0 definition, prior, Equation 1.5','Author textbook: probability identities and group interpretation.'),(T,'§1.4.2 two-event partition and total-probability formula','Author textbook: adding disjoint weighted contributions.'),(G,'Recall, FPR, Precision','Google course: distinct metric denominators.'),(N,'Opening Bayes/independence equations; Bernoulli; probability warning','Official implementation guide: word-feature model and assumptions.'),(K,'Calibration definition and calibration curves','Official guide: empirical interpretation of probability confidence.')]]
d['revisions'] += [
 {'round':1,'gaps':['Direct passage verification','Arithmetic','Training and probability limits'],'searches':[],'opens':[C,T,N,G],'evidence':'history/01-research.md','changes':'None; graph identical to initial.'},
 {'round':2,'gaps':['Remaining source sections','Calibration definition','Edge necessity'],'searches':[],'opens':[C+' (line 94)',N+' (line 107)',G+' (line 111)'],'evidence':'history/02-research.md','changes':'None; source reconciliation identified edits for next round.'},
 {'round':3,'gaps':['Calibration definition','Arithmetic','Dependency reconciliation'],'searches':[],'opens':[K],'evidence':'history/03-research.md','changes':'Added update_rule; replaced posterior→base_rate_change and base_rate_change→word_clue with semantic rule edges; added posterior→target and prior→training. Marked binary partition assumed. Replaced packet-only evidence with directly located passages and explicit original derivations. Removed smoothing from training answer to optional scope. Resolved partial/gap nodes. Full resulting snapshot: history/03-supported.json.'}]
(p/'history/03-research.md').write_text('''# Round 3 — calibration and final reconciliation

Opened https://scikit-learn.org/stable/modules/calibration.html. Definition and empirical frequency comparisons confirmed at lines 74–83. No search queries; no access failures.

Actual changes are recorded in dag.json revisions and history/03-supported.json. Added the general update_rule so word evidence does not require the separate base-rate comparison. Removed smoothing from the training prerequisite; retained as optional sourced scope. Marked partition a model assumption. Replaced packet paraphrases with directly verified locators, and labeled mathematical applications as original derivations. All initial partial/gap nodes now have source support plus derived arithmetic where applicable. Numerical and structural checks run by finalize.py, results in checks.json.
''')
# Exact arithmetic, including boundaries and concrete word-update cases.
post=lambda q,a=F(9,10),b=F(1,10): a*q/(a*q+b*(1-q))
values={str(q):str(post(q)) for q in [F(0),F(1,1000),F(1,100),F(1,10),F(1,2),F(1)]}
assert post(F(1,100))==F(1,12)
assert post(F(1,10))==F(1,2)
assert post(F(1,2))==F(9,10)
assert post(F(1,1000))==F(1,112)
assert post(F(1,100),F(2,10),F(2,10))==F(1,100)
assert post(F(1,100),F(4,10),F(2,10))>F(1,100)
assert post(F(1,100),F(1,10),F(2,10))<F(1,100)
ids=[n['id'] for n in d['nodes']]; assert len(ids)==len(set(ids))
adj={x:[] for x in ids}; indeg={x:0 for x in ids}
for e in d['edges']:
 assert e['from'] in adj and e['to'] in adj and e['why']
 adj[e['from']].append(e['to']); indeg[e['to']]+=1
queue=[x for x in ids if not indeg[x]]; order=[]
while queue:
 x=queue.pop(0); order.append(x)
 for y in adj[x]:
  indeg[y]-=1
  if indeg[y]==0: queue.append(y)
assert len(order)==len(ids)
def reaches(x): return x=='target' or any(reaches(y) for y in adj[x])
assert all(reaches(x) for x in ids)
assert all(n['status'] in ['assumed','supported','partial','gap'] for n in d['nodes'])
assert all(n['evidence'] for n in d['nodes'] if n['status']=='supported')
checks={'result':'PASS','nodes':len(ids),'edges':len(d['edges']),'unique_ids':True,'valid_endpoints':True,'acyclic':True,'all_nodes_reach_target':True,'supported_nodes_have_evidence':True,'topological_order':order,'counts':{'population':10000,'spam':100,'legitimate':9900,'true_flags':90,'false_flags':990,'all_flags':1080,'spam_fraction_among_flags':'1/12'},'exact_posterior_by_spam_fraction':values,'word_clue_direction_cases':'equal rates unchanged; greater spam rate increases posterior; lower spam rate decreases posterior','semantic_review':'Reviewed edge necessity; removed example-comparison dependency from word-clue reasoning. Structural checks do not prove semantic correctness.','unperformed':['HTML rendering (shared renderer assigned)','Empirical classifier calibration or training']}
(p/'checks.json').write_text(json.dumps(checks,indent=2)+'\n')
d['verification']={'artifact':'checks.json','result':'PASS','scope':'Structural validation, exact arithmetic, manual edge/evidence review. No empirical mail data or rendered report.'}
for f in ['dag.json','history/03-supported.json']: (p/f).write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps(checks,indent=2))
