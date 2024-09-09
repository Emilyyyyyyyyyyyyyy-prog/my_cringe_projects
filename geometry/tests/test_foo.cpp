#include <cassert>

#include "geometry/point_in_triangle.h"

int main(){
    assert(geometry::check_point(0, 0, 1, 1, 1, 0, 0, 0.5));
}

