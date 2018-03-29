#!/usr/bin/env python3

import stack

def main():
    s = stack.Stack()
    print('Stack is empty? {}'.format(s.isEmpty()))
    print('Stack has {} items'.format(s.numItems()))
    s.push(4)
    s.push(8)
    s.push(16)
    print('Stack has {} items'.format(s.numItems()))
    print('Peeking, item is {}'.format(s.peek()))
    print('Popping stack, item is {}'.format(s.pop()))
    print('Stack has {} items'.format(s.numItems()))
    print('Popping stack, item is {}'.format(s.pop()))

if __name__ == '__main__':
    main()
