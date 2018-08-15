#include <cstdio>

int main() {
  unsigned int i;
  unsigned int counter = 0;
  for (i = 10; i >= 0; --i) {
    std::printf("%u\n", i);
    std::printf("%d\n", i);

    if (counter > 20) {
      break;
    }
    
    counter++;
  }

  return 0;
}
