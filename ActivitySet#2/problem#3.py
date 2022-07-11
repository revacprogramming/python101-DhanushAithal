def get_str():
   """get string input"""
   string=''
   string=input("Enter the string:")
   return string


def str_to_lst(cs):
    """convert connected string to list of strings"""
    split=cs.split(';')
    lst=list()
    #if '' in split:
      #split.remove('')
    for word in split:
      wrd=word.split('=')
      t=tuple(wrd)
      lst.append(t)
    return lst

def main():
   name=get_str()
   list=str_to_lst(name)
   print(list)


if __name__ == '__main__':
 main()