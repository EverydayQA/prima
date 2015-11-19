
# Parse the C code for a typdefed struct, constructing a summary of the
# details in a form that can be easily used by a pystache template (see
# `generate.py`).

from itertools import chain

from pycparser import parse_file
from pycparser.c_ast import NodeVisitor, Typedef, PtrDecl


TYPE_DATA = {('int', False): ('d', 'integer'),
             ('char', True): ('s', 'text')}



# Call pycparser to parse the file.
def header_to_ast(path):
    return parse_file(path, use_cpp=True)

# A helper function for accessing (grand-)child nodes in the pycparser AST.
def child(node, gen=1):
    if gen:
        return child(node.children()[0][1], gen-1)
    else:
        return node

# Construct the map of values that contain information about a field in the
# struct.
def field(sname, n, decl):
    pointer = isinstance(child(decl), PtrDecl)
    type_ = child(decl, 3 if pointer else 2).names[0]
    data = TYPE_DATA.get((type_, pointer))
    if data:
        code, sql_type = data
        yield {'fname': decl.name,
               'n': n,
               'pointer': pointer,
               'type': type_,
               'code': code,
               'sql_type': sql_type}
    else:
        print('type %s%s of %s.%s is unsupported' %
              (type_, '*' if pointer else '', sname, decl.name))

# Construct the map of values that contain information about a struct.
def struct(name, node):
    return {'sname': name,
            'fields': list(add_comma(
                chain.from_iterable(
                    field(name, n, decl)
                        for (n, (_, decl)) in enumerate(node.children()))))}

def add_comma(fields):
    prev = None
    for field in fields:
        if prev: prev['comma'] = ','
        yield field
        prev = field

# Process an AST, collecting struct information.
def ast_to_structs(ast):
    structs = []
    def callback(name, node):
        structs.append(struct(name, node))
    StructVisitor(callback).visit(ast)
    return structs


class ParseError(Exception): pass


# The visitor classes used to extract data from the AST.  These extend those
# provided by pycparser to include more information on ancestors (used to look
# back to the typedef for a given struct).

class AncestorVisitor(NodeVisitor):

    def __init__(self):
        self.current = None
        self.ancestors = []

    def visit(self, node):
        if self.current:
            self.ancestors.append(self.current)
        self.current = node
        try:
            return super(AncestorVisitor, self).visit(node)
        finally:
            if self.ancestors:
                self.ancestors.pop(-1)

class StructVisitor(AncestorVisitor):

    def __init__(self, callback):
        self.callback = callback
        super(StructVisitor, self).__init__()

    def visit_Struct(self, node):
        '''
        Call the callback with the typedef name and the node.
        '''
        if len(self.ancestors) < 2 \
                or not isinstance(self.ancestors[-2], Typedef):
            raise ParseError("struct {} is not typedefed".format(node.name))
        self.callback(self.ancestors[-2].name, node)
