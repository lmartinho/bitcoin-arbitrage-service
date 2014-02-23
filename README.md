# bitcoin-arbitrage-service - RESTful API for https://github.com/maxme/bitcoin-arbitrage (opportunity detector)

Just a simple Flask app to expose a queue of current opportunities detected by bitcoin-arbitrage, running the custom Queuer observer.

Created during the [AngularJS hackathon on Sand Hill Road](http://www.meetup.com/AngularJS-Silicon-Valley/events/166270732). Probably not useful at this stage.

# Installation And Configuration

Install `virtualenv` using your platform's package manager

Create a virtualenv for the app's dependencies:
    virtualenv flask

Install flask to the virtualenv
    flask/bin/pip install flask

Install pymongo
    flask/bin/pip install pymongo

Add execute permission to the application file
    chmod +x app.py

Run the app
    ./app.py

Test the API endpoint at http://localhost:5000/bitcoin-arbitrage/api/v1.0/opportunities .
You should get a map with an empty array in the `opportunities` key.

    cp arbitrage/config.py-example arbitrage/config.py

# LICENSE

Public Domain
