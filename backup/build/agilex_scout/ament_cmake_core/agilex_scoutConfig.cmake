# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_agilex_scout_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED agilex_scout_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(agilex_scout_FOUND FALSE)
  elseif(NOT agilex_scout_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(agilex_scout_FOUND FALSE)
  endif()
  return()
endif()
set(_agilex_scout_CONFIG_INCLUDED TRUE)

# output package information
if(NOT agilex_scout_FIND_QUIETLY)
  message(STATUS "Found agilex_scout: 0.0.0 (${agilex_scout_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'agilex_scout' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${agilex_scout_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(agilex_scout_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${agilex_scout_DIR}/${_extra}")
endforeach()
