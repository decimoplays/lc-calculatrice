from antlr4 import *
from g4.hexcalcLexer import hexcalcLexer
from g4.hexcalcParser import hexcalcParser
from g4.hexcalcVisitor import hexcalcVisitor

# Visitor pour évaluer l'expression
class EvalVisitor(hexcalcVisitor):
    def __init__(self):
        self.variables = {}
        self.memory = None
    
    def visitProg(self, ctx):
        result = None
        for stmt in ctx.statement():
            val = self.visit(stmt)
            if stmt.getChildCount()==1:
                result = val
                self.memory = val
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
        if var_name == '_':
            if self.memory is None:
                raise NameError("empty memory : no previous results")
            return self.memory
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
            return left / right  # division entière

    def visitParens(self, ctx):
        return self.visit(ctx.expression())
    
    def visitHexFloatNumber(self, ctx):
        text = ctx.HEXFLOAT().getText()
        parts = text.split('.')
        if len(parts) != 2:
            raise ValueError(f"Invalid hex float: {text}")
        integer_part, frac_part = parts
        
        int_value = int(integer_part, 16)
        frac_value = sum(int(char, 16) * (16 ** -(i + 1)) for i, char in enumerate(frac_part))
        
        return int_value + frac_value

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
    
    def visitMinMax(self, ctx):
        func_name = ctx.ID().getText().lower()                      # récupère "max" ou “min" et le transforme en chaine de caractère.
        args = [self.visit(expr) for expr in ctx.expression()]      # permet de transformer les expressions hexadécimales en nombres entiers

        if func_name == "max":
            return max(args)
        elif func_name == "min":
            return min(args)
    
        # Fonctions de comparaison attendent exactement 2 arguments
        elif func_name in ("lt", "eq", "gt"):
            if len(args) != 2:
                raise ValueError(f"{func_name} attend exactement 2 arguments")
            a, b = args
            if func_name == "lt":
                return a < b
            elif func_name == "eq":
                return a == b
            elif func_name == "gt":
                return a > b
        else:
            raise ValueError(f"Fonction inconnue : {func_name}")
    
        
    def visitExpLn(self, ctx):
        func_name = ctx.ID().getText().lower()
        arg = self.visit(ctx.expression())

        if func_name == "exp":
            return self._exp(arg)
        elif func_name == "ln":
            if arg <= 0:
                raise ValueError("ln(x) : x doit être > 0")
            return self._ln(arg)
        elif func_name == "floor":
            return self.floor_custom(arg)
        elif func_name == "ceil":
            return self.ceil_custom(arg)
        elif func_name == "tohex":
        # Convertit l'argument en int puis en hex sans '0x'
            return format(int(arg), 'X')
        elif func_name == "todec":
            # Convertit l'argument (supposé hex string) en décimal string
            # Ici arg est un nombre, on le convertit en int puis string
            return str(int(arg))
        else:
            raise ValueError(f"Unknown Function : {func_name}")
        
    def _exp(self, x, terms=20):
        result = 1.0
        term = 1.0
        for n in range(1, terms):
            term *= x / n
            result += term
        return result

    def _ln(self, x, terms=20):
        y = (x - 1) / (x + 1)
        result = 0.0
        for n in range(terms):
            result += (y ** (2 * n + 1)) / (2 * n + 1)
        return 2 * result
    
    def floor_custom(self, x):
        i = int(x)
        if x < 0 and x != i:
            return i - 1
        return i

    def ceil_custom(self, x):
        i = int(x)
        if x > 0 and x != i:
            return i + 1
        return i
    

    
def float_to_hexfloat(x, precision=4):
    if x < 0:
        return '-' + float_to_hexfloat(-x, precision)

    int_part = int(x)
    frac_part = x - int_part

    int_hex = format(int_part, 'X')

    if frac_part == 0:
        return int_hex

    frac_hex = ''
    for _ in range(precision):
        frac_part *= 16
        digit = int(frac_part)
        frac_hex += format(digit, 'X')
        frac_part -= digit
        if frac_part == 0:
            break

    return f"{int_hex}.{frac_hex}"

# Fonction principale
def evaluate_expression(expr: str, visitor: EvalVisitor):
    input_stream = InputStream(expr)
    lexer = hexcalcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hexcalcParser(token_stream)
    tree = parser.prog()
    
    result = visitor.visit(tree)

    expr_lower = expr.lower()
    if expr_lower.startswith("tohex") or expr_lower.startswith("todec"):
        # Résultat déjà formaté en string, on l'affiche direct
        print("Result:", result)
        return None
    if isinstance(result, (int, float)):
        return float_to_hexfloat(result)  # conversion hex flottant
    return None  # pour les autres cas

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

