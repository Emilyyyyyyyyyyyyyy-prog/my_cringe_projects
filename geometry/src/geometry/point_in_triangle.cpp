#include "point_in_triangle.h"

namespace geometry {
    bool check_point(float x1, float y1, float x2, float y2, float x3, float y3, float x, float y) {
        double a = (x1 - x) * (y2 - y1) - (x2 - x1) * (y1 - y);
        double b = (x2 - x) * (y3 - y2) - (x3 - x2) * (y2 - y);
        double c = (x3 - x) * (y1 - y3) - (x1 - x3) * (y3 - y);
        return a * b >= 0 and b * c >= 0 and a * c >= 0;
    }
}

