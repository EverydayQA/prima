# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake28

# The command to remove a file.
RM = /usr/bin/cmake28 -E remove -f

# Escaping for special characters.
EQUALS = =

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = /usr/bin/ccmake28

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/gliang/work/prima/advanced/zlib

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/gliang/work/prima/advanced/zlib/build

# Include any dependencies generated for this target.
include xunit/CMakeFiles/check_example_xunit.dir/depend.make

# Include the progress variables for this target.
include xunit/CMakeFiles/check_example_xunit.dir/progress.make

# Include the compile flags for this target's objects.
include xunit/CMakeFiles/check_example_xunit.dir/flags.make

xunit/CMakeFiles/check_example_xunit.dir/example_check.o: xunit/CMakeFiles/check_example_xunit.dir/flags.make
xunit/CMakeFiles/check_example_xunit.dir/example_check.o: ../xunit/example_check.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/gliang/work/prima/advanced/zlib/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object xunit/CMakeFiles/check_example_xunit.dir/example_check.o"
	cd /home/gliang/work/prima/advanced/zlib/build/xunit && /usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/check_example_xunit.dir/example_check.o   -c /home/gliang/work/prima/advanced/zlib/xunit/example_check.c

xunit/CMakeFiles/check_example_xunit.dir/example_check.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/check_example_xunit.dir/example_check.i"
	cd /home/gliang/work/prima/advanced/zlib/build/xunit && /usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -E /home/gliang/work/prima/advanced/zlib/xunit/example_check.c > CMakeFiles/check_example_xunit.dir/example_check.i

xunit/CMakeFiles/check_example_xunit.dir/example_check.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/check_example_xunit.dir/example_check.s"
	cd /home/gliang/work/prima/advanced/zlib/build/xunit && /usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -S /home/gliang/work/prima/advanced/zlib/xunit/example_check.c -o CMakeFiles/check_example_xunit.dir/example_check.s

xunit/CMakeFiles/check_example_xunit.dir/example_check.o.requires:
.PHONY : xunit/CMakeFiles/check_example_xunit.dir/example_check.o.requires

xunit/CMakeFiles/check_example_xunit.dir/example_check.o.provides: xunit/CMakeFiles/check_example_xunit.dir/example_check.o.requires
	$(MAKE) -f xunit/CMakeFiles/check_example_xunit.dir/build.make xunit/CMakeFiles/check_example_xunit.dir/example_check.o.provides.build
.PHONY : xunit/CMakeFiles/check_example_xunit.dir/example_check.o.provides

xunit/CMakeFiles/check_example_xunit.dir/example_check.o.provides.build: xunit/CMakeFiles/check_example_xunit.dir/example_check.o

# Object files for target check_example_xunit
check_example_xunit_OBJECTS = \
"CMakeFiles/check_example_xunit.dir/example_check.o"

# External object files for target check_example_xunit
check_example_xunit_EXTERNAL_OBJECTS =

xunit/check_example_xunit: xunit/CMakeFiles/check_example_xunit.dir/example_check.o
xunit/check_example_xunit: xunit/CMakeFiles/check_example_xunit.dir/build.make
xunit/check_example_xunit: xunit/CMakeFiles/check_example_xunit.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking C executable check_example_xunit"
	cd /home/gliang/work/prima/advanced/zlib/build/xunit && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/check_example_xunit.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
xunit/CMakeFiles/check_example_xunit.dir/build: xunit/check_example_xunit
.PHONY : xunit/CMakeFiles/check_example_xunit.dir/build

xunit/CMakeFiles/check_example_xunit.dir/requires: xunit/CMakeFiles/check_example_xunit.dir/example_check.o.requires
.PHONY : xunit/CMakeFiles/check_example_xunit.dir/requires

xunit/CMakeFiles/check_example_xunit.dir/clean:
	cd /home/gliang/work/prima/advanced/zlib/build/xunit && $(CMAKE_COMMAND) -P CMakeFiles/check_example_xunit.dir/cmake_clean.cmake
.PHONY : xunit/CMakeFiles/check_example_xunit.dir/clean

xunit/CMakeFiles/check_example_xunit.dir/depend:
	cd /home/gliang/work/prima/advanced/zlib/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/gliang/work/prima/advanced/zlib /home/gliang/work/prima/advanced/zlib/xunit /home/gliang/work/prima/advanced/zlib/build /home/gliang/work/prima/advanced/zlib/build/xunit /home/gliang/work/prima/advanced/zlib/build/xunit/CMakeFiles/check_example_xunit.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : xunit/CMakeFiles/check_example_xunit.dir/depend
