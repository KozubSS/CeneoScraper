#import aplikacji
from app import app
#routing dla strony głównej
from flask import render_template
from flaskext.markdown import Markdown
@app.route('/')
@app.route('/index')
def index():
    return render_template("main.html")

@app.route('/about')
def about():
    with open("README.md", "r", encoding="UTF-8") as f:
        content = f.read()
    return render_template("main.html")

@app.route('/extract', methods=['POST', 'GET'])
def extract():
    form = ProductForm()
    if form.validate_on_submit():
        product_id = form.product_id.data
        page_response = requests.get("https://www.ceneo.pl/"+product_id+)
        if page_response.status_code == requests.codes['ok']:
            product = Product(product_id)
            product.extract_product()
            product.save_product()
            return redirect(url_for("product", id=product_id))
        else:
            form.product_id.errors.append("Podana wartość nie jest poprawnym kodem prodktu")
        return render_template("extract.html",form=form)

        

