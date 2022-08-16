def sfp():
  global Tangible_fixed_assets
  global Accumulated_depreciation
  global Stocks
  global Debtors
  global Cash
  global Capital
  global Revenue
  global Expenses
  global Dividends
  global Noncurrent_liabilities
  global Current_liabilities
  Fixed_assets = Tangible_fixed_assets + Accumulated_depreciation
  Current_assets = Stocks + Debtors + Cash
  Retained_earnings = Revenue + Expenses + Dividends
  fig = plt.figure(figsize=(5,8))
  labels = ['Assets','Equity and liabilities']
  plt.bar(labels,[Current_assets,Current_liabilities])
  plt.bar(labels,[Fixed_assets,Noncurrent_liabilities],bottom=[Current_assets,Current_liabilities])
  plt.bar(labels,[0,Retained_earnings],bottom=[Current_assets+Fixed_assets,Current_liabilities+Noncurrent_liabilities])
  plt.bar(labels,[0,Capital],bottom=[Current_assets+Fixed_assets,Current_liabilities+Noncurrent_liabilities+Retained_earnings])
  plt.title('Balance sheet')
  if Current_assets > 0:
    plt.text(0,Current_assets*0.5,'Current assets\n'+str(Current_assets),va='center',ha='center')
  if Fixed_assets > 0:
    plt.text(0,Fixed_assets*0.5+Current_assets,'Fixed assets\n'+str(Fixed_assets),va='center',ha='center')
  if Current_liabilities > 0:
    plt.text(1,Current_liabilities*0.5,'Current liabilities\n'+str(Current_liabilities),va='center',ha='center')
  if Noncurrent_liabilities > 0:
    plt.text(1,Noncurrent_liabilities*0.5+Current_liabilities,'Noncurrent liabilities\n'+str(Noncurrent_liabilities),va='center',ha='center')
  if Retained_earnings > 0:
    plt.text(1,Retained_earnings*0.5+Noncurrent_liabilities+Current_liabilities,'Retained earnings\n'+str(Retained_earnings),va='center',ha='center')
  if Capital > 0:
    plt.text(1,Capital*0.5+Retained_earnings+Noncurrent_liabilities+Current_liabilities,'Capital\n'+str(Capital),va='center',ha='center')
  plt.show()
  
