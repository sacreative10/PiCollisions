#include <chrono>
#include <cmath>
#include <cstdint>
#include <iostream>

class Vec2 {
public:
  long double x, y;
};

class Object {
public:
  uint32_t mass;
  long double velocity;
  Vec2 position;
  uint32_t width;

  Object(uint32_t m, long double v, Vec2 pos, uint32_t w)
      : mass(m), velocity(v), position(pos), width(w) {}
};

std::pair<long double, long double> elasticCollisionSolver(uint32_t mass1,
                                                           long double vel1,
                                                           uint32_t mass2,
                                                           long double vel2) {

  long double double_mass1 = static_cast<long double>(mass1);
  long double double_mass2 = static_cast<long double>(mass2);

  // Elastic collision formula
  long double final_vel1 =
      ((double_mass1 - double_mass2) / (double_mass1 + double_mass2)) * vel1 +
      ((2 * double_mass2) / (double_mass1 + double_mass2)) * vel2;
  long double final_vel2 =
      ((2 * double_mass1) / (double_mass1 + double_mass2)) * vel1 +
      ((double_mass2 - double_mass1) / (double_mass1 + double_mass2)) * vel2;

  return std::make_pair(final_vel1, final_vel2);
}

uint32_t computation(Object &obj1, Object &obj2, uint32_t timestep) {
  uint32_t collisionCount = 0;
  long double pos1 = obj1.position.x;
  long double pos2 = obj2.position.x;
  long double vel1 = obj1.velocity;
  long double vel2 = obj2.velocity;
  uint32_t width1 = obj1.width;
  uint32_t width2 = obj2.width;
  uint32_t mass1 = obj1.mass;
  uint32_t mass2 = obj2.mass;

  for (uint32_t i = 0; i < timestep; i++) {
    if (pos1 + width1 >= pos2) {
      collisionCount += 1;
      std::pair<long double, long double> result =
          elasticCollisionSolver(mass1, vel1, mass2, vel2);
      vel1 = result.first;
      vel2 = result.second;
    }
    if (pos1 <= 0) {
      collisionCount += 1;
      vel1 *= -1;
    }

    // update positions uing local variables
    pos1 += vel1;
    pos2 += vel2;
  }

  // update the objects
  obj1.position.x = pos1;
  obj2.position.x = pos2;
  obj1.velocity = vel1;
  obj2.velocity = vel2;

  std::cout << std::fixed;
  std::cout << collisionCount << std::endl;
  std::cout << pos1 << std::endl;
  std::cout << pos2 << std::endl;
  // print the velocity in full precision
  std::cout << vel1 << std::endl;
  std::cout << vel2 << std::endl;

  return collisionCount;
}

int main(int argc, char *argv[]) {
  if (argc != 12) {
    std::cerr << "Usage: " << argv[0]
              << " <timestep> <mass1> <mass2> <pos1x> <pos1y> <pos2x> <pos2y> "
                 "<width1> <width2> <vel1> <vel2>"
              << std::endl;
    return 1;
  }

  uint32_t timestep = std::stol(argv[1]);
  uint32_t mass1 = std::stol(argv[2]);
  uint32_t mass2 = std::stol(argv[3]);
  long double pos1x = std::stof(argv[4]);
  long double pos1y = std::stof(argv[5]);
  long double pos2x = std::stof(argv[6]);
  long double pos2y = std::stof(argv[7]);
  uint32_t width1 = std::stol(argv[8]);
  uint32_t width2 = std::stol(argv[9]);
  long double vel1 = std::stof(argv[10]);
  long double vel2 = std::stof(argv[11]);

  // std::cout << "Timestep: " << timestep << std::endl;
  // std::cout << "Mass1: " << mass1 << std::endl;
  // std::cout << "Mass2: " << mass2 << std::endl;
  // std::cout << "Pos1x: " << pos1x << std::endl;
  // std::cout << "Pos1y: " << pos1y << std::endl;
  // std::cout << "Pos2x: " << pos2x << std::endl;
  // std::cout << "Pos2y: " << pos2y << std::endl;
  // std::cout << "Width1: " << width1 << std::endl;
  // std::cout << "Width2: " << width2 << std::endl;
  // std::cout << "Vel1: " << vel1 << std::endl;
  // std::cout << "Vel2: " << vel2 << std::endl;

  Vec2 position1 = {pos1x, pos1y};
  Object obj1(mass1, vel1, position1, width1);

  Vec2 position2 = {pos2x, pos2y};
  Object obj2(mass2, vel2, position2, width2);

  auto start = std::chrono::high_resolution_clock::now();
  uint32_t collisions = computation(obj1, obj2, timestep);
  auto end = std::chrono::high_resolution_clock::now();

  // auto computation =
  //     elasticCollisionSolver(1, -0.01012, 1000000000000, -0.000001);

  // std::cout << collisions << std::endl;
  // std::cout << obj1.position.x << std::endl;
  // std::cout << obj2.position.x << std::endl;
  // // print the velocity in full precision
  // std::cout << std::fixed;
  // std::cout << obj1.velocity << std::endl;
  // std::cout << obj2.velocity << std::endl;

  std::chrono::duration<double> duration = end - start;
  // std::cout << "Elapsed time: " << duration.count() << " seconds" <<
  // std::endl;

  return 0;
}
