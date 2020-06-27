from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def IndexPage():
    return render_template('index.html')

@app.route('/LoginPage')
def LoginPage():
    return render_template('login.html')

@app.route('/RegisterPage')
def RegisterPage():
    return render_template('register.html')

@app.route('/ContactPage')
def ContactPage():
    return render_template('contact.html')

@app.route('/ProductsPage')
def ProductsPage():
    return render_template('products.html')

@app.route('/SpecialOfferPage')
def SpecialOfferPage():
    return render_template('special_offer.html')

@app.route('/ProductSummaryPage')
def ProductSummaryPage():
    return render_template('product_summary.html')

@app.route('/ProductDetailsPage')
def ProductDetailsPage():
    return render_template('product_details.html')


if __name__ == '__main__':
    app.run(debug=True)
