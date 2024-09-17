add_library(${PROJECT_NAME} STATIC geometry/point_in_triangle.cpp geometry/Vector2d.cpp geometry/Vector2d.h)

target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
