from flask import Flask, render_template, request

app = Flask(__name__)


# ---------------- SUPERMARKET CHATBOT ----------------

def get_response(user_input):
    user_input = user_input.lower()

    # Greeting
    if "hi" in user_input or "hii" in user_input or "hello" in user_input:
        return "Hello! 👋 Welcome to FreshMart Supermarket. How can I help you?"

    # Products
    elif "product" in user_input or "available" in user_input:
        return "We have groceries, vegetables, fruits, dairy products, snacks, beverages, personal care products, and household items."

    # Vegetables
    elif "vegetable" in user_input:
        return "We have tomatoes, potatoes, onions, carrots, beans, cabbage, and many fresh vegetables."

    # Fruits
    elif "fruit" in user_input:
        return "We have apples, bananas, oranges, grapes, mangoes, watermelon, and other fresh fruits."

    # Milk
    elif "milk" in user_input:
        return "We have fresh milk, curd, butter, cheese, and other dairy products."

    # Price
    elif "price" in user_input or "cost" in user_input:
        return "Please tell me the product name. I can help you check the available price."

    # Offers
    elif "offer" in user_input or "discount" in user_input:
        return "🎉 Today's Offer: Get 10% off on selected grocery products!"

    # Opening time
    elif "open" in user_input or "timing" in user_input:
        return "Our supermarket is open from 8:00 AM to 10:00 PM every day."

    # Location
    elif "location" in user_input or "where" in user_input:
        return "📍 FreshMart Supermarket is located near the Main Bus Stand."

    # Delivery
    elif "delivery" in user_input:
        return "🚚 Yes! We provide home delivery for orders above ₹500."

    # Payment
    elif "payment" in user_input or "pay" in user_input:
        return "We accept Cash, UPI, Credit Card, Debit Card, and online payments."

    # Order
    elif "order" in user_input:
        return "To place an order, please select your products and contact our supermarket billing counter."

    # Contact
    elif "contact" in user_input or "phone" in user_input:
        return "📞 You can contact FreshMart Supermarket at 9876543210."

    # Thanks
    elif "thank" in user_input or "thanks" in user_input:
        return "You're welcome! 😊 Happy shopping!"

    # Bye
    elif "bye" in user_input:
        return "Goodbye! 👋 Thank you for visiting FreshMart Supermarket. Have a great day!"

    # Default response
    else:
        return "Sorry, I didn't understand that. You can ask me about products, prices, offers, timings, delivery, payment, or orders."


# ---------------- FLASK ROUTE ----------------

@app.route('/', methods=['GET', 'POST'])
def chat():

    response = ""

    if request.method == 'POST':

        user_input = request.form['user_input']

        response = get_response(user_input)

    return render_template('index.html', response=response)


# ---------------- RUN APPLICATION ----------------

if __name__ == '__main__':
    app.run(debug=True)