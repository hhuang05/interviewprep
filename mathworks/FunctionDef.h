#ifndef FUNC_DEF_H
#define FUNC_DEF_H

#include "Term.h"
#include "Variable.h"
#include "ConstantExprs.h"
#include <string> 
#include <vector>

class FunctionDef : public Term
{
  std::vector<Variable*> *_vars;
  Term *_term;
  
 public:
  FunctionDef(std::vector<Variable*> *vars, Term *term);
  ~FunctionDef();

  std::vector<Variable*> *getVariables() {return _vars;};
  Term *getTerm() {return _term;};
  void dump(std::string prefix="");
};

#endif
