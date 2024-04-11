

accounts = [[1,2,3],[3,2,1]]


def find_largest_wealth(account):
  largest_wealth = 0
  rows = len(account)
  cols = len(account[0])

  for i in range(rows):
    wealth = 0
    for j in range(cols):
      wealth  += accounts[i][j]
    largest_wealth = max(largest_wealth, wealth)
  return largest_wealth

find_largest_wealth(accounts)