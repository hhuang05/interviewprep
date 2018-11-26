#ifndef TERM_H
#define TERM_H

#include <map>
#include <string>
#include <vector>

#define Abs(x)    ((x) < 0 ? -(x) : (x))
#define Max(a, b) ((a) > (b) ? (a) : (b))

typedef std::map<std::string, std::string> VariableMap;

/* Term: Abstract base class of all concrete terms
 * 
 */
class Term
{

public:
  static bool IsIsomorphic(Term *a, Term *b,
                           VariableMap *varMap=nullptr);

  // Prints each specific term to stdout
  virtual void dump(std::string prefix="") = 0;
};

#endif
