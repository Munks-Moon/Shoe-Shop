# Shoe Shop App

----

## Purpose

This project is primarily being used to demonstrate the author's ability to produce backend architecture directly related to payment processing and other online store functions.

## Description 

The Shuswap Shoe Shop is a fictional online shoe retailer intended to be used a demo.

----

## Features

- **Product Listing:** Displays list of shoes with details such as name, price, and images.
- **Shopping Cart:** Users can add and remove items from their shopping cart.
- **Checkout Process:** Seamless checkout process with payment integration (Stripe).

### Admin Features

- **PDF Invoices**: Once a purchase is completed, a PDF invoice is made available to the admin and could then be sent out to the customer.

### Accessing Admin Features

- **Creating a Superuser:** If you need access to admin features, you can create a superuser account. This is done through the terminal using the command `python manage.py createsuperuser`.
- **Admin Dashboard:** Once you have created a superuser account, navigate to the `/admin` page. Here, you will have access to a comprehensive dashboard with various administrative tools and features.

## Installation

To run this app, the following are required: Python (v3.9+).

### How to run locally

After cloning the app to your computer, navigate to the project directory in the terminal. Initiate the virtual environment, install the requirements, migrate and run the project.

1. Virtual environment command: 
`env\Scripts\activate`

2. Install the project requirements: 
`pip install -r requirements.txt`

3. Migrate and run the project:
`python manage.py migrate`
`python manage.py runserver`

## Payment Setup

In order to completely experience the payment process within this app, there are several needed components. This may be a lengthy process for some. 

### Stripe Setup

This app has implemented Stripe as it's primary payment processor.

1. Create an account https://dashboard.stripe.com/register and verify your email. On your dashboard test mode should be activated.

2. Add an account with the name of your choice and click save.

3. Go to https://dashboard.stripe.com/test/apikeys and replace the STRIPE_PUBLISHABLE_KEY and STRIPE_SECRET_KEY in the settings.py with the keys under the "Standard Keys" heading.

- **Using Stripe Checkout (Test Mode):** For successful payments, use the card number "4242 4242 4242 4242", any 3 digits for the CVC, and any future date for the card expiry date. Visit  https://dashboard.stripe.com/test/payments to view all payments made using this app.

### Using RabbitMQ, Celery, and Webhooks

These tools are used within this app to facilitate an efficient payment system that updates in real-time.

- **RabbitMQ:** A message broker that allows for the communication of tasks.
- **Celery:** A task queue system that allows you to execute tasks asynchronously. 
- **Webhooks:** HTTP callbacks that allow the app to recieve real-time notifications from external services such as Stripe.

Docker Setup

1. Install Docker (https://docs.docker.com/get-docker/). 

RabbitMQ Setup

1. Run `docker pull rabbitmq`

2. Run `docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management`. Keep this terminal running.

3. Open http://127.0.0.1:15672/ and login as a guest. This is where you will can monitor activity for RabbitMQ.

Celery Setup

1. Open a new terminal and run `celery -A mystore worker -l info`.

Webhooks Setup

1. Visit  https://dashboard.stripe.com/test/webhooks and click on "Test in a local environment".

2. Replace STRIPE_WEBHOOK_SECRET in settings.py with endpoint_secret within https://dashboard.stripe.com/test/webhooks.

3. Install Stripe CLI https://stripe.com/docs/stripe-cli#install and unzip the file. 

4. Go to the directory where the stripe.exe file is located.

5. Run `./stripe login` and visit the link.

6. Verify that the pairing code in the Stripe CLI matches the one shown on the website and click on "Allow access".

7. Run `stripe listen --forward-to localhost:8000/payment/webhook/`

8. Visit https://dashboard.stripe.com/test/webhooks where you will see your device in the local listeners.

----

### CSS Note

This project has not been made mobile responsive. If viewed on a mobile device the dimensions will be skewed.

## Contact

Hunter Weselosky - huntermweselosky@gmail.com