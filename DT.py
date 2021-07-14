"""
Decision Tree Classification.
"""
from __future__ import print_function

import json

if __name__ == "__main__":
    """
    copied from msc-thesis/saft/src/model/predict_task_failure
    Model: Decision tree
    Dataset: Alibaba 2017
    """
    tree_to_json = """DecisionTreeRegressionModel: uid=DecisionTreeRegressor_03b82f73f50f, depth=5, numNodes=45, numFeatures=10
  If (plan_cpu <= 45.0)
   If (duration_task <= 0.058333333333333334)
    If (real_cpu_max <= 1.7549999952316284)
     If (real_memory_max <= 8.153650851454586E-4)
      Predict: 1.0
     Else (real_memory_max > 8.153650851454586E-4)
      If (real_cpu_avg <= 0.625)
       Predict: 0.0
      Else (real_cpu_avg > 0.625)
       Predict: 0.17647058823529413
    Else (real_cpu_max > 1.7549999952316284)
     If (real_memory_avg <= 0.0020008800784125924)
      If (duration_instance <= 0.04166666666666667)
       Predict: 1.0
      Else (duration_instance > 0.04166666666666667)
       Predict: 0.0
     Else (real_memory_avg > 0.0020008800784125924)
      Predict: 0.0
   Else (duration_task > 0.058333333333333334)
    If (number_of_instances <= 5.5)
     If (duration_instance <= 0.025)
      Predict: 1.0
     Else (duration_instance > 0.025)
      Predict: 0.0
    Else (number_of_instances > 5.5)
     Predict: 0.0
  Else (plan_cpu > 45.0)
   If (plan_memory <= 0.00891724694520235)
    If (number_of_instances <= 5.5)
     If (real_memory_max <= 0.009823208209127188)
      Predict: 0.0
     Else (real_memory_max > 0.009823208209127188)
      If (real_memory_avg <= 0.005717909662052989)
       Predict: 0.00398406374501992
      Else (real_memory_avg > 0.005717909662052989)
       Predict: 4.336513443191674E-4
    Else (number_of_instances > 5.5)
     If (real_cpu_max <= 7.085000038146973)
      If (real_memory_max <= 0.02645665593445301)
       Predict: 5.241749486308551E-6
      Else (real_memory_max > 0.02645665593445301)
       Predict: 3.336224728097685E-5
     Else (real_cpu_max > 7.085000038146973)
      If (plan_memory <= 0.0041078871581703424)
       Predict: 0.009900990099009901
      Else (plan_memory > 0.0041078871581703424)
       Predict: 9.707795359673819E-5
   Else (plan_memory > 0.00891724694520235)
    If (real_cpu_avg <= 0.014999999664723873)
     If (real_memory_avg <= 6.704113038722426E-4)
      If (number_of_instances <= 5.5)
       Predict: 0.0
      Else (number_of_instances > 5.5)
       Predict: 1.0
     Else (real_memory_avg > 6.704113038722426E-4)
      Predict: 0.0
    Else (real_cpu_avg > 0.014999999664723873)
     If (real_cpu_max <= 5.295000076293945)
      If (number_of_instances <= 34.5)
       Predict: 0.0010686044026501388
      Else (number_of_instances > 34.5)
       Predict: 2.0320483046911287E-4
     Else (real_cpu_max > 5.295000076293945)
      If (duration_task <= 1.0083333333333333)
       Predict: 2.3634376200183167E-4
      Else (duration_task > 1.0083333333333333)
       Predict: 1.2339585389930897E-5
"""


    # Parser
    def parse(lines):
        block = []
        while lines:

            if lines[0].startswith('If'):
                bl = ' '.join(lines.pop(0).split()[1:]).replace('(', '').replace(')', '')
                block.append({'name': bl, 'children': parse(lines)})

                if lines[0].startswith('Else'):
                    be = ' '.join(lines.pop(0).split()[1:]).replace('(', '').replace(')', '')
                    block.append({'name': be, 'children': parse(lines)})
            elif not lines[0].startswith(('If', 'Else')):
                block2 = lines.pop(0)
                block.append({'name': block2})
            else:
                break
        return block


    # Convert Tree to JSON
    def tree_json(tree):
        data = []
        for line in tree.splitlines():
            if line.strip():
                line = line.strip()
                data.append(line)
            else:
                break
            if not line: break
        res = []
        res.append({'name': 'Root', 'children': parse(data[1:])})
        with open('data/structure.json', 'w') as outfile:
            json.dump(res[0], outfile)
        print('Conversion Success !')


    tree_json(tree_to_json)
