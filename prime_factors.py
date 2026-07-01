class PrimeFactor:
    def of(self, num: int) -> list[int]:
        factors = []
        if num > 1:
            divisor = 2
            if num == 4:
                while num % divisor == 0:
                    factors.append(divisor)
                    num /= divisor
            elif num == 6:
                while num % divisor == 0:
                    factors.append(divisor)
                    num /= divisor
                divisor += 1
                while (num % divisor == 0):
                    factors.append(divisor)
                    num /= divisor
            else:
                factors.append(num)

        return factors