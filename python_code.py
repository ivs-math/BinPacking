import pandas as pd
df_products=pd.read_csv('products.csv')
df_order_prod=pd.read_csv('order_products.csv')
df_orders=pd.read_csv('orders.csv')
df_store_prod=pd.read_csv('store_products.csv')

Total_orders=df_orders['order_id'].values.tolist()

for oid in Total_orders:
  print('-----------NEW ORDER-------------')
  print('Order ID:',oid)
  df_list=df_order_prod[df_order_prod['order_id']==oid]
  df_list=df_list.reset_index(drop=True)
  Storage=[]
  for x in df_list['store_product_id']:
    z=df_store_prod.loc[df_store_prod['store_product_id'] == x]
    l=z['storage'].values.tolist()
    Storage.append(l[0])

  df_list.insert(1,"Storage",Storage)

  #Classify the Category
  Prod_id=[]

  for x in df_list['store_product_id']:
    z=df_store_prod.loc[df_store_prod['store_product_id'] == x]

    l=z['product_id'].values.tolist()
    Prod_id.append(l[0])

  df_list.insert(1,"product_id",Prod_id)

  Mix=[]
  for x in df_list['product_id']:
    z=df_products.loc[df_products['product_id'] == x]
    l=z['can_mix'].values.tolist()
    Mix.append(l[0])

  df_list.insert(1,"can_mix",Mix)
  volume=[]
  weight=[]
  for x in df_list['product_id']:
    z=df_products.loc[df_products['product_id'] == x]
    len=z['length'].values.tolist()
    wid=z['width'].values.tolist()
    hei=z['height'].values.tolist()
    wei=z['weight'].values.tolist()
    vol=len[0]*wid[0]*hei[0]
    volume.append(vol)
    weight.append(wei[0])

  df_list.insert(1,"volume",volume)
  df_list.insert(1,"weight",weight)
  st=df_list['Storage'].values.tolist()
  mx=df_list['can_mix'].values.tolist()
  key=df_list['store_product_id'].values.tolist()
  qnt=df_list['quantity'].values.tolist()
  vol=df_list['volume'].values.tolist()
  DF={}
  DT={}
  DP={}
  RF={}
  RT={}
  RP={}

  for x, y,k,q,v in zip(st, mx, key, qnt, vol):
    lst=[]
    if (x,y)==('Seco','Food'):
      for x in range(0,q):
        lst.append(v)
      DF[k]=lst
      DF['clase']='DF'
    if (x,y)==('Seco','Toilet'):
      for x in range(0,q):
        lst.append(v)
      DT[k]=lst
      DT['clase']='DT'
    if (x,y)==('Seco','Pets'):
      for x in range(0,q):
        lst.append(v)
      DP[k]=lst
      DP['clase']='DP'
    if ((x,y)==('Congelado','Food')) or ((x,y)==('Refrigerado','Food')):
      for x in range(0,q):
        lst.append(v)
      RF[k]=lst
      RF['clase']='RF'   
    if ((x,y)==('Congelado','Toilet')) or ((x,y)==('Refrigerado','Toilet')):
      for x in range(0,q):
        lst.append(v)
      RT[k]=lst
      RT['clase']='RT'
    if ((x,y)==('Congelado','Pets')) or ((x,y)==('Refrigerado','Pets')):
      for x in range(0,q):
        lst.append(v)
      RP[k]=lst
      RP['clase']='DT'  
  #Let's bin
  import binpacking
  order=[DF,DT,DP,RF,RP,RT]
  A=[]
  for d in order:
    for values in d.values():
      if type(values)==list:
        A=A+values
    
    


    if A and (d==DT or d==DF or d==DP):
      
      print('Clase:', d['clase'])
      print('Objects',A)
      bins=binpacking.to_constant_volume(A,12000)
      print('Bins:',bins)
      print('#Baskets--->',bins.__len__())
    if A and (d==RT or d==RP or d==RF):
      print('Clase',d['clase'])
      print('Objects',A)
      bins=binpacking.to_constant_volume(A,15318)
      print('Bins:',bins)
      print('#Cold Bags--->',bins.__len__())   
    
    A=[]