# Quantified Self Back-end Django

You'll need Python3 and Django 2.0.7 installed.

## Initial Setup

1. Clone this repository

  ```shell
  git clone git@github.com:hmesander/quantified-self-django.git
  ```
2. Change into the `qs_django` directory

  ```shell
  cd qs_django
  ```
3. Create a virtual environment and activate it

  ```shell
  virtualenv -p python3 .venv
  source .venv/bin/activate
  ```
4. Upgrade pip and install dependencies

  ```shell
  pip3 install --upgrade pip
  pip3 install -r requirements/local.txt
  ```

3. Set up the database in psql

  ```shell
  CREATE DATABASE food_tracker_django2;
  CREATE DATABASE food_tracker_django2_test;
  ```

4. Migrate and Seed

  ```shell
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```

5. Run test suite

  ```shell
    python3 manage.py test
  ```
<hr>

## Running the Server Locally

  ```shell
  python3 manage.py runserver
  ```

  Visit `http://localhost:8000/` in your browser.

<hr>  

## Deployments

Front End deployed with Surge: http://quantified-self-django.surge.sh/

Backend deployed with Heroku: https://fierce-fjord-58365.herokuapp.com/

<hr>

## API Endpoints

**Food Index**
---
  Returns all foods currently in the database or 404 if no foods exist in database.

* **URL**

  /api/v1/foods

* **Method:**

  `GET`

* **Success Response:**

  * **Code:** 200 <br />
    **Content Example:** `[
    {
        "id": 1,
        "name": "Ice cream, rich",
        "calories": 369
    },
    {
        "id": 2,
        "name": "Soft serve ice cream",
        "calories": 348
    },
    {
        "id": 3,
        "name": "Ice cream bar, chocolate covered",
        "calories": 278
    }
  ]`

* **Error Response:**

  * **Code:** 404 NOT FOUND <br />

<hr>

**Show Food**
---
  Returns the food object with the specific :id you’ve passed or 404 if food is not found

* **URL**

  /api/v1/foods/:id

* **Method:**

  `GET`

* **Success Response:**

  * **Code:** 200 <br />
    **Content Example:** `{ "id": 1, "name": "Banana", "calories": 150 }`

* **Error Response:**

  * **Code:** 404 NOT FOUND <br />

<hr>

**Create Food**
---
  Create a new food with given parameters and returns the newly created food, or returns 400 if food was not created successfully. Both name and calories are required.

* **URL**

  /api/v1/foods

* **Method:**

  `POST`

* **Data Parameters**
`{ "food": { "name": "Name of food here", "calories": "Calories here"} }`

* **Success Response:**

  * **Code:** 200 <br />
    **Content Example:** `{ "id": 1, "name": "Banana", "calories": 150 }`

* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />

<hr>

**Update Food**
---
  Updates a food with given parameters and returns the updated food, or returns 400 if food was not updated successfully. Both name and calories are required.

* **URL**

  /api/v1/foods/:id

* **Method:**

  `PATCH`

* **Data Parameters**
`{ "food": { "name": "Name of food here", "calories": "Calories here"} }`

* **Success Response:**

  * **Code:** 200 <br />
    **Content Example:** `{ "id": 1, "name": "Banana", "calories": 150 }`

* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />

<hr>

**Delete Food**
---
  Deletes the food with the given id and returns a 204, or returns a 404 if food cannot be found.

* **URL**

  /api/v1/foods/:id

* **Method:**

  `DELETE`

* **Success Response:**

  * **Code:** 204 <br />

* **Error Response:**

  * **Code:** 404 NOT FOUND <br />

<hr>

**Meal Index**
---
  Returns all the meals in the database along with their associated foods.

* **URL**

  /api/v1/meals

* **Method:**

  `GET`

* **Success Response:**

  * **Code:** 200 <br />
    **Content Example:** `[
    {
        "id": 1,
        "name": "Breakfast",
        "foods": [
            {
                "id": 1,
                "name": "Banana",
                "calories": 150
            },
            {
                "id": 6,
                "name": "Yogurt",
                "calories": 550
            },
            {
                "id": 12,
                "name": "Apple",
                "calories": 220
            }
        ]
    },
    {
        "id": 2,
        "name": "Snack",
        "foods": [
            {
                "id": 1,
                "name": "Banana",
                "calories": 150
            },
            {
                "id": 9,
                "name": "Gum",
                "calories": 50
            },
            {
                "id": 10,
                "name": "Cheese",
                "calories": 400
            }
        ]
    },
    {
        "id": 3,
        "name": "Lunch",
        "foods": [
            {
                "id": 2,
                "name": "Bagel Bites - Four Cheese",
                "calories": 650
            },
            {
                "id": 3,
                "name": "Chicken Burrito",
                "calories": 800
            },
            {
                "id": 12,
                "name": "Apple",
                "calories": 220
            }
        ]
    },
    {
        "id": 4,
        "name": "Dinner",
        "foods": [
            {
                "id": 1,
                "name": "Banana",
                "calories": 150
            },
            {
                "id": 2,
                "name": "Bagel Bites - Four Cheese",
                "calories": 650
            },
            {
                "id": 3,
                "name": "Chicken Burrito",
                "calories": 800
            }
        ]
    }
]`

<hr>

**Show Meal**
---
Returns all the foods associated with the meal with an id specified by :meal_id or a 404 if the meal is not found

* **URL**

  /api/v1/meals/:meal_id/foods

* **Method:**

  `GET`

* **Success Response:**

  * **Code:** 200 <br />
    **Content Example:** `{
    "id": 1,
    "name": "Breakfast",
    "foods": [
        {
            "id": 1,
            "name": "Banana",
            "calories": 150
        },
        {
            "id": 6,
            "name": "Yogurt",
            "calories": 550
        },
        {
            "id": 12,
            "name": "Apple",
            "calories": 220
        }
    ]
}`

* **Error Response:**

  * **Code:** 404 NOT FOUND <br />

<hr>

**Associate Food with Meal**
---
Adds the food with :id to the meal with :meal_id and returns 201 and success message.  If either the food or meal cannot be found, returns 404.

* **URL**

  /api/v1/meals/:meal_id/foods/:id

* **Method:**

  `POST`

* **Success Response:**

  * **Code:** 201 <br />
    **Content Example:** `{ "message": "Successfully added FOODNAME to MEALNAME"
}`

* **Error Response:**

  * **Code:** 404 NOT FOUND <br />

<hr>

**Disassociate Food with Meal**
----
Removes the food with :id from the meal with :meal_id and returns 200 and success message.  If either the food or meal cannot be found, returns 404.

* **URL**

  /api/v1/meals/:meal_id/foods/:id

* **Method:**

  `DELETE`

* **Success Response:**

  * **Code:** 200 <br />
    **Content Example:** `{
    "message": "Successfully deleted FOODNAME from MEALNAME"
}`

* **Error Response:**

  * **Code:** 404 NOT FOUND <br />

<hr>
