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
include CMakeFiles/minigzip.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/minigzip.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/minigzip.dir/flags.make

CMakeFiles/minigzip.dir/minigzip.o: CMakeFiles/minigzip.dir/flags.make
CMakeFiles/minigzip.dir/minigzip.o: ../minigzip.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/gliang/work/prima/advanced/zlib/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object CMakeFiles/minigzip.dir/minigzip.o"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/minigzip.dir/minigzip.o   -c /home/gliang/work/prima/advanced/zlib/minigzip.c

CMakeFiles/minigzip.dir/minigzip.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/minigzip.dir/minigzip.i"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -E /home/gliang/work/prima/advanced/zlib/minigzip.c > CMakeFiles/minigzip.dir/minigzip.i

CMakeFiles/minigzip.dir/minigzip.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/minigzip.dir/minigzip.s"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -S /home/gliang/work/prima/advanced/zlib/minigzip.c -o CMakeFiles/minigzip.dir/minigzip.s

CMakeFiles/minigzip.dir/minigzip.o.requires:
.PHONY : CMakeFiles/minigzip.dir/minigzip.o.requires

CMakeFiles/minigzip.dir/minigzip.o.provides: CMakeFiles/minigzip.dir/minigzip.o.requires
	$(MAKE) -f CMakeFiles/minigzip.dir/build.make CMakeFiles/minigzip.dir/minigzip.o.provides.build
.PHONY : CMakeFiles/minigzip.dir/minigzip.o.provides

CMakeFiles/minigzip.dir/minigzip.o.provides.build: CMakeFiles/minigzip.dir/minigzip.o

# Object files for target minigzip
minigzip_OBJECTS = \
"CMakeFiles/minigzip.dir/minigzip.o"

# External object files for target minigzip
minigzip_EXTERNAL_OBJECTS =

minigzip: CMakeFiles/minigzip.dir/minigzip.o
minigzip: CMakeFiles/minigzip.dir/build.make
minigzip: libz.so.1.2.5
minigzip: CMakeFiles/minigzip.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking C executable minigzip"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/minigzip.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/minigzip.dir/build: minigzip
.PHONY : CMakeFiles/minigzip.dir/build

CMakeFiles/minigzip.dir/requires: CMakeFiles/minigzip.dir/minigzip.o.requires
.PHONY : CMakeFiles/minigzip.dir/requires

CMakeFiles/minigzip.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/minigzip.dir/cmake_clean.cmake
.PHONY : CMakeFiles/minigzip.dir/clean

CMakeFiles/minigzip.dir/depend:
	cd /home/gliang/work/prima/advanced/zlib/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/gliang/work/prima/advanced/zlib /home/gliang/work/prima/advanced/zlib /home/gliang/work/prima/advanced/zlib/build /home/gliang/work/prima/advanced/zlib/build /home/gliang/work/prima/advanced/zlib/build/CMakeFiles/minigzip.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/minigzip.dir/depend

