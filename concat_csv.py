import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('--path', help= 'paste path to biog.txt file')
args = parser.parse_args()


# os.chdir(args.path) 
p=os.getcwd()
print(p)

if p=='/home/user/Documents/python_jupyter/':
    print("hello")


