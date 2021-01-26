cmake_minimum_required (VERSION 3.15)

project (csp VERSION 0.0.1)

include(cmake/sources.cmake)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
include(GNUInstallDirs)

add_library (csp ${SOURCES})
target_compile_features(csp PRIVATE c_std_11)

include_directories (include)

install(TARGETS csp)

# Additional install step installing public header files retaining original structure
install(DIRECTORY "include/gs" DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
