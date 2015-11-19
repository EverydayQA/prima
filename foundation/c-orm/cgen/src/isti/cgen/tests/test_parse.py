
from unittest import TestCase
from pycparser.c_ast import Struct

from isti.cgen.parse import header_to_ast, ast_to_structs, StructVisitor


class TestParseHeader(TestCase):

    def test_parse_isti_str(self):
        ast = header_to_ast('../../../../../clib/tests/check_isti_sqlite.h')
        ast.show()

    def test_struct_visitor(self):
        ast = header_to_ast('../../../../../clib/tests/check_isti_sqlite.h')
        data = []
        def save(name, node):
            data.append(name)
            data.append(node)
        StructVisitor(save).visit(ast)
        assert data[0] == 'foo', data[0]
        assert isinstance(data[1], Struct), data[1]

    def test_ast_to_structs(self):
        ast = header_to_ast('../../../../../clib/tests/check_isti_sqlite.h')
        structs = ast_to_structs(ast)
        assert len(structs) == 1, structs
        assert 'foo' in [struct['sname'] for struct in structs], structs
        fields = structs[0]['fields']
        assert len(fields) == 3, fields
        for field in fields:
            assert field['fname'] in ('id', 'bar', 'baz'), field
            assert field['fname'] != 'id' or field['type'] == 'int'
            assert field['fname'] != 'bar' or field['type'] == 'int'
            assert field['fname'] != 'baz' or (field['type'] == 'char' and field['pointer'])
