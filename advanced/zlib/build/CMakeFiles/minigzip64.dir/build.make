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
include CMakeFiles/minigzip64.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/minigzip64.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/minigzip64.dir/flags.make

CMakeFiles/minigzip64.dir/minigzip.o: CMakeFiles/minigzip64.dir/flags.make
CMakeFiles/minigzip64.dir/minigzip.o: ../minigzip.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/gliang/work/prima/advanced/zlib/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object CMakeFiles/minigzip64.dir/minigzip.o"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -D_FILE_OFFSET_BITS=64 -o CMakeFiles/minigzip64.dir/minigzip.o   -c /home/gliang/work/prima/advanced/zlib/minigzip.c

CMakeFiles/minigzip64.dir/minigzip.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/minigzip64.dir/minigzip.i"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -D_FILE_OFFSET_BITS=64 -E /home/gliang/work/prima/advanced/zlib/minigzip.c > CMakeFiles/minigzip64.dir/minigzip.i

CMakeFiles/minigzip64.dir/minigzip.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/minigzip64.dir/minigzip.s"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -D_FILE_OFFSET_BITS=64 -S /home/gliang/work/prima/advanced/zlib/minigzip.c -o CMakeFiles/minigzip64.dir/minigzip.s

CMakeFiles/minigzip64.dir/minigzip.o.requires:
.PHONY : CMakeFiles/minigzip64.dir/minigzip.o.requires

CMakeFiles/minigzip64.dir/minigzip.o.provides: CMakeFiles/minigzip64.dir/minigzip.o.requires
	$(MAKE) -f CMakeFiles/minigzip64.dir/build.make CMakeFiles/minigzip64.dir/minigzip.o.provides.build
.PHONY : CMakeFiles/minigzip64.dir/minigzip.o.provides

CMakeFiles/minigzip64.dir/minigzip.o.provides.build: CMakeFiles/minigzip64.dir/minigzip.o

# Object files for target minigzip64
minigzip64_OBJECTS = \
"CMakeFiles/minigzip64.dir/minigzip.o"

# External object files for target minigzip64
minigzip64_EXTERNAL_OBJECTS =

minigzip64: CMakeFiles/minigzip64.dir/minigzip.o
minigzip64: CMakeFiles/minigzip64.dir/build.make
minigzip64: libz.so.1.2.5
minigzip64: CMakeFiles/minigzip64.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking C executable minigzip64"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/minigzip64.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/minigzip64.dir/build: minigzip64
.PHONY : CMakeFiles/minigzip64.dir/build

CMakeFiles/minigzip64.dir/requires: CMakeFiles/minigzip64.dir/minigzip.o.requires
.PHONY : CMakeFiles/minigzip64.dir/requires

CMakeFiles/minigzip64.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/minigzip64.dir/cmake_clean.cmake
.PHONY : CMakeFiles/minigzip64.dir/clean

CMakeFiles/minigzip64.dir/depend:
	cd /home/gliang/work/prima/advanced/zlib/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/gliang/work/prima/advanced/zlib /home/gliang/work/prima/advanced/zlib /home/gliang/work/prima/advanced/zlib/build /home/gliang/work/prima/advanced/zlib/build /home/gliang/work/prima/advanced/zlib/build/CMakeFiles/minigzip64.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/minigzip64.dir/depend
