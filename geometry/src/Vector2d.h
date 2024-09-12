#ifndef GEOMETRY_VECTOR2D_H
#define GEOMETRY_VECTOR2D_H


class Vector2d {
private:
    float x, y;
public:
    Vector2d();
    Vector2d(float, float);
    float getX();
    float getY();
    void setX(float);
    void setY(float);
};


#endif //GEOMETRY_VECTOR2D_H
