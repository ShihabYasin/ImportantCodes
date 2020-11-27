import argparse,os,sys,textwrap
parser = argparse.ArgumentParser(
      prog='sudo python3 git_commit_single_file.py',
      formatter_class=argparse.RawDescriptionHelpFormatter,
      epilog=textwrap.dedent('''\
         Add & commit a single file to the associated Github repo. 
         '''))
parser.add_argument('-f','--file', help='file name to add & commit to github')
args = parser.parse_args()


if not len(sys.argv) > 1:
    parser.print_help()
    exit (0)

print("git commit "+args.file)


os.system("git add "+args.file)
os.system("git status")
os.system("git commit "+args.file)
os.system("git push origin master")