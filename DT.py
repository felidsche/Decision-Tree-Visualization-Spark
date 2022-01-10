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
    tree_to_json = """GBTClassificationModel: uid = gbtc_ceb4315c6291, numTrees=20, numClasses=2, numFeatures=21
    If (feature 12 <= 1.5)
     If (feature 1 <= 50077.0)
      If (feature 2 <= 9.5)
       If (feature 10 <= 88097.0)
        If (feature 1 <= 771.5)
         If (feature 9 <= 103969.0)
          If (feature 5 <= 22.5)
           Predict: -1.0
          Else (feature 5 > 22.5)
           Predict: -0.9850746268656716
         Else (feature 9 > 103969.0)
          If (feature 2 <= 2.0)
           Predict: -0.7910447761194029
          Else (feature 2 > 2.0)
           Predict: -1.0
        Else (feature 1 > 771.5)
         If (feature 1 <= 1110.0)
          Predict: -0.9879032258064516
         Else (feature 1 > 1110.0)
          If (feature 7 <= 1357.0)
           If (feature 7 <= 12.5)
            Predict: -0.99609375
           Else (feature 7 > 12.5)
            Predict: -1.0
          Else (feature 7 > 1357.0)
           Predict: -0.9951807228915662
       Else (feature 10 > 88097.0)
        If (feature 7 <= 7.5)
         If (feature 1 <= 1890.0)
          If (feature 2 <= 2.0)
           If (feature 16 <= 0.14033439289828956)
            If (feature 13 <= 18.5)
             If (feature 1 <= 1.5)
              Predict: -0.9937629937629938
             Else (feature 1 > 1.5)
              Predict: -0.9996079200156832
            Else (feature 13 > 18.5)
             If (feature 6 <= 502944.5)
              Predict: -1.0
             Else (feature 6 > 502944.5)
              Predict: -0.9997349589186324
           Else (feature 16 > 0.14033439289828956)
            If (feature 15 <= 0.10946435352513936)
             If (feature 0 <= 1.5)
              Predict: -0.9536231884057971
             Else (feature 0 > 1.5)
              Predict: -0.9950418345212272
            Else (feature 15 > 0.10946435352513936)
             Predict: -1.0
          Else (feature 2 > 2.0)
           If (feature 3 <= 20.0)
            Predict: -1.0
           Else (feature 3 > 20.0)
            Predict: -0.9512195121951219
         Else (feature 1 > 1890.0)
          If (feature 13 <= 63.5)
           Predict: -0.7820823244552058
          Else (feature 13 > 63.5)
           Predict: -1.0
        Else (feature 7 > 7.5)
         If (feature 2 <= 2.0)
          If (feature 15 <= 0.10446435352513936)
           If (feature 16 <= 0.01)
            If (feature 15 <= 0.035)
             Predict: -1.0
            Else (feature 15 > 0.035)
             Predict: -0.9900744416873449
           Else (feature 16 > 0.01)
            If (feature 16 <= 0.425)
             If (feature 6 <= 3.5)
              Predict: -0.9996219996219996
             Else (feature 6 > 3.5)
              Predict: -1.0
            Else (feature 16 > 0.425)
             Predict: -0.9969088098918083
          Else (feature 15 > 0.10446435352513936)
           If (feature 7 <= 17.5)
            If (feature 1 <= 1596.5)
             If (feature 15 <= 0.10946435352513936)
              Predict: -0.9931506849315068
             Else (feature 15 > 0.10946435352513936)
              Predict: -1.0
            Else (feature 1 > 1596.5)
             Predict: -0.9489194499017681
           Else (feature 7 > 17.5)
            If (feature 13 <= 63.5)
             If (feature 13 <= 62.333916561475164)
              Predict: -0.9998965873836608
             Else (feature 13 > 62.333916561475164)
              Predict: -0.9975838115372999
            Else (feature 13 > 63.5)
             If (feature 10 <= 162156.5)
              Predict: -0.9999224475551591
             Else (feature 10 > 162156.5)
              Predict: -1.0
         Else (feature 2 > 2.0)
          If (feature 15 <= 0.10446435352513936)
           Predict: -1.0
          Else (feature 15 > 0.10446435352513936)
           If (feature 4 <= 0.305)
            Predict: -0.88470066518847
           Else (feature 4 > 0.305)
            If (feature 2 <= 4.5)
             Predict: -0.9761904761904762
            Else (feature 2 > 4.5)
             If (feature 7 <= 49.5)
              Predict: -0.9902676399026764
             Else (feature 7 > 49.5)
              Predict: -1.0
      Else (feature 2 > 9.5)
       If (feature 7 <= 10.5)
        Predict: 0.09292035398230089
       Else (feature 7 > 10.5)
        If (feature 1 <= 31.5)
         If (feature 16 <= 0.065)
          Predict: -1.0
         Else (feature 16 > 0.065)
          Predict: -0.9640449438202248
        Else (feature 1 > 31.5)
         Predict: -1.0
     Else (feature 1 > 50077.0)
      If (feature 7 <= 45.5)
       If (feature 10 <= 338583.5)
        If (feature 5 <= 2.5)
         Predict: 1.0
        Else (feature 5 > 2.5)
         Predict: 0.99609375
       Else (feature 10 > 338583.5)
        Predict: 0.004739336492890996
      Else (feature 7 > 45.5)
       Predict: -1.0
    Else (feature 12 > 1.5)
     If (feature 13 <= 63.5)
      If (feature 11 <= 1.5)
       If (feature 6 <= 104619.5)
        If (feature 10 <= 189924.0)
         Predict: 1.0
        Else (feature 10 > 189924.0)
         Predict: 0.9907834101382489
       Else (feature 6 > 104619.5)
        If (feature 7 <= 213.5)
         Predict: 1.0
        Else (feature 7 > 213.5)
         Predict: 0.9731543624161074
      Else (feature 11 > 1.5)
       If (feature 12 <= 3.5)
        Predict: -0.029449423815621
       Else (feature 12 > 3.5)
        If (feature 10 <= 189924.0)
         Predict: 0.6689342403628118
        Else (feature 10 > 189924.0)
         Predict: 1.0
     Else (feature 13 > 63.5)
      Predict: -1.0
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
    def tree_json(tree: str, model: str):
        data = []
        for line in tree.splitlines():
            if line.strip():
                line = line.strip()
                data.append(line)
            else:
                break
            if not line: break
        res = []
        res.append({'name': model, 'children': parse(data[1:])})
        # add feature names
        # the 19 feature names as short strings (taken from GBT*.scala)
        features = {0: "task_id", 1: "inst_num", 2: "task_type", 3: "plan_cpu", 4: "plan_mem",
                    5: "sched_intv", 6: "job_exec", 7: "task_dur", 8: "inst_task_type",
                    9: "inst_start", 10: "inst_end", 11: "seq_no", 12: "total_seq_no", 13: "cpu_avg",
                    14: "cpu_max", 15: "mem_avg", 16: "mem_max", 17: "cpu_cols_vec", 18: "mr"}
        # drop prefix "feature " from keys

        with open('data/GBT_high_weight_tree_alibaba2018_structure.json', 'w') as outfile:
            json.dump(res[0], outfile)
        print('Conversion Success !')


    tree_json(tree_to_json, model="GBTNestedCVOuter1perc")
