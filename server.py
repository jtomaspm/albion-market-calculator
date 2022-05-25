from flask import Flask, render_template, url_for, request, redirect
import json



#initial setup
app = Flask(__name__)

cities = [
    'thetford',
    'fortsterling',
    'lymhurst',
    'bridgewatch',
    'martlock',
    'caerleon'
]



#Home
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        form = request.form
        print(form)
        city_tax_dict = {}
        for city in cities:
            if form.get(city):
                city_tax_dict[city] = int(form.get(city+'_tax'))
        print(city_tax_dict)



    else:
        return render_template('home.html')






#Start Flask App
if __name__ == "__main__":
    app.run(debug=True)

