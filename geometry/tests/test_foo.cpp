#include <cassert>
#include "geometry/point_in_triangle.h"

int main(){
    Vector2d v1 = Vector2d(0, 0);
    Vector2d v2 = Vector2d(1, 1);
    Vector2d v3 = Vector2d(1, 0);
    Vector2d v = Vector2d(0, 0.5);
    assert(geometry::check_point(v1, v2, v3, v));
}

