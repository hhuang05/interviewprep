#ifndef VARIABLE_H
#define VARIABLE_H

#include "Term.h"
#include <string>

class Variable : public Term
{
  std::string _name;
 public:
  Variable(std::string name);
  ~Variable();

  std::vector<Term *> *getOperands() {return nullptr;};
  void dump();

  std::string getName() {return _name;};
};

#endif
