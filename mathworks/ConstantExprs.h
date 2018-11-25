#include "Term.h"
#include <string>
#include <cstdint>

class ConstantExpr : public Term
{
 public :
  virtual bool isOperator() = 0;
  virtual bool isInteger() = 0; 
  virtual bool isFloat() = 0;
};

/* Operators
 */
class Operator : public ConstantExpr
{
  std::string _op;
  std::vector<Term*> *_operands;
  
 public:
  Operator(std::string op, std::vector<Term*> *operands);
  ~Operator();
  std::vector<Term *> *getOperands() {return _operands;};
  std::string getOp() {return _op;};
  bool isOperator() {return true;};
  bool isInteger() {return false;};
  bool isFloat() {return false;};
  void dump();
};

class Numeric : public ConstantExpr
{
};

class Integer : public Numeric
{
  int64_t _internalVal;
  
 public:
  Integer(int64_t integer);
  ~Integer();
  bool isOperator() {return false;};
  bool isInteger() {return true;};
  bool isFloat() {return false;};
  void dump();
};

class Float : public Numeric
{
  double _num;
  
 public:
  Float(double num);
  ~Float();
  bool isOperator() {return false;};
  bool isInteger() {return false;};
  bool isFloat() {return true;};
  void dump();
};
