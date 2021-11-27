import random
def main():
    with open("quotes.txt",'r') as f:
        lines=f.readlines()
        rdm_no=random.randint(0,len(lines)-1)
        print(lines[rdm_no])
if __name__=="__main__":
    main()
