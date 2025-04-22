import argparse
parser=argparse.ArgumentParser(description="Testing Parameters")
#parser.add_argument("-p1",dest="param1",help="this is a param 1")#takes it as string
parser.add_argument("-p1",dest="param1",help="this is a param 1",type=int)#takes it as string
parser.add_argument("-p2",dest="param2",help="this is a param 2",type=int)
params=parser.parse_args()
print("parameter 1 is ",params.param1)
print("parameter 2 is ",params.param2)
print("the sum is ", params.param1+params.param2)

