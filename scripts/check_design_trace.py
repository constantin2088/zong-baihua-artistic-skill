"""Local deterministic aid; never a factual or model behavior certificate."""
def analyze(p):
 intents=p['intents']
 if not intents or len(set(intents))!=len(intents):raise ValueError('nonempty unique intentions required')
 seen=set();mapped=set()
 for e in p['elements']:
  if e['id'] in seen:raise ValueError('duplicate element')
  seen.add(e['id'])
  if e['intent'] not in intents:raise ValueError('unmapped intention')
  if not all(isinstance(e.get(k),str) and e[k].strip() for k in ('observation','reason')):raise ValueError('specific observation and reason required')
  mapped.add(e['intent'])
 hidden=[x['id'] for x in p['required_info'] if x.get('visible') is not True]
 return {'unrepresented_intents':sorted(set(intents)-mapped),'hidden_required_info':hidden,'note':'Traceability and visibility do not certify beauty, reader understanding or accessibility.'}

if __name__=='__main__':
 import json,sys
 print(json.dumps(analyze(json.loads(open(sys.argv[1],encoding='utf-8').read())),ensure_ascii=False,indent=2))
