class Comb_Iterator:

    def __init__(self, num_counters, max_value = 1):
        """
        Object constructor:
        * num_counters: number of counters of the combinations
            computed by the generator function comb_generator().
        * max_value: maximum value of each counter. 
        """

        self.num_counters = num_counters
        self.max_value = max_value
        
        return

    def comb_generator(self):
        """
        Generator function. Return a list containing the next
        value of the counters.
        """
        
        Maximo = [i for i in range(self.max_value+1)]#[1, 2, 3, ...]
        iterable = {x: i for i, x in enumerate(Maximo)}#{'0': 0...}
        resultado = [Maximo[0]] * self.num_counters
        while True:
            yield resultado
            for i in range(1, self.num_counters + 1):
                if resultado[-i] == Maximo[-1]:  # el ultimo no puede seguir
                    resultado[-i] = Maximo[0]
                else:
                    resultado[-i] = Maximo[iterable[resultado[-i]] + 1]  #Se modifica el siguiente
                    break
            else:
                break

        # Y cuando no queden valores simplemente retornamos
        return
