#!/usr/bin/env python3

class StringBuilder:
    """ An object that builds strings without needlessly creating 
    new string objects 
    """

    def __init__(self):
        self.internal_list = []

    def length(self):
        return len(self.internal_list)

    def append(self, s):
        self.internal_list.append(s)
        return s

    def toString(self):
        return ''.join(self.internal_list)


def test_strbuilder():
    print("Testing StringBuilder ...")
    strBuild = StringBuilder()
    strBuild.append("The ") 
    strBuild.append("Lord ")
    strBuild.append("is ")
    strBuild.append("my ")
    strBuild.append("shepherd.")
    print(strBuild.toString())
    
if __name__ == '__main__':
    test_strbuilder()    
