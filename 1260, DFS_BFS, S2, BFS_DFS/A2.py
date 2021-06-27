#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.

def solution(price, cost):
    price_maxx = 0
    sales_maxx = 0
    for pric in price:
        sales = sum([pric-y if x >= pric > y else 0 for x, y in zip(price, cost)])

        if sales_maxx < sales:
            sales_maxx = sales
            price_maxx = pric

    return price_maxx
price = [13,17,14,30,19,17,55,16]
cost  = [12,1,5,10,3,2,40,19]
print(solution(price = price, cost = cost))