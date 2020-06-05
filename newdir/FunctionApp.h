#ifndef FUNC_APP_H
#define FUNC_APP_H

#include "Term.h"
#include "Variable.h"
#include "ConstantExprs.h"
#include <string>
#include <vector>

/* Function Applications in the IR language
 *
 * (<term> <term>*)
 * Example: (+ a b)
 */ 
class FunctionApp : public Term
{
  Term *_op;
  std::vector<Term *> *_operands;
  
 public:
  FunctionApp(Term *op, std::vector<Term*> *operands);
  ~FunctionApp();
  
  std::vector<Term *> *getOperands();
  Term *getOp();
  void dump(std::string prefix="");
};

#endif
