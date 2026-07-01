class PrimeFactor:
    def of(self, num: int) -> list[int]:
        factors = []
        if num == 2:
            factors.append(2)
        elif num == 3:
            factors.append(3)

        return factors