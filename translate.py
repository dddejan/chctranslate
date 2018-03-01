import z3
import argparse

def parse_with_z3(file):
    t = z3.With(z3.Tactic("horn-simplify"), "xform.inline_eager", False)
    assertions = z3.parse_smt2_file(file)
    g = z3.Goal()
    g.add(assertions)
    r = t(g)
    s = z3.Solver()
    s.add(r[0])
    print(s.sexpr())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Translate horn problems from SMT2 to other formats.')
    parser.add_argument('--output-format', dest='output_format', metavar='FORMAT', help='Output format: mcmt')
    parser.add_argument('file', nargs='+', help='Files to process')
    args = parser.parse_args()

    for file in args.file:
        parse_with_z3(file)