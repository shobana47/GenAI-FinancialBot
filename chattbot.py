def chattbot(user_query):
    responses = {
        "What is the total revenue?": "The total revenue is $168,088.",
        "How has net income changed over the last year?": "The net income has increased by $10,000 over the last year.",
        "What are the total assets?": "The total assets are $344,607.",
        "What are the total liabilities?": "The total liabilities are $198,304.",
        "What is the cash flow from operating activities?": "The cash flow from operating activities is $89,192."
    }
    return responses.get(user_query, "Sorry, I can only provide information on predefined queries.")
while 1:
    user_query = input("Ask a financial question: ")
    response = chattbot(user_query)
    print(response)
