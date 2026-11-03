import json,copy,html,pathlib,datetime
p=pathlib.Path(__file__).parent
g=json.loads((p/'dag.json').read_text())
rsa='https://people.csail.mit.edu/rivest/Rsapaper.pdf';rfc='https://www.rfc-editor.org/rfc/rfc8017.html';hpke='https://www.rfc-editor.org/rfc/rfc9180.html';nist='https://csrc.nist.gov/glossary/term/public_key_cryptography'
data=[
('bits','How can a message be transformed mathematically?','Files are bits; groups can be interpreted as integers without hiding them.',rfc,'§4.2','Converts byte strings to integers.'),
('secrecy','What must encryption hide, and what may be public?','The procedure and encryption key may be public; the decryption capability must remain infeasible to recover.',nist,'Definition from SP 800-56B Rev. 2','Two related keys; private-key recovery from the public key computationally infeasible.'),
('hard','How can an easy calculation be hard to reverse?','Multiplication is efficient; recovering large hidden factors is believed hard. RSA inversion is not proven equivalent to factoring.',rsa,'§§V, IX.A–D','Factors enable computing a private exponent; no proof that every inversion method must factor.'),
('mod','What does taking a remainder mean?','Modulo retains the remainder after division; powers can be evaluated by repeated squaring and reduction.',rsa,'§§V, VII.A','RSA encryption is exponentiation modulo n; efficient repeated-squaring algorithm.'),
('pair','How can two related keys have different capabilities?','The public exponent and product permit forward arithmetic; the secret factors permit calculation of a matching private exponent.',rfc,'§§3.1–3.2','Public (n,e); private (n,d) satisfying the modular inverse relation.'),
('construction','How does RSA recover the message?','Encrypt with exponent 17 modulo 2773; decrypt with exponent 157. Their product is 2668+1, giving the inverse relation.',rsa,'§§VI, VIII','Example uses p=47 q=59 n=2773 d=157 e=17; 920 encrypts to 948.'),
('randomness','Why must predictable messages be randomized?','A deterministic public encryption lets an observer encrypt candidate messages and compare. OAEP encodes with fresh randomness before RSA.',rfc,'§§5,7.1.1 steps 2–3','Primitive alone provides no security; OAEP explicitly generates a random seed and encodes before RSA.'),
('hybrid','How does a practical scheme protect arbitrary files?','A public-key mechanism produces a shared secret and public encapsulation; derived symmetric keys protect the file.',hpke,'§§1,4,5.1.1,5.2','KEM encapsulation/decapsulation, key schedule and authenticated encryption.'),
('identity','How do I know whose public key I received?','A key must be authenticated through already trusted information; substitution encrypts to the attacker.',rsa,'§IV last paragraph','Public-directory substitution attack and signed directory response rooted in trusted initial key.'),
('limits','What does the construction leave unprotected?','Base HPKE lacks sender identity authentication; recipient key compromise reveals old ciphertexts; plaintext length is not hidden.',hpke,'§§9.1,9.7.4,9.7.6','Documented non-goals and compromise conditions.'),
('target','Why can strangers encrypt with a public key without decrypting messages?','Forward and reverse computations have different costs without the private information; complete randomized schemes and authentic keys preserve that distinction.',nist,'Definition from SP 800-56B Rev. 2','Public-key cryptography requires infeasible private-key derivation; synthesis incorporates the other nodes.')]
nodes=[{'id':i,'question':q,'answer':a,'status':'supported','evidence':[{'url':u,'locator':l,'claim':c}]} for i,q,a,u,l,c in data]
edge_tuples=[('bits','secrecy','The object being protected must first be understood as encoded data.'),('bits','mod','Arithmetic requires a numeric interpretation of message data.'),('secrecy','pair','The pair must realize the distinct public and secret capabilities.'),('hard','pair','Hard inversion explains why related public information need not reveal secret information.'),('mod','construction','The exponent operations only make sense after the remainder rule.'),('pair','construction','A concrete round trip requires knowing which exponent each party has.'),('construction','randomness','The deterministic example exposes the guess-and-compare weakness.'),('randomness','hybrid','The practical scheme must incorporate fresh randomness to address predictable-message comparisons.'),('pair','identity','Key possession must be distinguished from the identity of its holder.'),('hybrid','limits','Limits here are specific to the practical HPKE construction just explained.'),('limits','target','The conclusion needs the conditions under which privacy holds.'),('identity','target','Encryption to the intended person requires authentic public-key ownership.'),('hybrid','target','The full answer must cover a complete scheme rather than raw RSA.')]
edges=[{'from':a,'to':b,'why':w} for a,b,w in edge_tuples]
g['revisions'].append({'round':1,'gaps':['Meaning of remainder arithmetic absent from initial graph','Bundled practical node conflated guess resistance with hybrid construction','Key compromise and sender authentication limits absent'],'searches':['RFC 8017 RSA encryption OAEP public key private key','RFC 9180 hybrid public key encryption authentication','RSA original paper Rivest Shamir Adleman'],'evidence':[{'url':rsa,'locators':['§§IV–IX']},{'url':rfc,'locators':['§§3–5,7.1.1']},{'url':hpke,'locators':['§§1,4–5,9.1,9.7']}],'changes':['Added mod prerequisite','Split practical into randomness and hybrid','Added limits dependent on hybrid'],'nodes':copy.deepcopy(nodes[:-1]),'edges':copy.deepcopy(edges)})
g['nodes']=nodes;g['edges']=edges
g['revisions'].append({'round':2,'gaps':['Terminology source and source identity verification','Need concrete rather than merely asserted reversibility'],'searches':['NIST public key cryptography definition','Original source frontmatter and affiliations; RSA worked example §VIII'],'evidence':[{'url':nist,'locator':'Definitions'},{'url':rsa,'locator':'§VIII, PDF p.11'}],'changes':['All necessary nodes supported','Extracted original calculation line','Added independent exhaustive check and public-operation-twice calculation','Pruned no-path topics including certificates internals, algorithm catalogs, historical performance estimates'],'nodes':copy.deepcopy(nodes),'edges':copy.deepcopy(edges)})
ids=[n['id'] for n in nodes];assert len(ids)==len(set(ids));adj={i:[] for i in ids}
for e in edges:assert e['from'] in adj and e['to'] in adj;adj[e['from']].append(e['to'])
def visit(n,stack,done):
 assert n not in stack,'cycle'
 if n in done:return
 for v in adj[n]:visit(v,stack|{n},done)
 done.add(n)
done=set()
for n in ids:visit(n,set(),done)
def reaches(n):return n=='target' or any(reaches(v) for v in adj[n])
assert all(reaches(n) for n in ids)
g['verification']={'unique_ids':True,'valid_endpoints':True,'acyclic':True,'all_nodes_reach_target':True,'node_count':len(nodes),'edge_count':len(edges),'prose_check':'All answers appear in report; edges reviewed as required knowledge, not merely reading order.'}
(p/'dag.json').write_text(json.dumps(g,indent=2));(p/'dag-checks.json').write_text(json.dumps(g['verification'],indent=2))
# Render a dependency graph as SVG, with numbered explanations below in HTML.
levels={'bits':0,'hard':0,'secrecy':1,'mod':1,'pair':2,'construction':3,'randomness':4,'hybrid':5,'identity':5,'limits':6,'target':7}
by={}
for n in nodes:by.setdefault(levels[n['id']],[]).append(n)
pos={}
for lev,ns in by.items():
 for ix,n in enumerate(ns):pos[n['id']]=(40+ix*410,40+lev*110)
svg=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 900" role="img" aria-label="Prerequisite graph, arrows point to concepts that require earlier concepts"><defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0 0L9 4.5L0 9" fill="#646c77"/></marker></defs><rect width="840" height="900" fill="#f5f4f0"/>']
for e in edges:
 x,y=pos[e['from']];xx,yy=pos[e['to']]
 svg.append(f'<path d="M{x+175} {y+64} C{x+175} {y+90},{xx+175} {yy-25},{xx+175} {yy}" fill="none" stroke="#646c77" marker-end="url(#arrow)"/>')
labels={'bits':'Messages as numbers','secrecy':'Public procedure, secret capability','hard':'Easy forward; difficult reverse','mod':'Remainder arithmetic','pair':'Related keys, different capabilities','construction':'RSA round-trip calculation','randomness':'Why fresh randomness matters','hybrid':'Shared secret + file encryption','identity':'Authentic public-key ownership','limits':'Limits and compromise','target':'Why a public key can preserve privacy'}
for n in nodes:
 x,y=pos[n['id']];svg.append(f'<rect x="{x}" y="{y}" width="350" height="64" fill="white" stroke="#cbd0d3"/><text x="{x+16}" y="{y+37}" font-family="sans-serif" font-size="16" fill="#101527">{html.escape(labels[n["id"]])}</text>')
svg.append('</svg>');(p/'dag.svg').write_text(''.join(svg))
rows=''.join(f'<li><strong>{html.escape(n["question"])}</strong><p>{html.escape(n["answer"])}</p></li>' for n in nodes)
why=''.join(f'<li><strong>{e["from"]} → {e["to"]}</strong>: {html.escape(e["why"])}</li>' for e in edges)
(p/'dag.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Research dependencies</title><style>body{max-width:900px;margin:40px auto;padding:20px;font:17px/1.6 system-ui;background:#f5f4f0;color:#101527}img{width:100%}li{margin-bottom:20px}</style><h1>Research dependencies</h1><p>Arrows point from a prerequisite to the concept that requires it.</p><img src="dag.svg" alt="Dependency graph"><h2>Questions and answers</h2><ol>'+rows+'</ol><h2>Why each dependency is needed</h2><ul>'+why+'</ul></html>')
print(g['verification'])
