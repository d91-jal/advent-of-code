# Approach: go from left to right, evaluate all possible digits recursively.
# 
# E.g. given my input 347312-805915.
# 
# First digit candidates: 3-8. Loop.
#   3 => Second digit candidates: 4-9. Loop.
#       34 => Third digit candidates: 7-9. Loop.
#           347 => Fourth digit candidates: 7-9. Loop.
#               3477 => Fifth digit candidates: 7-9. Loop.
#                   34777 => Sixth digit candidates: 7-9. Add 347777, 347778, 347779 to result.
#                   34778 => Sixth digit candidates: 8-9. Add 347788, 347789 to result.
#                   34779 => Sixth digit candidates: 9. Add 347799 to result.
#               3478 => Fifth digit candidates: 8-9. Loop.
#                   34788 => Sixth digit candidates: 8-9. Add 347888, 347889 to result.
#                   34789 => Sixth digit candidates: 9. Add 347899 to result.
#               3479 => Fifth digit candidates: 9.
#                   34799 => Sixth digit candidate: 9. Add 347999 to result.
#           348 => Fourth digit candidates: 8-9. Loop.
# ....
# 

