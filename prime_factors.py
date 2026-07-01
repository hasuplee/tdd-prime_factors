class PrimeFactor:
    def of(self, num: int) -> list[int]:
        factors = []
        if num > 1:
            if num == 4:
                while num % 2 == 0:
                    factors.append(2)
                    num /= 2
            elif num == 6:
                while num % 2 == 0:
                    factors.append(2)
                    num /= 2
                while num % 3 == 0:
                    factors.append(3)
                    num /= 3
                # factors.append(3)
            else:
                factors.append(num)

        return factors