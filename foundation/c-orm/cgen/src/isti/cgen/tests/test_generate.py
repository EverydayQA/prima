
from unittest import TestCase

from isti.cgen.parse import header_to_ast, ast_to_structs
from isti.cgen.generate import generate

class TestGenerator(TestCase):

    def test_generate(self):
        ast = header_to_ast('../../../../../clib/tests/check_isti_sqlite.h')
        structs = ast_to_structs(ast)
        for struct in structs:
            generate(struct)
        assert False
