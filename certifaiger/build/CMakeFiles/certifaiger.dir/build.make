# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build

# Include any dependencies generated for this target.
include CMakeFiles/certifaiger.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/certifaiger.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/certifaiger.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/certifaiger.dir/flags.make

CMakeFiles/certifaiger.dir/src/certifaiger.cpp.o: CMakeFiles/certifaiger.dir/flags.make
CMakeFiles/certifaiger.dir/src/certifaiger.cpp.o: ../src/certifaiger.cpp
CMakeFiles/certifaiger.dir/src/certifaiger.cpp.o: CMakeFiles/certifaiger.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/certifaiger.dir/src/certifaiger.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/certifaiger.dir/src/certifaiger.cpp.o -MF CMakeFiles/certifaiger.dir/src/certifaiger.cpp.o.d -o CMakeFiles/certifaiger.dir/src/certifaiger.cpp.o -c /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/src/certifaiger.cpp

CMakeFiles/certifaiger.dir/src/certifaiger.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/certifaiger.dir/src/certifaiger.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/src/certifaiger.cpp > CMakeFiles/certifaiger.dir/src/certifaiger.cpp.i

CMakeFiles/certifaiger.dir/src/certifaiger.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/certifaiger.dir/src/certifaiger.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/src/certifaiger.cpp -o CMakeFiles/certifaiger.dir/src/certifaiger.cpp.s

# Object files for target certifaiger
certifaiger_OBJECTS = \
"CMakeFiles/certifaiger.dir/src/certifaiger.cpp.o"

# External object files for target certifaiger
certifaiger_EXTERNAL_OBJECTS =

certifaiger: CMakeFiles/certifaiger.dir/src/certifaiger.cpp.o
certifaiger: CMakeFiles/certifaiger.dir/build.make
certifaiger: libaiger.a
certifaiger: CMakeFiles/certifaiger.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable certifaiger"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/certifaiger.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/certifaiger.dir/build: certifaiger
.PHONY : CMakeFiles/certifaiger.dir/build

CMakeFiles/certifaiger.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/certifaiger.dir/cmake_clean.cmake
.PHONY : CMakeFiles/certifaiger.dir/clean

CMakeFiles/certifaiger.dir/depend:
	cd /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/CMakeFiles/certifaiger.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/certifaiger.dir/depend

