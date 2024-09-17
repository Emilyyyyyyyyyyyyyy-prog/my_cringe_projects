#include "Vector2d.h"

Vector2d::Vector2d() {
    x_ = 0;
    y_ = 0;
}

Vector2d::Vector2d(float x, float y) {
    x_ = x;
    y_ = y;
}

float Vector2d::x() const {
    return x_;
}

float Vector2d::y() const {
    return y_;
}

void Vector2d::x(float new_x) {
    x_ = new_x;
}

void Vector2d::y(float new_y) {
    y_ = new_y;
}

Vector2d Vector2d::operator-(Vector2d v) const {
    return {x_ - v.x(), y_ - v.y()};
}

Vector2d Vector2d::operator*(float c) const {
    return {x_ * c, y_ * c};
}

Vector2d Vector2d::operator+(Vector2d v) const {
    return {x_ + v.x(), y_ + v.y()};
}

Vector2d Vector2d::operator+=(Vector2d v) {
    x_ += v.x();
    y_ += v.y();
    return *this;
}

Vector2d Vector2d::operator-=(Vector2d v) {
    x_ -= v.x();
    y_ -= v.y();
    return *this;
}

Vector2d Vector2d::operator*=(float c) {
    x_ *= c;
    y_ *= c;
    return *this;
}

Vector2d Vector2d::operator/=(float c) {
    x_ /= c;
    y_ /= c;
    return *this;
}
