def min_coins(coins, T):
    W = [ None for _ in range(T+1) ]
    W[0] = 0
    for i in range(T):
        for coin in coins:
            if i+coin < T+1:
                if W[i+coin] is None:
                    W[i+coin] = W[i]+1
                else:
                    W[i+coin] = min(W[i+coin], W[i]+1)
    return W[-1]


if __name__ == "__main__":
    coins = [1,5,8]
    T = 15
    print(min_coins(coins, T))