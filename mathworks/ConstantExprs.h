#ifndef CONSTANT_EXPR_H
#define CONSTANT_EXPR_H

#include "Term.h"
#include <string>
#include <cstdint>

/* ConstantExpr - This abstract base class defines all the constant exprs
 * which includes predeined operators and numerics 
 */
class ConstantExpr : public Term
{
};

/* Operators - Predefined operators in the IR language
 */
class Operator : public ConstantExpr
{
  std::string _op;
  
 public:
  Operator(std::string op);
  ~Operator();
  std::string getOp();
  void dump(std::string prefix="");
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
  int64_t getInt();
  void dump(std::string prefix="");
};

class Float : public Numeric
{
  double _num;
  
 public:
  Float(double num);
  ~Float();
  double getFloat();
  void dump(std::string prefix="");
};

#endif
