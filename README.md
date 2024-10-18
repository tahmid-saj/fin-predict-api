# fin-predict-api

API for finance forecasting: predicting prices of BTC, stocks, forex etc, retrieving historic market data, getting financial advice and more. Developed with Django, TensorFlow / PyTorch, AWS, OpenAI API.

The directory structure is as follows:

```
fin-predict-api/
├── chatbot/
│   ├── admin.py
│   ├── apps.py
│   ├── controllers.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── __pycache__/
│   │       └── __init__.cpython-312.pyc
│   ├── models.py
│   ├── permissions.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── __init__.py
│   └── __pycache__/
│       ├── admin.cpython-312.pyc
│       ├── apps.cpython-312.pyc
│       ├── controllers.cpython-312.pyc
│       ├── models.cpython-312.pyc
│       ├── permissions.cpython-312.pyc
│       ├── urls.cpython-312.pyc
│       ├── views.cpython-312.pyc
│       └── __init__.cpython-312.pyc
├── conf/
│   ├── mongodb/
│   │   ├── mongodb_conf.py
│   │   └── __pycache__/
│   │       └── mongodb_conf.cpython-312.pyc
│   └── openai/
│       ├── openai_conf.py
│       └── __pycache__/
│           └── openai_conf.cpython-312.pyc
├── db.sqlite3
├── fin_predict_api/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── __init__.py
│   └── __pycache__/
│       ├── settings.cpython-312.pyc
│       ├── urls.cpython-312.pyc
│       ├── wsgi.cpython-312.pyc
│       └── __init__.cpython-312.pyc
├── manage.py
├── market_data/
│   ├── admin.py
│   ├── apps.py
│   ├── controllers.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── __pycache__/
│   │       └── __init__.cpython-312.pyc
│   ├── models.py
│   ├── permissions.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── __init__.py
│   └── __pycache__/
│       ├── admin.cpython-312.pyc
│       ├── apps.cpython-312.pyc
│       ├── controllers.cpython-312.pyc
│       ├── models.cpython-312.pyc
│       ├── permissions.cpython-312.pyc
│       ├── urls.cpython-312.pyc
│       ├── views.cpython-312.pyc
│       └── __init__.cpython-312.pyc
├── market_predictions/
│   ├── admin.py
│   ├── apps.py
│   ├── controllers.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── __pycache__/
│   │       └── __init__.cpython-312.pyc
│   ├── models.py
│   ├── permissions.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── __init__.py
│   └── __pycache__/
│       ├── admin.cpython-312.pyc
│       ├── apps.cpython-312.pyc
│       ├── controllers.cpython-312.pyc
│       ├── models.cpython-312.pyc
│       ├── permissions.cpython-312.pyc
│       ├── urls.cpython-312.pyc
│       ├── views.cpython-312.pyc
│       └── __init__.cpython-312.pyc
├── README.md
├── requirements.txt
├── requirements_dev.txt
├── services/
│   ├── mongodb/
│   │   ├── mongodb.py
│   │   └── __pycache__/
│   │       └── mongodb.cpython-312.pyc
│   └── openai/
│       ├── openai.py
│       └── __pycache__/
│           └── openai.cpython-312.pyc
├── utils/
│   ├── api_requests/
│   │   ├── chatbot_requests.py
│   │   ├── market_data_requests.py
│   │   ├── market_predictions_requests.py
│   │   └── __pycache__/
│   │       ├── chatbot_requests.cpython-312.pyc
│   │       ├── market_data_requests.cpython-312.pyc
│   │       └── market_predictions_requests.cpython-312.pyc
│   ├── constants/
│   │   ├── chatbot_constants.py
│   │   ├── market_data_constants.py
│   │   ├── market_predictions_constants.py
│   │   └── __pycache__/
│   │       ├── market_data_constants.cpython-312.pyc
│   │       └── market_predictions_constants.cpython-312.pyc
│   ├── errors/
│   └── helpers/
│       ├── market_data_helpers.py
│       ├── shared_helpers.py
│       └── __pycache__/
│           ├── market_data_helpers.cpython-312.pyc
│           └── shared_helpers.cpython-312.pyc
└── vercel.json
```
