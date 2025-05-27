from antlr4 import *
from g4.hexcalcLexer import hexcalcLexer
from g4.hexcalcParser import hexcalcParser
from g4.hexcalcVisitor import hexcalcVisitor

# Visitor pour évaluer l'expression
class EvalVisitor(hexcalcVisitor):
    def __init__(self):
        self.variables = {}
    
    def visitProg(self, ctx):
        result = None
        for stmt in ctx.statement():
            val = self.visit(stmt)
            if stmt.getChildCount()==1:
                result = val
        return result
    
    def visitAssign(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value
        return value
    
    def visitExpr(self, ctx):
        return self.visit(ctx.expression())
    
    def visitVariable(self, ctx):
        var_name = ctx.ID().getText()
        if var_name not in self.variables:
            raise NameError(f"Variable {var_name} not defined!")
        return self.variables[var_name]
    
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
    
    def visitPower(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left ** right
    
    def visitMod(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left % right
    
    def visitUnaryMinus(self, ctx):
        value = self.visit(ctx.expression())
        return - value

# Fonction principale
def evaluate_expression(expr: str, visitor: EvalVisitor):
    input_stream = InputStream(expr)
    lexer = hexcalcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hexcalcParser(token_stream)
    tree = parser.prog()
    
    result = visitor.visit(tree)
    if isinstance(result, int):
        return hex(result).upper()[2:] # retourne le résultat en base 16 (ex: '1F')
    return None # n'affiche rien


# Exemple d’utilisation
if __name__ == "__main__":
    visitor = EvalVisitor()
    print("HexCalc (type 'exit' to quit)")
    while True:
        line = input(">>> ").strip()
        if line.lower() == "exit":
            break
        try:
            result = evaluate_expression(line, visitor)
            if result is not None:
                print("Result (hex):", result)
        except Exception as e:
            print("Error:", e)

