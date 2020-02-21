from . import environment
from . import function

class Visitor():
    def __default__(self, tree, env):
        raise

    def program(self, tree, env):
        for sub_tree in tree.children:
            r = self.visit(sub_tree, env)
            if sub_tree.data == 'return_state':
                return r

    def assignment(self, tree, env):
        key = self.visit(tree.children[0], env)
        value = self.visit(tree.children[1], env)
        env.set(key, value)

    def return_state(self, tree, env):
        return self.visit(tree.children[0], env)

    def new_symbol(self, tree, env):
        return tree.children[0].value

    def parameter(self, tree, env):
        return tree.children[0].value

    def function(self, tree, env):
        key = self.visit(tree.children[0], env)
        parameters = []
        if len(tree.children) > 2:
            parameters = [self.visit(child, env) for child in tree.children[1:-1] ]
        ast = tree.children[-1]

        func = function.Function(parameters, ast)
        env.set(key, func)

    def function_call(self, tree, env):
        func = self.visit(tree.children[0], env)

        arguments = [self.visit(c, env) for c in tree.children[1:]]
        if len(arguments) != len(func.parameters()):
            raise BaseException('Number of arguments is wrong')

        local_env = environment.Environment(env)
        for (k, v) in zip(func.parameters(), arguments):
            local_env.set(k, v)

        return self.visit(func.tree(), local_env)

    def addition(self, tree, env):
        left = self.visit(tree.children[0], env)
        right = self.visit(tree.children[1], env)
        return left + right

    def substraction(self, tree, env):
        left = self.visit(tree.children[0], env)
        right = self.visit(tree.children[1], env)
        return left - right

    def multiplication(self, tree, env):
        left = self.visit(tree.children[0], env)
        right = self.visit(tree.children[1], env)
        return left * right

    def division(self, tree, env):
        left = self.visit(tree.children[0], env)
        right = self.visit(tree.children[1], env)
        return left / right

    def symbol(self, tree, env):
        key = tree.children[0].value
        return env.get(key)

    def number(self, tree, env):
        return float(tree.children[0].value)

    def visit(self, tree, env):
        f = getattr(self, tree.data, self.__default__)
        return f(tree, env)
