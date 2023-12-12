#include <chrono>
#include <cmath>
#include <iostream>

class Vec2 {
public:
  double x, y;
};

class Object {
public:
  uint32_t mass;
  double velocity;
  Vec2 position;
  uint32_t width;

  Object(uint32_t m, double v, Vec2 pos, uint32_t w = 10)
      : mass(m), velocity(v), position(pos), width(w) {}
};

std::pair<double, double> elasticCollisionSolver(Object obj1, Object obj2) {
  double newv1 =
      ((double)(obj1.mass - obj2.mass) / (double)(obj1.mass + obj2.mass)) *
          obj1.velocity +
      ((double)2 * obj2.mass / (double)(obj1.mass + obj2.mass)) *
          (double)obj2.velocity;
  double newv2 =
      ((double)2 * obj1.mass / (double)(obj1.mass + obj2.mass)) *
          (double)obj1.velocity +
      ((double)(obj2.mass - obj1.mass) / (double)(obj1.mass + obj2.mass)) *
          (double)obj2.velocity;

  return std::make_pair(newv1, newv2);
}

uint32_t computation(Object &obj1, Object &obj2, uint32_t timestep) {
  uint32_t collisionCount = 0;
  Vec2 pos1 = obj1.position;
  Vec2 pos2 = obj2.position;
  double vel1 = obj1.velocity;
  double vel2 = obj2.velocity;
  uint32_t width1 = obj1.width;
  uint32_t width2 = obj2.width;
  uint32_t mass1 = obj1.mass;
  uint32_t mass2 = obj2.mass;

  for (uint32_t i = 0; i < timestep; i++) {
    if (pos1.x + width1 >= pos2.x) {
      collisionCount += 1;
      auto result = elasticCollisionSolver(Object(mass1, vel1, Vec2(pos1)),
                                           Object(mass2, vel2, Vec2(pos2)));
      vel1 = result.first;
      vel2 = result.second;
    } else if (pos1.x <= 0) {
      collisionCount += 1;
      vel1 = -vel1;
    }

    // update positions uing local variables
    pos1.x += vel1;
    pos2.x += vel2;
  }

  // update the objects
  obj1.position = pos1;
  obj2.position = pos2;
  obj1.velocity = vel1;
  obj2.velocity = vel2;

  std::cout << std::fixed;
  std::cout << collisionCount << std::endl;
  std::cout << pos1.x << std::endl;
  std::cout << pos2.x << std::endl;
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
  double pos1x = std::stof(argv[4]);
  double pos1y = std::stof(argv[5]);
  double pos2x = std::stof(argv[6]);
  double pos2y = std::stof(argv[7]);
  uint32_t width1 = std::stol(argv[8]);
  uint32_t width2 = std::stol(argv[9]);
  double vel1 = std::stof(argv[10]);
  double vel2 = std::stof(argv[11]);

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
