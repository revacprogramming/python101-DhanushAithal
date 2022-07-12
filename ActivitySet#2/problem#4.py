

def get_cs():
    """get string input"""
    string=str(input("Enter the string :"))
    return string


def str_to_lst(cs):
    """convert connected string to list of strings"""
    l=[]
    spt=cs.split(';')
    for word in spt:
        word=word.split('=')
        t=tuple(word)
        l.append(t)
    return l


def lst_to_str(lot):
    """convert list of strings to connected string"""
    str=""
    l=[]
    for wrd in lot:
        l.append(wrd)
        
    for i in l:
            str+=i[0]+'='+i[1]+';'
            
    return str

print(f"present Dictionary/-_name__=={__name__}")
def main():
    name=get_cs()
    list=str_to_lst(name)
    string=lst_to_str(list)
    print(list)
    print(string)
    #system=s;database=d;username=u;passwd=psystem=s;database=d;username=u;passwd=pprint(string)

if __name__ == '__main__':
    main()