from core import *
from core.modules.data import *

@app.route('/')
def index_page():
    return render_template('index.html',data=enumerate(data_bcg.query.all(),1))

# add data ..
@app.route('/add-product',methods=["POST","GET"])
def add_data():
    if request.method == 'POST':
        try:
            name = request.form['name']
            sku = request.form['sku']
            data_product = data_bcg(name=name,sku=sku)
            db.session.add(data_product) # add session 
            db.session.commit()
        except Exception as e:
            return e # show an error 

        return redirect(url_for('index_page'))
    else:return render_template('index.html',data=enumerate(data_bcg.query.all(),1))

# delete data 
@app.route('/delete/<int:id>')
def delete_data(id):
    datasis = data_bcg.query.filter_by(id=id).first() # filter by id 
    db.session.delete(datasis)
    db.session.commit()
    return redirect(url_for('index_page'))

# edit data
@app.route('/edit/<int:id>',methods=["GET","POST"])

def edit_page(id):
    if request.method == 'POST':
        datasis = data_bcg.query.filter_by(id=id).first()
        datasis.name = request.form['name']
        datasis.sku = request.form['sku']
        db.session.commit()
        return redirect(url_for('index_page'))
    get_data = data_bcg.query.filter_by(id=id).first()
    return render_template('edit_page.html',name=get_data.name,sku=get_data.sku)


def query_table(id):
    return "querying id " + id