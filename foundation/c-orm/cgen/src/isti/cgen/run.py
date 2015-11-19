
from os.path import splitext, sep
from sys import argv

from isti.cgen.generate import generate_h, generate_c, generate_sql, \
    generate_h_preamble, generate_h_postamble, generate_c_preamble
from isti.cgen.parse import header_to_ast, ast_to_structs


def run(files, prefix='corm'):
    for infile in files:
        root = splitext(infile)[0]
        outfile = root + '.%s.' % prefix
        ast = header_to_ast(infile)
        structs = ast_to_structs(ast)
        with open(outfile + 'h', 'w') as out:
            generate_h_preamble(out, original=infile, root=root.replace(sep, '_'))
            for struct in structs:
                generate_h(struct, out, prefix=prefix)
            generate_h_postamble(out)
        with open(outfile + 'c', 'w') as out:
            generate_c_preamble(out, header=outfile+'h')
            for struct in structs:
                generate_c(struct, out, prefix=prefix)
        with open(outfile + 'sql', 'w') as out:
            for struct in structs:
                generate_sql(struct, out)


if __name__ == '__main__':
    run(argv[1:])