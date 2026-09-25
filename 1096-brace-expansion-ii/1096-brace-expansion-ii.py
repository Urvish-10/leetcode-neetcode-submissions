class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def combine(a, b):
            return {x + y for x in a for y in b}

        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != "}":
                if expression[i] == ",":
                    result |= current
                    current = {""}
                    i += 1

                elif expression[i] == "{":
                    group, i = parse(i + 1)
                    current = combine(current, group)

                else:
                    current = {x + expression[i] for x in current}
                    i += 1

            result |= current
            return result, i + 1 if i < len(expression) and expression[i] == "}" else i

        return sorted(parse(0)[0])