print("running new code ")
import matplotlib.pyplot as plt
import pandas as pd 
df=pd.read_csv("transactions.csv")

print("Full data:")
print(df)


#print("Descriptions:")
#print(df["Description"])

def categorize(text):
    text=text.lower()
    if any(word in text for word in ["swiggy","zomato","restraunt"]):
        return("food")
    elif any(word in text for word in["uber","ola","rapido"]):
        return("transport")
    elif any(word in text for word in["netflix","prime","hotstar"]):
        return("Entertainment")
    elif any(word in text for word in["electricity","Water","bill","gas","recharge"]):
        return("Bills")
    elif any(word in text for word in["amazon","flipkart","myntra","mart"]):
        return("Shopping")
    elif "salary" in text:
        return("Salary")
    else:
        return "other"

df["Category"]=df["Description"].apply(categorize)
print("\nWith categories:")
print(df)
#print(df.info())
#having an absolute amount 
df["absolute"]=df["Amount"].abs()
expenses=df[df["Amount"]<0] #this is the code for getting the expenses 
category_spending=expenses.groupby("Category")["absolute"].sum()
print("\n Spending by category :")
print(category_spending)



#making the charts for this analysis 
category_spending.plot(kind="pie")
plt.title("Spending by category ")
plt.xlabel("Category")
plt.ylabel("spent money")

plt.show()

# scatter plot maybe 
df["Category Code"] = df["Category"].astype("category").cat.codes
plt.scatter(df["Category Code"],df["Amount"])
plt.title("Category vs Amount")
plt.show()