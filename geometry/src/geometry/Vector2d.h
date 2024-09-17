#ifndef GEOMETRY_VECTOR2D_H
#define GEOMETRY_VECTOR2D_H


class Vector2d {
private:
    float x_, y_;
public:
    Vector2d();
    Vector2d(float, float);
    float x() const;
    float y() const;
    void x(float);
    void y(float);

    Vector2d operator-(Vector2d) const;
    Vector2d operator*(float) const;
    Vector2d operator+(Vector2d) const;
    Vector2d operator+=(Vector2d);
    Vector2d operator-=(Vector2d) ;
    Vector2d operator*=(float);
    Vector2d operator/=(float);
};


#endif //GEOMETRY_VECTOR2D_H
