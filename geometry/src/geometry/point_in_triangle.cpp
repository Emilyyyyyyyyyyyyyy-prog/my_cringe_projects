#include "point_in_triangle.h"

namespace geometry {
    bool check_point(Vector2d v1, Vector2d v2, Vector2d v3, Vector2d v) {
        float x1 = v1.getX();
        float y1 = v1.getY();
        float x2 = v2.getX();
        float y2 = v2.getY();
        float x3 = v3.getX();
        float y3 = v3.getY();
        float x = v.getX();
        float y = v.getY();
        double a = (x1 - x) * (y2 - y1) - (x2 - x1) * (y1 - y);
        double b = (x2 - x) * (y3 - y2) - (x3 - x2) * (y2 - y);
        double c = (x3 - x) * (y1 - y3) - (x1 - x3) * (y3 - y);
        return a * b >= 0 and b * c >= 0 and a * c >= 0;
    }
}

