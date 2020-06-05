#include <cstdint>
#include <iostream>

int swap_int32(int32_t v)
{
  const uint8_t *b = (const uint8_t *)&v;
  union {
    int32_t v;
    uint8_t b[4];
  } u;

  u.b[0] = b[3];
  u.b[1] = b[2];
  u.b[2] = b[1];
  u.b[3] = b[0];

  return u.v;

}

int main()
{
  int32_t num = 1093541423;
  std::cout << "Number : " << num << ", Swapped: " << swap_int32(num) << std::endl;
}
