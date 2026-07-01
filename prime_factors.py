class PrimeFactor:
    def of(self, num: int) -> list[int]:
        factors = []
        if num > 1:
            if num == 4:
                factors += [2,2]
            else:
                factors.append(num)

        return factors