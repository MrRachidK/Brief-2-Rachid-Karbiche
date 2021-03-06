{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3",
   "language": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "source": [
    "Importation des modules SQLite3, Pandas puis connexion à la base de données"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "source": [
    "import sqlite3\n",
    "import pandas as pd\n",
    "\n",
    "conn = sqlite3.connect('e_commerce.db')\n",
    "c = conn.cursor()"
   ],
   "cell_type": "code",
   "metadata": {},
   "execution_count": 1,
   "outputs": []
  },
  {
   "source": [
    "Création de la table Products"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x1e729ce1030>"
      ]
     },
     "metadata": {},
     "execution_count": 2
    }
   ],
   "source": [
    "c.execute('''CREATE TABLE IF NOT EXISTS Products (\n",
    "    product_id text NOT NULL PRIMARY KEY, \n",
    "    product_category_name text,\n",
    "    product_name_lenght integer,\n",
    "    product_description_lenght integer,\n",
    "    product_photos_qty integer,\n",
    "    product_weight_g integer,\n",
    "    product_length_cm integer,\n",
    "    product_height_cm integer,\n",
    "    product_width_cm integer\n",
    "    )''')"
   ]
  },
  {
   "source": [
    "Création de la table Geolocation"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x1e729ce1030>"
      ]
     },
     "metadata": {},
     "execution_count": 3
    }
   ],
   "source": [
    "c.execute('''CREATE TABLE IF NOT EXISTS Geolocation (\n",
    "    geolocation_zip_code_prefix integer NOT NULL PRIMARY KEY,\n",
    "    geolocation_city text NOT NULL,\n",
    "    geolocation_state text\n",
    "    )''')"
   ]
  },
  {
   "source": [
    "Création de la table Sellers"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x1e729ce1030>"
      ]
     },
     "metadata": {},
     "execution_count": 4
    }
   ],
   "source": [
    "c.execute('''CREATE TABLE IF NOT EXISTS Sellers (\n",
    "    seller_id text NOT NULL PRIMARY KEY, \n",
    "    seller_zip_code_prefix integer NOT NULL,\n",
    "    seller_city integer NOT NULL,\n",
    "    seller_state text NOT NULL,\n",
    "    FOREIGN KEY (seller_zip_code_prefix) REFERENCES Geolocation (geolocation_zip_code_prefix)\n",
    "    )''')"
   ]
  },
  {
   "source": [
    "Création de la table Customers"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x1e729ce1030>"
      ]
     },
     "metadata": {},
     "execution_count": 5
    }
   ],
   "source": [
    "c.execute('''CREATE TABLE IF NOT EXISTS Customers (\n",
    "    customer_id text NOT NULL PRIMARY KEY, \n",
    "    customer_unique_id text NOT NULL,\n",
    "    customer_zip_code_prefix integer NOT NULL,\n",
    "    customer_city text NOT NULL,\n",
    "    customer_state text NOT NULL,\n",
    "    FOREIGN KEY (customer_zip_code_prefix) REFERENCES Geolocation (geolocation_zip_code_prefix)\n",
    "    )''')"
   ]
  },
  {
   "source": [
    "Création de la table Orders"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x1e729ce1030>"
      ]
     },
     "metadata": {},
     "execution_count": 6
    }
   ],
   "source": [
    "c.execute('''CREATE TABLE IF NOT EXISTS Orders (\n",
    "    order_id text NOT NULL PRIMARY KEY, \n",
    "    customer_id text NOT NULL,\n",
    "    order_status datetime default current_timestamp,\n",
    "    order_purchase_timestamp datetime default current_timestamp,\n",
    "    order_approved_at datetime,\n",
    "    order_delivered_carrier_date datetime,\n",
    "    order_delivered_customer_date datetime,\n",
    "    order_estimated_delivery_date datetime,\n",
    "    FOREIGN KEY (customer_id) REFERENCES Customers (customer_id)\n",
    "    )''')"
   ]
  },
  {
   "source": [
    "Création de la table Payments"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x1e729ce1030>"
      ]
     },
     "metadata": {},
     "execution_count": 7
    }
   ],
   "source": [
    "c.execute('''CREATE TABLE IF NOT EXISTS Orders_payments (\n",
    "    order_id text NOT NULL, \n",
    "    payment_sequential text NOT NULL,\n",
    "    payment_type text,\n",
    "    payment_installments integer NOT NULL,\n",
    "    payment_value integer NOT NULL,\n",
    "    FOREIGN KEY (order_id) REFERENCES Orders (order_id)\n",
    "    )''')"
   ]
  },
  {
   "source": [
    "Création de la table Order_reviews"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x1e729ce1030>"
      ]
     },
     "metadata": {},
     "execution_count": 8
    }
   ],
   "source": [
    "c.execute('''CREATE TABLE IF NOT EXISTS Orders_reviews (\n",
    "    review_id text NOT NULL PRIMARY KEY,\n",
    "    order_id text NOT NULL, \n",
    "    review_score integer NOT NULL,\n",
    "    review_comment_title text,\n",
    "    review_comment_message text,\n",
    "    review_creation_date datetime NOT NULL,\n",
    "    review_answer_timestamp datetime NOT NULL,\n",
    "    FOREIGN KEY (order_id) REFERENCES Orders (order_id)\n",
    "    )''')"
   ]
  },
  {
   "source": [
    "Création de la table Orders_items"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x1e729ce1030>"
      ]
     },
     "metadata": {},
     "execution_count": 9
    }
   ],
   "source": [
    "c.execute('''CREATE TABLE IF NOT EXISTS Orders_items (\n",
    "    order_id text NOT NULL, \n",
    "    order_item_id int NOT NULL,\n",
    "    product_id text NOT NULL,\n",
    "    seller_id text NOT NULL,\n",
    "    shipping_limit_date datetime NOT NULL,\n",
    "    price numeric NOT NULL,\n",
    "    freight_value numeric NOT NULL,\n",
    "    FOREIGN KEY (order_id) REFERENCES Orders (order_id),\n",
    "    FOREIGN KEY (product_id) REFERENCES Products (product_id),\n",
    "    FOREIGN KEY (seller_id) REFERENCES Sellers (seller_id)\n",
    "    )''')"
   ]
  }
 ]
}