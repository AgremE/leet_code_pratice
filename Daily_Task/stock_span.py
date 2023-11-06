import collections

### Using stack to pop the element with the score, keep pop ulti you hit higher number
### otherwise, you will almost always return 1
class StockSpanner:
    def __init__(self):
        self.price_sofar = collections.deque()

    def next(self, price: int) -> int:
        ### Determin the score first
        final_score = 0
        while self.price_sofar:
            elem = self.price_sofar.pop()
            price_pop = elem[0]
            score_pop = elem[1]
            if price > price_pop:
                final_score = final_score + score_pop
            else:
                self.price_sofar.append([price_pop, score_pop])
                break
        final_score = final_score + 1
        self.price_sofar.append([price, final_score])
        return final_score


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

stockSpanner = StockSpanner()
print(stockSpanner.next(32))
print(stockSpanner.next(82))
print(stockSpanner.next(73))
print(stockSpanner.next(99))
print(stockSpanner.next(91))
