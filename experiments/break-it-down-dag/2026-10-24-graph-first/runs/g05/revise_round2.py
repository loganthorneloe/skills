import json,copy
from pathlib import Path
p=Path(__file__).parent;g=json.loads((p/'dag.json').read_text());before=copy.deepcopy(g)
n={x['id']:x for x in g['nodes']}
a='https://www.anthropic.com/research/demystifying-evals-for-ai-agents'
s='https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm'
def ev(url,loc,claim,basis='Directly read primary source; paraphrase, not quotation'):
 return dict(url=url,locator=loc,exact_claim=claim,basis=basis)
n['summary']['answer']='For binary judgments, the pass rate is passing cases divided by tested cases. It describes this set of judgments under this rule.'
n['summary']['status']='supported';n['summary']['evidence'].append(ev(s,'Binomial confidence interval example, lines 20–21','Observed proportion equals event count divided by sample count.','Elementary proportion calculation applied to passes; NIST uses defects.'))
n['compare']['answer']='Rerun the same cases and graders after a change, then compare results. Reset mutable test state between attempts. Hold other settings fixed where possible to make the intended change interpretable.'
n['compare']['status']='supported';n['compare']['evidence'].append(ev(a,'Step 4: stable environment, lines 305–307','Shared state can distort comparisons.'))
n['compare']['synthesis_note']='Holding non-target settings fixed is an experimental-design inference from repeated comparable runs and stable environments, not a guarantee of causal identification.'
n['limits']['answer']='An eval score supports conclusions about the measured behavior and tested situations. Coverage, grading validity, and variation limit extrapolation to production.'
n['limits']['status']='supported'
n['limits']['evidence']+= [ev(a,'How to think about non-determinism, lines 271–277','Success varies across attempts.')]
n['target']['status']='supported';n['target']['evidence']+=n['choice']['evidence']+n['calibration']['evidence']+n['improve']['evidence']
n['target']['evidence']+=n['limits']['evidence']
n['target']['answer']='Use evals to turn explicit success criteria and recorded cases into repeatable evidence. For support, define one task, collect cases with needed context and expected behavior, select and human-check graders, run a baseline, inspect failures, and compare revisions. Add real failures to the suite. Interpret results within their coverage and measurement limits.'
new=[dict(id='arithmetic',question='What does a fraction of cases mean?',answer='A count divided by the total gives the fraction of cases with that property.',status='assumed',evidence=[]),dict(id='uncertainty',question='Why might an observed score difference be inconclusive?',answer='Outcomes vary across attempts. Repeat trials; smaller effects can require larger evaluations. The graph does not establish a significance test for a particular comparison.',status='supported',evidence=[ev(a,'Structure, lines 61–62; Step 0, lines 288–289','Repeated trials address variability; smaller effects need more evidence.')]),dict(id='coverage',question='Which real-world situations does a dataset represent?',answer='Coverage depends on how cases were selected. Include expected usage and difficult cases; an unrepresentative collection can give misleading evidence about production behavior.',status='supported',evidence=n['dataset']['evidence']+[n['limits']['evidence'][0]])]
g['nodes']+=new
# Separate arithmetic summary, coverage, and repeated-attempt uncertainty because their prerequisites differ.
remove={('variation','limits'),('dataset','limits'),('reference','grader'),('objective','target')}
g['edges']=[x for x in g['edges'] if (x['from'],x['to']) not in remove]
def link(x,y,why):g['edges'].append(dict(**{'from':x,'to':y,'why':why}))
link('objective','grader','A grading rule needs a definition of success; a reference answer is optional for rules such as format checks.')
link('arithmetic','summary','A pass rate requires understanding a fraction of observed cases.')
link('dataset','coverage','Representation concerns which cases the collection includes.')
link('variation','uncertainty','Without output variation, differing results across identical attempts have no explained source.')
link('run','uncertainty','Repeated attempts require an identified execution of cases and grading.')
link('summary','uncertainty','A reported score difference requires understanding the scores being compared.')
link('uncertainty','limits','Sampling and repeated-attempt limits explain why observed differences may not settle a decision.')
link('coverage','limits','Extrapolating to production requires knowing which production situations were represented.')
g['reader_assumptions'].append('Understands elementary counts, division, and percentages; no statistical inference assumed.')
g['scope']['optional_examples']=[dict(name='Constructed refund-policy case',input='Customer requests a refund after 40 days; supplied policy allows ordinary refunds within 30 days.',expected_behavior='Explain the policy accurately; do not invent approval. Any exceptions or escalation must follow the supplied service policy.',purpose='Illustrates recording context and desired behavior; not measured data or a universal refund rule.'),dict(name='Published support-ticket classification',source='https://developers.openai.com/api/docs/guides/evals',purpose='Exact-label matching example only; not a complete evaluation of an open-ended support assistant.')]
g['scope']['limits']=['No company policy, real logs, or actual assistant outputs supplied; startup workflow is a supported synthesis, not an executed application eval.','No universal passing score, sufficient sample size, or deployment guarantee established.','Formal paired-comparison inference and test-set overfitting controls are outside this starter graph.','Legacy platform material supports concepts only; no current SDK implementation is prescribed.']
g['scope']['exhibit_decisions']=[dict(source=a,locator='Structure of an evaluation; nondeterminism diagrams',decision='No extraction: graph-only request; original exhibits can be considered for a later report.'),dict(source=s,locator='Confidence interval formulas and example',decision='No extraction: formal interval calculation is outside this prerequisite graph.')]
r=dict(round=2,kind='supplemental_research_and_reconciliation',gaps_before=before['revisions'][-1]['gaps_remaining'],searches=['site.anthropic.com engineering evals trials non deterministic evaluations agents pass rate','site.nist.gov proportion confidence interval sample size binomial'],opened=[a,s],read_sections=['Anthropic: structure; conversational agents; nondeterminism; zero-to-one roadmap; monitoring','NIST: complete confidence-interval page, especially observed proportion definition'],findings=['Repeated attempts and sufficient cases matter when effects are small.','State isolation avoids comparison contamination.','Observed fraction has an explicit mathematical definition.'],changes=[dict(id=x['id'],before=next((z for z in before['nodes'] if z['id']==x['id']),None),after=x) for x in g['nodes'] if x!=next((z for z in before['nodes'] if z['id']==x['id']),None)],edges_before=before['edges'],edges_after=g['edges'],scope_before=before['scope'],scope_after=g['scope'],assumptions_after=g['reader_assumptions'],edge_audit=['Removed reference -> grader: a specific reference answer is not necessary for every grader; objective -> grader is the actual prerequisite.','Removed objective -> target as transitively present through grader/choice.','Split fraction arithmetic, coverage, and repeated-attempt uncertainty into distinct questions.'],remaining_gaps=g['scope']['limits'],stop_reason='Core starter concepts supported; formal inference and service-specific criteria explicitly scoped out, no further rounds needed.')
g['revisions'].append({k:v for k,v in r.items() if k not in ['changes','edges_before','edges_after','scope_before','scope_after','assumptions_after']})
(p/'dag.json').write_text(json.dumps(g,indent=2)+'\n');(p/'history/round-02.json').write_text(json.dumps(r,indent=2)+'\n');(p/'history/after-round-02.json').write_text(json.dumps(g,indent=2)+'\n')
print('Saved round 2: 20 nodes; final reconciliation ready for checks.')
