import json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from check_design_trace import analyze
class TaskToolTests(unittest.TestCase):
 def sample(self):return json.loads((ROOT/'examples/tool-input.json').read_text(encoding='utf-8'))
 def test_intention_is_traced(self):self.assertEqual(analyze(self.sample())['unrepresented_intents'],[])
 def test_hidden_date_remains_problem(self):
  p=self.sample();p['required_info'][0]['visible']=False;self.assertEqual(analyze(p)['hidden_required_info'],['日期'])
 def test_unused_intention_is_visible(self):
  p=self.sample();p['intents'].append('热烈');self.assertEqual(analyze(p)['unrepresented_intents'],['热烈'])
 def test_unrecognized_intention_stops(self):
  p=self.sample();p['elements'][0]['intent']='unknown'
  with self.assertRaises(ValueError):analyze(p)
 def test_empty_praise_is_not_observation(self):
  p=self.sample();p['elements'][0]['observation']=' '
  with self.assertRaises(ValueError):analyze(p)

if __name__=='__main__':unittest.main()
