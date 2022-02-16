from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from logic.calorie import Calorie
from logic.temperature import Temperature

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('home_page.html')


class CaloriesHomePage(MethodView):

    def get(self):
        calories_form = CaloriesForm()
        return render_template('calories_page_my.html',
                               caloriesform=calories_form)

    def post(self):
        caloriesform = CaloriesForm(request.form)
        temperature =Temperature(caloriesform.country.data, caloriesform.city.data).get()
        calorie = Calorie(float(caloriesform.weight.data), float(caloriesform.height.data), float(caloriesform.age.data), temperature=temperature)

        return render_template('calories_page_my.html',
                               result=True,
                               caloriesform=caloriesform,
                               name=caloriesform.name.data,
                               calories_needed=calorie.calculate())


class CaloriesForm(Form):

    name = StringField('Name: ', default='Aibek')
    weight = StringField('Weight: ', default="77")
    height = StringField('Height: ', default="185")
    age = StringField('Age: ', default="19")
    country = StringField('Country: ', default='kyrgyzstan')
    city = StringField('City: ', default='bishkek')

    button = SubmitField('Calculate')


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_page_my', view_func=CaloriesHomePage.as_view('calories_page_my'))

app.run(debug=True)





