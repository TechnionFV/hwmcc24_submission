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

# Utility rule file for kissat.

# Include any custom commands dependencies for this target.
include CMakeFiles/kissat.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/kissat.dir/progress.make

CMakeFiles/kissat: CMakeFiles/kissat-complete

CMakeFiles/kissat-complete: kissat/src/kissat-stamp/kissat-install
CMakeFiles/kissat-complete: kissat/src/kissat-stamp/kissat-mkdir
CMakeFiles/kissat-complete: kissat/src/kissat-stamp/kissat-download
CMakeFiles/kissat-complete: kissat/src/kissat-stamp/kissat-update
CMakeFiles/kissat-complete: kissat/src/kissat-stamp/kissat-patch
CMakeFiles/kissat-complete: kissat/src/kissat-stamp/kissat-configure
CMakeFiles/kissat-complete: kissat/src/kissat-stamp/kissat-build
CMakeFiles/kissat-complete: kissat/src/kissat-stamp/kissat-install
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Completed 'kissat'"
	/usr/bin/cmake -E make_directory /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/CMakeFiles
	/usr/bin/cmake -E touch /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/CMakeFiles/kissat-complete
	/usr/bin/cmake -E touch /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/kissat/src/kissat-stamp/kissat-done

kissat/src/kissat-stamp/kissat-build: kissat/src/kissat-stamp/kissat-configure
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Performing build step for 'kissat'"
	cd /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/dependencies/kissat && make -j
	cd /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/dependencies/kissat && /usr/bin/cmake -E touch /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/kissat/src/kissat-stamp/kissat-build

kissat/src/kissat-stamp/kissat-configure: kissat/tmp/kissat-cfgcmd.txt
kissat/src/kissat-stamp/kissat-configure: kissat/src/kissat-stamp/kissat-patch
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Performing configure step for 'kissat'"
	cd /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/dependencies/kissat && ./configure
	cd /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/dependencies/kissat && /usr/bin/cmake -E touch /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/kissat/src/kissat-stamp/kissat-configure

kissat/src/kissat-stamp/kissat-download: kissat/src/kissat-stamp/kissat-mkdir
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "No download step for 'kissat'"
	/usr/bin/cmake -E echo_append
	/usr/bin/cmake -E touch /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/kissat/src/kissat-stamp/kissat-download

kissat/src/kissat-stamp/kissat-install: kissat/src/kissat-stamp/kissat-build
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Performing install step for 'kissat'"
	cd /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/dependencies/kissat && cp build/kissat /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/kissat && make clean
	cd /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/dependencies/kissat && /usr/bin/cmake -E touch /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/kissat/src/kissat-stamp/kissat-install

kissat/src/kissat-stamp/kissat-mkdir:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Creating directories for 'kissat'"
	/usr/bin/cmake -E make_directory /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/dependencies/kissat
	/usr/bin/cmake -E make_directory /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/dependencies/kissat
	/usr/bin/cmake -E make_directory /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/kissat
	/usr/bin/cmake -E make_directory /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/kissat/tmp
	/usr/bin/cmake -E make_directory /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/kissat/src/kissat-stamp
	/usr/bin/cmake -E make_directory /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/kissat/src
	/usr/bin/cmake -E make_directory /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/kissat/src/kissat-stamp
	/usr/bin/cmake -E touch /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/kissat/src/kissat-stamp/kissat-mkdir

kissat/src/kissat-stamp/kissat-patch: kissat/src/kissat-stamp/kissat-update
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "No patch step for 'kissat'"
	/usr/bin/cmake -E echo_append
	/usr/bin/cmake -E touch /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/kissat/src/kissat-stamp/kissat-patch

kissat/src/kissat-stamp/kissat-update: kissat/src/kissat-stamp/kissat-download
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "No update step for 'kissat'"
	/usr/bin/cmake -E echo_append
	/usr/bin/cmake -E touch /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/kissat/src/kissat-stamp/kissat-update

kissat: CMakeFiles/kissat
kissat: CMakeFiles/kissat-complete
kissat: kissat/src/kissat-stamp/kissat-build
kissat: kissat/src/kissat-stamp/kissat-configure
kissat: kissat/src/kissat-stamp/kissat-download
kissat: kissat/src/kissat-stamp/kissat-install
kissat: kissat/src/kissat-stamp/kissat-mkdir
kissat: kissat/src/kissat-stamp/kissat-patch
kissat: kissat/src/kissat-stamp/kissat-update
kissat: CMakeFiles/kissat.dir/build.make
.PHONY : kissat

# Rule to build all files generated by this target.
CMakeFiles/kissat.dir/build: kissat
.PHONY : CMakeFiles/kissat.dir/build

CMakeFiles/kissat.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/kissat.dir/cmake_clean.cmake
.PHONY : CMakeFiles/kissat.dir/clean

CMakeFiles/kissat.dir/depend:
	cd /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build /home/basel.khouri/integrating-DRUP2ITP-in-AVY/certifaiger/build/CMakeFiles/kissat.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/kissat.dir/depend

