#!/usr/bin/env python3

def listcomps():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(c, s) for s in sizes
                      for c in colors]
    print(tshirts)

def genexps():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
        print(tshirt)
    
def main():
    listcomps()
    genexps()
    
if __name__ == '__main__':
    main()
