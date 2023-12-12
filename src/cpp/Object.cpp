#include <chrono>
#include <cmath>
#include <iostream>

class Vec2 {
public:
  float x, y;
};

class Object {
public:
  int mass;
  float velocity;
  Vec2 position;
  int width;

  Object(int m, float v, Vec2 pos, int w = 10)
      : mass(m), velocity(v), position(pos), width(w) {}
};

std::pair<float, float> elasticCollisionSolver(Object obj1, Object obj2) {
  float newv1 =
      ((obj1.mass - obj2.mass) / (obj1.mass + obj2.mass)) * obj1.velocity +
      (2 * obj2.mass / (obj1.mass + obj2.mass)) * obj2.velocity;
  float newv2 =
      (2 * obj1.mass / (obj1.mass + obj2.mass)) * obj1.velocity +
      ((obj2.mass - obj1.mass) / (obj1.mass + obj2.mass)) * obj2.velocity;

  return std::make_pair(newv1, newv2);
}

int computation(Object &obj1, Object &obj2, int timestep) {
  int collisionCount = 0;
  Vec2 pos1 = obj1.position;
  Vec2 pos2 = obj2.position;
  float vel1 = obj1.velocity;
  float vel2 = obj2.velocity;
  int width1 = obj1.width;
  int width2 = obj2.width;
  int mass1 = obj1.mass;
  int mass2 = obj2.mass;

  for (int i = 0; i < timestep; ++i) {
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

  int timestep = std::stoi(argv[1]);
  int mass1 = std::stoi(argv[2]);
  int mass2 = std::stoi(argv[3]);
  float pos1x = std::stof(argv[4]);
  float pos1y = std::stof(argv[5]);
  float pos2x = std::stof(argv[6]);
  float pos2y = std::stof(argv[7]);
  int width1 = std::stoi(argv[8]);
  int width2 = std::stoi(argv[9]);
  float vel1 = std::stof(argv[10]);
  float vel2 = std::stof(argv[11]);

  Vec2 position1 = {pos1x, pos1y};
  Object obj1(mass1, vel1, position1, width1);

  Vec2 position2 = {pos2x, pos2y};
  Object obj2(mass2, vel2, position2, width2);

  auto start = std::chrono::high_resolution_clock::now();
  int collisions = computation(obj1, obj2, timestep);
  auto end = std::chrono::high_resolution_clock::now();

  std::cout << "Total collisions: " << collisions << std::endl;
  std::chrono::duration<double> duration = end - start;
  std::cout << "Elapsed time: " << duration.count() << " seconds" << std::endl;

  return 0;
}
