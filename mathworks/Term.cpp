#include "FunctionApp.h"
#include "ConstantExprs.h"
#include "Variable.h"
#include "Term.h"
#include <iostream>

#define TOLERANCE 0.0000001

double RelDif(double a, double b)
{
  double c = Abs(a);
  double d = Abs(b);

  d = Max(c, d);

  return d == 0.0 ? 0.0 : Abs(a - b) / d;
}

bool Term::IsIsomorphic(Term *a, Term *b)
{
  if (Variable *v1 = dynamic_cast<Variable*>(a)) {
    if (Variable *v2 = dynamic_cast<Variable*>(b)) {
      std::cout << "Both terms are variables" << std::endl;
      return true;
    }
    
  } else if (Integer *i1 = dynamic_cast<Integer*>(a)) {
    if (Integer *i2 = dynamic_cast<Integer*>(b)) {
      if (i1->getInt() == i2->getInt()) {
        std::cout << "Integers constants are same" << std::endl;
        return true;
      } else {
        std::cout << "Integers are not the same" << std::endl;
      }
    }
    
  } else if (Float *f1 = dynamic_cast<Float*>(a)) {
    if (Float *f2 = dynamic_cast<Float*>(b)) {
      if (RelDif(f1->getFloat(), f2->getFloat()) <= TOLERANCE) {
        std::cout << "Floating points constants are close enough" << std::endl;
        return true;
      } else {
        std::cout << "Floating points are not close enough" << std::endl;
      }
    }
    
  } else if (Operator *op1 = dynamic_cast<Operator*>(a)) {
    if (Operator *op2 = dynamic_cast<Operator*>(b)) {
      // We first check the operators, then check operands
      if (op1->getOp().compare(op2->getOp()) == 0) {
        auto op1_operands = op1->getOperands();
        auto op2_operands = op2->getOperands();

        // if we have the same number of operands
        if (op1_operands->size() == op2_operands->size()) {
          auto operand1_it = op1_operands->begin();
          auto operand2_it = op2_operands->begin();

          while (operand1_it != op1_operands->end() &&
                 operand2_it != op2_operands->end()) {

            if (Term::IsIsomorphic(*operand1_it, *operand2_it)) {
              ++operand1_it;
              ++operand2_it;
            } else {
              return false;
            }
          }

          std::cout << "Operators are isomorphic" << std::endl;
          return true;
                 
        } else {
          std::cout << "Number of operands different" << std::endl;
        }
        
      } else {
        std::cout << "Operators not the same" << std::endl;
      }
    }
  }
  else {
    std::cout << "Both terms are not the same" << std::endl;
  }
  
  return false;
}
