def categorize(text):

        text = str(text).lower()

        if any(word in text for word in ["swiggy", "zomato", "restaurant"]):
            return "Food"

        elif any(word in text for word in ["uber", "ola", "rapido"]):
            return "Transport"

        elif any(word in text for word in ["netflix", "prime", "hotstar"]):
            return "Entertainment"

        elif any(word in text for word in ["electricity", "water", "bill", "gas", "recharge"]):
            return "Bills"

        elif any(word in text for word in ["amazon", "flipkart", "myntra", "mart"]):
            return "Shopping"

        elif "salary" in text:
            return "Salary"

        else:
            return "Other"
