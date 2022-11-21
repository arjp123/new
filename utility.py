# import argparse
# import sys
# def calc(args):
#     if args.o=='add':
#         return args.x+args.y
#     elif args.o=='mul':
# import argpar
# import sys
# def calc(args):
#     if args.o=='add':
#         return args.x+args.y
#     elif args.o=='mul':
#         return args.x*args.y
#     elif args.o=='sub':
#         return args.x-args.y
#     elif args.o=='div':
#         return args.x/args.y
#     else:
#         print("something went wrong..")




# if __name__=='__main__':
#     parser=argparse.ArgumentParser()
#     parser.add_argument('--x',type=float,default=1.0,help="1st this is a utility for calsi..")
#     parser.add_argument('--y',type=float,default=3.0,help="2nd this is a utility for calsi..")
#     parser.add_argument('--o',type=str,default="add",help="this is a utility for calsi..")
    
#     args=parser.parse_args()
#     sys.stdout.write(str(calc(args)))














# if __name__=='__main__':
#     parser=argparse.ArgumentParser()
#     parser.add_argument('--x',type=float,default=1.0,help="1st this is a utility for calsi..")
#     parser.add_argument('--y',type=float,default=3.0,help="2nd this is a utility for calsi..")
#     parser.add_argument('--o',type=str,default="add",help="this is a utility for calsi..")
    
#     args=parser.parse_args()
#     sys.stdout.write(str(calc(args)))




import argparse
import sys

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("--num1",help="num1")
    parser.add_argument("--num2",help="num2")
    parser.add_argument("--operation",help="operation")
    args=parser.parse_args()

    n1=int(args.num1)
    n2=int(args.num2)
    result=None
    if args.operation=="add":
        result= n1 + n2
    elif args.operation=='sub':
        result=n1-n2
    else:
        print("wrong...")
    print("result ",result)















