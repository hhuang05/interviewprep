#!/usr/bin/env python3

class Calculator:
    def __init__(self):
        self.last_val = 0
        self.allow_ops = set(['+', '-', '*', '/'])

    def allow_push(self, op_onstack, op_new):
        """ Enforces operator precedence on the op stack """
        if ((op_onstack == '+' and op_new == '*') or
            (op_onstack == '+' and op_new == '/') or
            (op_onstack == '-' and op_new == '*') or
            (op_onstack == '-' and op_new == '/')):
            return True

        return False

    def eval_immediate(self, val_stack, op_stack):
        """ Evaluates and updates val and op stacks """
        if (len(val_stack) >= 2 and len(op_stack) >= 1):
            operand2 = val_stack.pop()
            operand1 = val_stack.pop()
            operator = op_stack.pop()

            if (operator == '+'):
                result = operand1 + operand2
            elif (operator == '-'):
                result = operand1 - operand2
            elif (operator == '*'):
                result = operand1 * operand2
            elif (operator == '/'):
                result = operand1 / operand2    

            val_stack.append(result)

    def is_operator(self, op):
        if (op in self.allow_ops):
            return True
        else:
            return False
        
    def evaluate(self, inputs):
        """ Evaluates the string of inputs """ 
        cur_num = ""
        val_stack = []
        op_stack = []
        
        for c in inputs:
            if (c.isdigit()):
                cur_num += c
            elif (self.is_operator(c)):
                to_num = int(cur_num)
                cur_num = ""
                val_stack.append(to_num)

                while (len(op_stack) > 0):
                    op_top = op_stack[len(op_stack)-1]            
                    if (self.allow_push(op_top, c)):
                        op_stack.append(c)
                        break
                    else:
                        self.eval_immediate(val_stack, op_stack)

                if (len(op_stack) == 0):
                    op_stack.append(c)
                    
            else:
                print("Input not valid")
                return None

        if (cur_num != ""):
            val_stack.append(int(cur_num))
            cur_num = ""
            self.eval_immediate(val_stack, op_stack)
            return val_stack.pop()
        else:
            print("Input not valid")
            return None


def main():
    newCalc = Calculator()
    s = "45-23-66/3*41+72"
    print(s)
    print('={}'.format(newCalc.evaluate(s)))
    
if __name__ == '__main__':
    main()
