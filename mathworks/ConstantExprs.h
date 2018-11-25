#include "Term.h"
#include <string>

class ConstantExpr : public Term
{
 public :
  virtual bool isOperator() = 0;
  virtual bool isNumeric() = 0;
};

class Operator : public ConstantExpr
{
  std::string _op;
    
 public:
  Operator(std::string op);
  ~Operator();
  bool isOperator() {return true;};
};

class Numeric : public ConstantExpr
{
 public:
  virtual bool isInteger() = 0;
  virtual bool isFloat() = 0;
};

class Integer : public Numeric
{
 public:
  bool isInteger() {return true;};
};

class Float : public Numeric
{
 public:
  Float(double num);
  ~Float();
  bool isFloat() {return true;};
};
