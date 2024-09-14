#include "Vector2d.h"

Vector2d::Vector2d() {
    this->x = 0;
    this->y = 0;
}

Vector2d::Vector2d(float x, float y) {
    this->x = x;
    this->y = y;
}

float Vector2d::getX() {
    return this->x;
}

float Vector2d::getY() {
    return this->y;
}

void Vector2d::setX(float x) {
    this->x = x;
}

void Vector2d::setY(float y) {
    this->y = y;
}

Vector2d Vector2d::operator-(Vector2d v) {
    return {this->x - v.getX(), this->y - v.getY()};
}

Vector2d Vector2d::operator*(float c) {
    return {this->x * c, this->y * c};
}

Vector2d Vector2d::operator+(Vector2d v) {
    return {this->x + v.getX(), this->y + v.getY()};
}

Vector2d Vector2d::operator+=(Vector2d v) {
    this->x += v.getX();
    this->y += v.getY();
    return *this;
}

Vector2d Vector2d::operator-=(Vector2d v) {
    this->x -= v.getX();
    this->y -= v.getY();
    return *this;
}

Vector2d Vector2d::operator*=(float c) {
    this->x *= c;
    this->y *= c;
    return *this;
}

Vector2d Vector2d::operator/=(float c) {
    this->x /= c;
    this->y /= c;
    return *this;
}
