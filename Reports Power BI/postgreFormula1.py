#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install psycopg2


# In[7]:


import psycopg2


# In[8]:


conn = psycopg2.connect(
    host="localhost",
    database="formula1",
    user="postgres",
    port="5432",
    password="123456")


# In[13]:


cur = conn.cursor()


# In[15]:


print(cur)


# In[32]:


type(cur)


# In[70]:


drivers_query = "select * from DRIVERS"
constructors_query = "select * from constructors"
circuits_query= "select * from circuits"
driver_standings_query= "select * from driver_standings"
drivers_query="select * from drivers"
lap_times_query="select * from lap_times"
pit_stops_query="select * from pit_stops"
qualifyings_query="select * from qualifyings"
races_query="select * from races"
results_query="select * from results"
status_query="select * from status"


# In[71]:


import pandas as pd 
drivers = pd.read_sql(drivers_query, conn)
print(drivers)


# In[72]:


constructors = pd.read_sql(constructors_query, conn)
print(constructors)


# In[73]:


circuits = pd.read_sql(circuits_query, conn)
print(circuits)


# In[75]:


drivers= pd.read_sql(drivers_query, conn)
print(drivers)


# In[76]:


lap_times=pd.read_sql(lap_times_query, conn)
print(lap_times)


# In[77]:


pit_stops=pd.read_sql(pit_stops_query, conn)
print(pit_stops)


# In[78]:


status=pd.read_sql(status_query, conn)
print(status)


# In[79]:


races=pd.read_sql(races_query, conn)
print(races)


# In[81]:


results=pd.read_sql(results_query, conn)
print(results)


# In[82]:


qualifyings=pd.read_sql(qualifyings_query, conn)
print(qualifyings)


# In[83]:


driver_standings = pd.read_sql(driver_standings_query, conn)
print(driver_standings)


# In[ ]:




