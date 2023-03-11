# degreemate

A single-page web application that provides major recommendations for students at the University of Wisconsin-Madison based on their previously completed courses. An (unofficial) UW transcript is required.

Created by Andrew Logan, Will Musolf, Cooper Nasiedlak, and David Viggiano. Developed in 24 hours for CheeseHacks 2022, a University of Wisconsin-Madison hackathon. Special thanks to WebDev UW and the Google Developer Student Club for putting on a great event.

> Running the backend from MacOS has proved troublesome with CORS permissions. Recommended that it is run from a Windows machine.

# Getting Started

Set up the project by installing required packages.


```
pip install -r requirements.txt
cd client
npm install
```

Navigate to <code>Home.vue</code> and set your IP in both of the fetch calls.

Navigate back to the root directory and start the backend.

```
cd ..
flask run --host=0.0.0.0
```

Finally, start another terminal instance and start the frontend.

```
cd client
npm run serve
```
