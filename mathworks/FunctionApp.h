#ifndef FUNC_APP_H
#define FUNC_APP_H

#include "Term.h"
#include "Variable.h"
#include "ConstantExprs.h"
#include <string>
#include <vector>

class FunctionApp : public Term
{
  Term *_op;
  std::vector<Term *> *_operands;
  
 public:
  FunctionApp(Term *op, std::vector<Term*> *operands);
  ~FunctionApp();
  std::vector<Term *> *getOperands() {return _operands;};
  Term *getOp() {return _op;};
  void dump(std::string prefix="");
};

#endif
