
# Options
if(GLAD_GENERATOR STREQUAL "d")
	list(APPEND GLAD_SOURCES
		"${GLAD_OUT_DIR}/glad/gl/all.d"
		"${GLAD_OUT_DIR}/glad/gl/enums.d"
		"${GLAD_OUT_DIR}/glad/gl/ext.d"
		"${GLAD_OUT_DIR}/glad/gl/funcs.d"
		"${GLAD_OUT_DIR}/glad/gl/gl.d"
		"${GLAD_OUT_DIR}/glad/gl/loader.d"
		"${GLAD_OUT_DIR}/glad/gl/types.d"
	)
elseif(GLAD_GENERATOR STREQUAL "volt")
	list(APPEND GLAD_SOURCES
		"${GLAD_OUT_DIR}/amp/gl/enums.volt"
		"${GLAD_OUT_DIR}/amp/gl/ext.volt"
		"${GLAD_OUT_DIR}/amp/gl/funcs.volt"
		"${GLAD_OUT_DIR}/amp/gl/gl.volt"
		"${GLAD_OUT_DIR}/amp/gl/loader.volt"
		"${GLAD_OUT_DIR}/amp/gl/package.volt"
		"${GLAD_OUT_DIR}/amp/gl/types.volt"
	)
else()
	set(GLAD_INCLUDE_DIRS "${GLAD_OUT_DIR}/include")
	set(GLAD_LINKER_LANGUAGE CXX)
	list(APPEND GLAD_SOURCES
		"${GLAD_OUT_DIR}/src/glad.c"
		"${GLAD_INCLUDE_DIRS}/glad/glad.h"
	)
endif()

if(GLAD_NO_LOADER)
	 set(GLAD_NO_LOADER_ARG "--no-loader")
endif()

add_custom_command(
	OUTPUT ${GLAD_SOURCES}
	COMMAND ${PYTHON_EXECUTABLE} -m glad
		--profile=${GLAD_PROFILE}
		--out-path=${GLAD_OUT_DIR}
		--api=${GLAD_API}
		--generator=${GLAD_GENERATOR}
		--extensions=${GLAD_EXTENSIONS}
		--spec=${GLAD_SPEC}
		${GLAD_NO_LOADER_ARG}
	WORKING_DIRECTORY ${GLAD_DIR}
	COMMENT "Generating Aurora GL Loader"
)
add_custom_target(glad-generate-files DEPENDS ${GLAD_SOURCES})
set_source_files_properties(${GLAD_SOURCES} PROPERTIES GENERATED TRUE)
add_library(glad ${GLAD_SOURCES})
add_dependencies(glad glad-generate-files)
target_include_directories(glad PUBLIC ${GLAD_INCLUDE_DIRS})

if(GLAD_LINKER_LANGUAGE)
	set_target_properties(glad PROPERTIES LINKER_LANGUAGE ${GLAD_LINKER_LANGUAGE})
endif()

# Export
if(GLAD_EXPORT)
	set(GLAD_LIBRARIES glad PARENT_SCOPE)
	set(GLAD_INCLUDE_DIRS ${GLAD_INCLUDE_DIRS} PARENT_SCOPE)
endif()

# Install
if(GLAD_INSTALL)
	if(GLAD_INCLUDE_DIRS)
		install(DIRECTORY ${GLAD_INCLUDE_DIRS} DESTINATION ${CMAKE_INSTALL_PREFIX})
	endif()
	install(TARGETS glad EXPORT glad-targets
					ARCHIVE DESTINATION lib)
endif()
