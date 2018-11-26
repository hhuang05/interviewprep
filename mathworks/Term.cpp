#include "FunctionDef.h"
#include "FunctionApp.h"
#include "ConstantExprs.h"
#include "Variable.h"
#include "Term.h"

#include <iostream>
#include <map>
#include <utility>

#define TOLERANCE 0.0000001


double RelDif(double a, double b)
{
  double c = Abs(a);
  double d = Abs(b);

  d = Max(c, d);

  return d == 0.0 ? 0.0 : Abs(a - b) / d;
}

bool Term::IsIsomorphic(Term *a, Term *b, VariableMap *varMap)
{
  if (Variable *v1 = dynamic_cast<Variable*>(a)) {
    if (Variable *v2 = dynamic_cast<Variable*>(b)) {

      if (varMap != nullptr) {
        auto map_it = varMap->find(v1->getName());
        if (map_it == varMap->end()) {
          std::cout << "Variable not defined" << std::endl;
          return false;
        } else if ((*map_it).second.compare(v2->getName()) != 0) {
          std::cout << "Expecting variables ("<< v1->getName() << ","
                    << (*map_it).second << ")" << std::endl;
          std::cout << " but got ("<< v1->getName() << ","
                    << v2->getName() << ")" << std::endl;
          return false;
        } else {
          std::cout << "Variables match in order" << std::endl;
          return true;
        }
      } else {
        std::cout << "Both terms are variables" << std::endl;
        return true;
      }
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
      if (op1->getOp().compare(op2->getOp()) == 0) {
        std::cout << "Operators are isomorphic" << std::endl;
        return true;
      } else {
        std::cout << "Operators not the same" << std::endl;
      }
    }
    
  } else if (FunctionApp *fn1 = dynamic_cast<FunctionApp*>(a)) {
    if (FunctionApp *fn2 = dynamic_cast<FunctionApp*>(b)) {
      // We first check the operators, then check operands
      if (Term::IsIsomorphic(fn1->getOp(), fn2->getOp(), varMap)) {
        auto op1_operands = fn1->getOperands();
        auto op2_operands = fn2->getOperands();

        // if we have the same number of operands
        if (op1_operands->size() == op2_operands->size()) {
          auto operand1_it = op1_operands->begin();
          auto operand2_it = op2_operands->begin();

          while (operand1_it != op1_operands->end() &&
                 operand2_it != op2_operands->end()) {

            if (Term::IsIsomorphic(*operand1_it, *operand2_it, varMap)) {
              ++operand1_it;
              ++operand2_it;
            } else {
              std::cout << "Function applications are not isomorphic" << std::endl;
              return false;
            }
          }

          std::cout << "Function applications are isomorphic" << std::endl;
          return true;
                 
        } else {
          std::cout << "Number of operands different" << std::endl;
        }
      } 
    }
  } else if (FunctionDef *fndef1 = dynamic_cast<FunctionDef*>(a)) {
    if (FunctionDef *fndef2 = dynamic_cast<FunctionDef*>(b)) {
      if (fndef1->getVariables()->size() == fndef2->getVariables()->size()) {
        // First create a map of the variables from one funcdef to the other
        VariableMap *localMap = new VariableMap();

        auto fndef1Var_it = fndef1->getVariables()->begin();
        auto fndef2Var_it = fndef2->getVariables()->begin();

        while (fndef1Var_it != fndef1->getVariables()->end() &&
               fndef2Var_it != fndef2->getVariables()->end()) {
          
          localMap->insert(make_pair((*fndef1Var_it)->getName(),
                                   (*fndef2Var_it)->getName()));
          
          ++fndef1Var_it;
          ++fndef2Var_it;
        }

        // Now map is created, we now compare the terms but use
        // the map as a verifier for the order of the bound
        // variables in the term
        if (Term::IsIsomorphic(fndef1->getTerm(), fndef2->getTerm(), localMap)) {
          std::cout << "Function definitions isomorphic" << std::endl;
          return true;
          
        } else {
          std::cout << "Function definitions not isomorphic" << std::endl;
        }
        
      } else {
        std::cout << "Number of variables different" << std::endl;
      }
    }
  } else {
    std::cout << "Both terms are not the same" << std::endl;
  }
  
  return false;
}
