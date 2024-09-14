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

    Vector2d operator-(Vector2d);
    Vector2d operator*(float);
    Vector2d operator+(Vector2d);
    Vector2d operator+=(Vector2d);
    Vector2d operator-=(Vector2d) ;
    Vector2d operator*=(float);
    Vector2d operator/=(float);
};


#endif //GEOMETRY_VECTOR2D_H
