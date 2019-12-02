from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'nodes' : 'Number of Nodes'
    },
        
    {
        'basestations': 'Number of Base Stations'
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title= 'About')

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = RegistrationForm()
    if form.validate_on_submit():
        #flash(f'Number of Nodes {form.nodes.data}!', 'success')
        #flash(f'Number of Base Stations {form.basestations.data}!', 'success')
        return redirect(url_for('simulation'))
    return render_template('create.html', title='Create', form=form)

@app.route('/simulation')
def simulation():
    return render_template('simulation.html', title= 'Simulation')

if __name__ == '__main__':
    app.run(debug=True)
