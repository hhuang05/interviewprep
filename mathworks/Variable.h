#ifndef VARIABLE_H
#define VARIABLE_H

#include "Term.h"
#include <string>

/* Variable - Defines variables in the IR
 */ 
class Variable : public Term
{
  std::string _name;
  
 public:
  
  Variable(std::string name);
  ~Variable();
  
  std::string getName();
  void dump(std::string prefix="");
  
};

#endif
