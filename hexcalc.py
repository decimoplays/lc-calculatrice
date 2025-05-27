from antlr4 import *
from g4.hexcalcLexer import hexcalcLexer
from g4.hexcalcParser import hexcalcParser
from g4.hexcalcVisitor import hexcalcVisitor

# Visitor pour évaluer l'expression
class EvalVisitor(hexcalcVisitor):
    def visitAddSub(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.text == '+':
            return left + right
        else:
            return left - right

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.text == '*':
            return left * right
        else:
            return left // right  # division entière

    def visitParens(self, ctx):
        return self.visit(ctx.expression())

    def visitHexNumber(self, ctx):
        return int(ctx.HEX().getText(), 16)  # parse hex string into int

# Fonction principale
def evaluate_expression(expr: str):
    input_stream = InputStream(expr)
    lexer = hexcalcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hexcalcParser(token_stream)
    tree = parser.expression()

    visitor = EvalVisitor()
    result = visitor.visit(tree)
    return hex(result).upper()[2:]  # retourne le résultat en base 16 (ex: '1F')

# Exemple d’utilisation
if __name__ == "__main__":
    expr = input("Enter hex expression: ").upper()
    result = evaluate_expression(expr)
    print("Result (hex):", result)
