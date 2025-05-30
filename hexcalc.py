from antlr4 import *
from g4.hexcalcLexer import hexcalcLexer
from g4.hexcalcParser import hexcalcParser
from g4.hexcalcVisitor import hexcalcVisitor

# Visitor pour évaluer l'expression
class EvalVisitor(hexcalcVisitor):
    """
    Visitor personnalisé pour évaluer des expressions arithmétiques en base hexadécimale.
    Gère les variables, les fonctions intégrées et la conversion de valeurs hexadécimales avec ou sans fraction.
    """

    def __init__(self) -> None:
        """
        Initialise les attributs de l'interprète.

        Attributs :
            variable (dict): dictionnaire des variables assignées
            memory (float|int|None): résultat de la dernière expression
            decimal (bool): active la lecture en base 10
        """
        self.variables = {}
        self.memory = None
        self.decimal = False
    
    def visitProg(self, ctx: hexcalcParser.ProgContext) -> float|int:
        """
        Exécute toutes les instructions d'un programme.

        Args:
            ctx (hexcalcParser.ProgContext): contexte du parseur pour la règle 'prog'
        
        Returns:
            (int|float): Le dernier résultat calculé
        """
        result = None
        for stmt in ctx.statement():
            val = self.visit(stmt)
            if stmt.getChildCount()==1:
                result = val
                self.memory = val
        return result
    
    def visitAssign(self, ctx: hexcalcParser.AssignContext) -> float|int:
        """
        Associe une valeur à une variable.

        Args:
            ctx (hexcalcParser.AssignContext): contexte de l'assignation

        Returns:
            (float|int): la valeur assignée
        """
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value
        return value
    
    def visitExpr(self, ctx: hexcalcParser.ExprContext) -> float|int:
        """
        Redirige vers l'expression à évaluer.

        Args:
            ctx (hexcalcParser.ExprContext): contexte de l'expression

        Returns:
            (float|int): la valeur de l'expression
        """
        return self.visit(ctx.expression())
    
    def visitVariable(self, ctx: hexcalcParser.VariableContext) -> float|int:
        """
        Récupère la valeur d'une variable, ou la mémoire si le nom est '_'.

        Args:
            ctx (hexcalcParser.VariableContext): contexte de variable

        Returns:
            (float|int): la valeur stockée
        """
        var_name = ctx.ID().getText()
        if var_name == '_':
            if self.memory is None:
                raise NameError("empty memory : no previous results")
            return self.memory
        if var_name not in self.variables:
            raise NameError(f"Variable {var_name} not defined!")
        return self.variables[var_name]
    
    def visitAddSub(self, ctx: hexcalcParser.AddSubContext) -> float|int:
        """
        Effectue une addition ou soustraction entre deux expressions.

        Args:
            ctx (hexcalcParser.AddSubContext): contexte de l'expression AddSub

        Returns:
            (float|int): le résultat du calcul
        """
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.text == '+':
            return left + right
        else:
            return left - right

    def visitMulDiv(self, ctx: hexcalcParser.MulDivContext) -> float|int:
        """
        Effectue une multiplication ou division flottante entre deux expressions.

        Args:
            ctx (hexcalcParser.MulDivContext): contexte de l'expression MulDiv

        Returns:
            (float|int): le résultat du calcul
        """
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.text == '*':
            return left * right
        else:
            return left / right 

    def visitParens(self, ctx: hexcalcParser.ParensContext) -> float|int:
        """
        Evalue l'expression entre parenthèses.

        Args:
            ctx (hexcalcParser.ParensContext): context d'expression entre parenthèses

        Returns:
            (float|int): résultat de l'expression
        """
        return self.visit(ctx.expression())
    
    def visitHexFloatNumber(self, ctx: hexcalcParser.HexFloatNumberContext) -> float:
        """
        Convertit un nombre héxadécimal avec partie fractionnaire en float.

        Args:
            ctx (hexcalcParser.HexFloatNumberContext): contexte du nombre hexadécimal flottant

        Returns:
            (float): float représentant le nombre
        """
        text = ctx.HEXFLOAT().getText()
        parts = text.split('.')
        if len(parts) != 2:
            raise ValueError(f"Invalid hex float: {text}")
        integer_part, frac_part = parts
        
        int_value = int(integer_part, 16)
        frac_value = sum(int(char, 16) * (16 ** -(i + 1)) for i, char in enumerate(frac_part))
        
        return int_value + frac_value

    def visitHexNumber(self, ctx: hexcalcParser.HexNumberContext) -> int:
        """
        Convertit un nombre hexadécimal entier.
        Peut être interprété comme décimal si self.decimal est True.

        Args:
            ctx (hexcalcParser.HexNumberContext): contexte du nombre hexadécimal

        Returns:
            (int): entier représentant le nombre
        """
        base = 10 if self.decimal else 16
        return int(ctx.HEX().getText(), base)
    
    def visitPower(self, ctx: hexcalcParser.PowerContext) -> float:
        """
        Calcule la puissance d'une expression (a^b).

        Args:
            ctx (hexcalcParser.PowerContext): contexte de l'expression Power
        
        Returns:
            (float): le résultat du calcul
        """
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left ** right
    
    def visitMod(self, ctx: hexcalcParser.ModContext) -> int:
        """
        Calcule le modulo de deux expressions.

        Args:
            ctx (hexcalcParser.ModContext) : contexte de l'expression Mod

        Returns:
            int: résultat de l'opération modulo
        """
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left % right
    
    def visitUnaryMinus(self, ctx: hexcalcParser.UnaryMinusContext) -> float|int:
        """
        Applique la négation unaire à une expression.

        Args:
            ctx (hexcalcParser.UnaryMinusContext): contexte de l'expression UnaryMinus
        
        Returns:
            (float|int): la valeur opposée de l'expression
        """
        value = self.visit(ctx.expression())
        return - value
    
    def visitFuncCall(self, ctx: hexcalcParser.FuncCallContext) -> float:
        """
        Gère l'appel à une fonction avec ou sans arguments.
        Fonctionne avec : max, min, exp, ln, floor, ceil, tohex, todec, lt, eq, gt

        Args:
            ctx (hexcalcParser.FuncCallContext) : contexte de FuncCall

        Retour:
            (float|int|bool): le résultat de la fonction
        """        
        func_name = ctx.functionCall().funcName.text.lower()  # on utilise ID()
        args = [self.visit(expr) for expr in ctx.functionCall().argList().expression()] if ctx.functionCall().argList() else []

        if func_name == "max":
            return max(args)
        elif func_name == "min":
            return min(args)
        elif func_name == "exp":
            return self._exp(args[0])
        elif func_name == "ln":
            if args[0] <= 0:
                raise ValueError("ln(x) : x doit être > 0")
            return self._ln(args[0])
        elif func_name == "floor":
            return self.floor_custom(args[0])
        elif func_name == "ceil":
            return self.ceil_custom(args[0])
        elif func_name == "tohex":
            self.decimal = True
            try:
                args = [self.visit(expr) for expr in ctx.functionCall().argList().expression()] if ctx.functionCall().argList() else []
                return float_to_hexfloat(args[0])
            finally:
                self.decimal = False
        elif func_name == "todec":
            return str(int(args[0]))
        
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
            raise ValueError(f"Unknown function: {func_name}")

        
    def _exp(self, x: float, terms: int = 20) -> float:
        """
        Approximation de la fonction exponentielle e^x.

        Args:
            x (float): exposant
            terms (int): nombre de termes de la série de Taylor

        Returns:
            (float): approximation de e^x
        """
        result = 1.0
        term = 1.0
        for n in range(1, terms):
            term *= x / n
            result += term
        return result

    def _ln(self, x: float, terms: int = 20) -> float:
        """
        Approximation du logarithme népérien via développement en série.

        Args:
            x (float): valeur dont on cherche le logarithme
            terms (int): nombre de termes de la série

        Returns:
            (float): approximation de ln(x)
        """
        y = (x - 1) / (x + 1)
        result = 0.0
        for n in range(terms):
            result += (y ** (2 * n + 1)) / (2 * n + 1)
        return 2 * result
    
    def floor_custom(self, x: float) -> int:
        """
        Renvoie la valeur entière inférieure (floor) personnalisée pour les négatifs.

        Args:
            x (float): valeur à arrondir

        Returns:
            (int): plus grand entier inférieur ou égal à x
        """
        i = int(x)
        if x < 0 and x != i:
            return i - 1
        return i

    def ceil_custom(self, x: float) -> int:
        """
        Renvoie la valeur entière supérieure (ceil) personnalisée pour les positifs.

        Args:
            x (float): valeur à arrondir

        Returns:
            (int): plus petit entier supérieur ou égal à x
        """
        i = int(x)
        if x > 0 and x != i:
            return i + 1
        return i
    

    
def float_to_hexfloat(x: float, precision: int = 4) -> str:
    """
    Convertit un float en chaîne hexadécimale (avec partie fractionnaire).

    Args:
        x (float): la valeur à convertir
        precision (int): nombre de chiffres hexadécimaux après la virgule

    Returns:
        (str): chaîne de caractères représentant le float en hexadécimal
    """
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
def evaluate_expression(expr: str, visitor: EvalVisitor) -> str|None:
    """
    Compile et évalue une expression en chaîne.

    Args:
        expr (str): l'expression à évaluer
        visitor (EvalVisitor): visiteur personnalisé pour l'évaluation

    Returns:
        (str|None): Résultat sous forme de chaîne hexadécimale ou affichage direct si tohex/todec
    """
    input_stream = InputStream(expr)
    lexer = hexcalcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hexcalcParser(token_stream)
    tree = parser.prog()
    
    result = visitor.visit(tree)

    expr_lower = expr.lower()
    if expr_lower.startswith("tohex") or expr_lower.startswith("todec"):
        print("Result:", result)
        return None
    if isinstance(result, (int, float)):
        return float_to_hexfloat(result)  
    return None 

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

