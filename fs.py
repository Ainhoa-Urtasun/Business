import matplotlib.pyplot as plt
import seaborn

Fixed_assets = 0
Stocks = 0
Debtors = 0
Cash = 0
Capital = 0
Retained_earnings = 0
Noncurrent_liabilities = 0
Current_liabilities = 0

def Balance(Fixed_assets,Stocks,Debtors,Cash,Capital,Retained_earnings,Noncurrent_liabilities,Current_liabilities):
  fig = plt.figure(figsize=(5,8))
  labels = ['Assets','Equity and liabilities']
  plt.bar(labels,[Cash,Current_liabilities])
  plt.bar(labels,[Debtors,Noncurrent_liabilities],bottom=[Cash,Current_liabilities])
  plt.bar(labels,[Stocks,Retained_earnings],bottom=[Debtors+Cash,Noncurrent_liabilities+Current_liabilities])
  plt.bar(labels,[Fixed_assets,Capital],bottom=[Stocks+Debtors+Cash,Retained_earnings+Noncurrent_liabilities+Current_liabilities])
  plt.title('Balance sheet')
  if Cash > 0:
    plt.text(0,Cash*0.5,'Cash\n'+str(Cash),va='center',ha='center')
  if Debtors > 0:
    plt.text(0,Debtors*0.5+Cash,'Debtors\n'+str(Debtors),va='center',ha='center')
  if Stocks > 0:
    plt.text(0,Stocks*0.5+Debtors+Cash,'Stocks\n'+str(Stocks),va='center',ha='center')
  if Fixed_assets > 0:
    plt.text(0,Fixed_assets*0.5+Stocks+Debtors+Cash,'Fixed_assets\n'+str(Fixed_assets),va='center',ha='center')
  if Current_liabilities > 0:
    plt.text(1,Current_liabilities*0.5,'Current liabilities\n'+str(Current_liabilities),va='center',ha='center')
  if Noncurrent_liabilities > 0:
    plt.text(1,Noncurrent_liabilities*0.5+Current_liabilities,'Noncurrent liabilities\n'+str(Noncurrent_liabilities),va='center',ha='center')
  if Retained_earnings > 0:
    plt.text(1,Retained_earnings*0.5+Noncurrent_liabilities+Current_liabilities,'Retained earnings\n'+str(Retained_earnings),va='center',ha='center')
  if Capital > 0:
    plt.text(1,Capital*0.5+Retained_earnings+Noncurrent_liabilities+Current_liabilities,'Capital\n'+str(Capital),va='center',ha='center')
  plt.show()
  
def Income(Revenue,COGS,Other_operating_expenses,Financial_expenses,Taxation):
  Expenses = -(COGS + Other_operating_expenses + Financial_expenses + Taxation)
  Gross_profit = Revenue - COGS
  EBIT = Gross_profit - Other_operating_expenses
  EBT = EBIT - Financial_expenses
  Net_income = EBT - Taxation
  fig = plt.figure(figsize=(10,10))
  labels = ['Revenue','Expenses','Classified expenses']
  plt.subplot(2,1,1)
  plt.bar(labels,[Revenue,Expenses,-Taxation],color=['green','darkorchid','thistle'])
  plt.bar(labels,[0,0,-Financial_expenses],bottom=[Revenue,Expenses,-Taxation],color=['green','darkorchid','plum'])
  plt.bar(labels,[0,0,-Other_operating_expenses],bottom=[Revenue,Expenses,-Taxation-Financial_expenses],color=['green','darkorchid','violet'])
  plt.bar(labels,[0,0,-COGS],bottom=[Revenue,Expenses,-Taxation-Financial_expenses-Other_operating_expenses],color=['green','darkorchid','purple'])
  plt.hlines(0,-1,3,colors='red',linestyle='--')
  seaborn.despine(left=True, bottom=True, right=True)
  plt.title('Income statement')
  if Taxation > 0:
    plt.text(2,-Taxation*0.5,'Taxation\n'+str(Taxation),va='center',ha='center')
  if Financial_expenses > 0:
    plt.text(2,-Financial_expenses*0.5-Taxation,'Financial expenses\n'+str(Financial_expenses),va='center',ha='center')
  if Other_operating_expenses > 0:
    plt.text(2,-Other_operating_expenses*0.5-Financial_expenses-Taxation,'Other operating\nexpenses '+str(Other_operating_expenses),va='center',ha='center')
  if COGS > 0:
    plt.text(2,-COGS*0.5-Other_operating_expenses-Financial_expenses-Taxation,'COGS\n'+str(COGS),va='center',ha='center')
  plt.subplot(2,1,2)
  plt.bar(['Gross profit','EBIT','EBT','Net income'],[Gross_profit,EBIT,EBT,Net_income],color=['seashell','peachpuff','sandybrown','chocolate'])
  plt.hlines(0,-1,3,colors='red',linestyle='--')
  seaborn.despine(left=True, bottom=True, right=True)
