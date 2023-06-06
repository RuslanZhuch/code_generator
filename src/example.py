from code_generation.core import code_generator
from code_generation.cpp import cpp_generator
from code_generation.cpp import cpp_variable

# Create a new code file
cpp = code_generator.CodeFile('example.cpp')
cpp('int i = 0;')

# Create a new variable 'x'
x_variable = cpp_variable.CppVariable(
    name='x',
    type='int const&',
    is_static=True,
    is_constexpr=True,
    initialization_value='42')
x_variable.render_to_string(cpp)

# Create a new variable 'name'
name_variable = cpp_variable.CppVariable(
    name='name',
    type='char*',
    is_extern=True)
name_variable.render_to_string(cpp)


# Generated C++ code
"""
int i = 0;
static constexpr int const& x = 42;
extern char* name;
"""
