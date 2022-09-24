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
  labels = ['Assets','Equity and Liabilities']
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
    plt.text(0,Fixed_assets*0.5+Stocks+Debtors+Cash,'Fixed Assets\n'+str(Fixed_assets),va='center',ha='center')
  if Current_liabilities > 0:
    plt.text(1,Current_liabilities*0.5,'Current Liabilities\n'+str(Current_liabilities),va='center',ha='center')
  if Noncurrent_liabilities > 0:
    plt.text(1,Noncurrent_liabilities*0.5+Current_liabilities,'Noncurrent Liabilities\n'+str(Noncurrent_liabilities),va='center',ha='center')
  if Retained_earnings > 0:
    plt.text(1,Retained_earnings*0.5+Noncurrent_liabilities+Current_liabilities,'Retained Earnings\n'+str(Retained_earnings),va='center',ha='center')
  if Capital > 0:
    plt.text(1,Capital*0.5+Retained_earnings+Noncurrent_liabilities+Current_liabilities,'Capital\n'+str(Capital),va='center',ha='center')
  plt.show()
  
def Income(Revenue,Expenses,COGS,Other_operating_expenses,Financial_expenses,Taxation,Gross_profit,EBIT,EBT,Net_income):
  fig = plt.figure(figsize=(10,10))
  labels = ['Revenue','Expenses','Classified expenses']
  plt.subplot(2,1,1)
  plt.bar(labels,[Revenue,-Expenses,-Taxation],color=['green','darkorchid','thistle'])
  plt.bar(labels,[0,0,-Financial_expenses],bottom=[Revenue,-Expenses,-Taxation],color=['green','darkorchid','plum'])
  plt.bar(labels,[0,0,-Other_operating_expenses],bottom=[Revenue,-Expenses,-Taxation-Financial_expenses],color=['green','darkorchid','violet'])
  plt.bar(labels,[0,0,-COGS],bottom=[Revenue,-Expenses,-Taxation-Financial_expenses-Other_operating_expenses],color=['green','darkorchid','purple'])
  plt.hlines(0,-1,3,colors='red',linestyle='--')
  seaborn.despine(left=True, bottom=True, right=True)
  plt.title('Income statement')
  if Revenue > 0:
    plt.text(0,Revenue*0.5,'Revenue\n'+str(Revenue),va='center',ha='center')
  if Expenses > 0:
    plt.text(1,Expenses*0.5,'Expenses\n'+str(Expenses),va='center',ha='center')
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
  if Gross_profit > 0:
    plt.text(0,Gross_profit*0.5,'Gross Profit\n'+str(Gross_profit),va='center',ha='center')
  if EBIT > 0:
    plt.text(1,EBIT*0.5,'EBIT\n'+str(EBIT),va='center',ha='center')
  if EBT > 0:
    plt.text(2,EBT*0.5,'EBT\n'+str(EBT),va='center',ha='center')
  if Net_income > 0:
    plt.text(3,Net_income*0.5,'Net Income\n'+str(Net_income),va='center',ha='center')
  seaborn.despine(left=True, bottom=True, right=True)
