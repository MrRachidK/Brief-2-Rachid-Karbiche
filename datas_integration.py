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
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3\n",
    "import pandas as pd\n",
    "import tables_creation\n",
    "\n",
    "conn = sqlite3.connect('e_commerce.db')\n",
    "c = conn.cursor()"
   ]
  },
  {
   "source": [
    "Intégration des données des fichiers CSV dans les différentes tables créées"
   ],
   "cell_type": "markdown",
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"Importation des données de Products dans la table Products\"\"\"\n",
    "\n",
    "products = pd.read_csv('olist_products_dataset.csv')\n",
    "products.to_sql('Products', conn, if_exists='replace', index = False)\n",
    "\n",
    "\n",
    "\"\"\"Importation des données de Geolocation dans la table Geolocation\"\"\"\n",
    "\n",
    "geolocation = pd.read_csv('olist_geolocation_dataset.csv')\n",
    "\n",
    "\"\"\" Suppression des doublons de la colonne geolocation_zip_code_prefix \"\"\"\n",
    "\n",
    "geolocation_df = pd.DataFrame(geolocation)\n",
    "geolocation.drop_duplicates(subset=['geolocation_zip_code_prefix']).to_sql('Geolocation', conn, index = False, if_exists='replace')\n",
    "\n",
    "\n",
    "\"\"\"Importation des données de Sellers dans la table Sellers\"\"\"\n",
    "\n",
    "sellers = pd.read_csv('olist_sellers_dataset.csv')\n",
    "sellers.to_sql('Sellers', conn, if_exists='replace', index = False)\n",
    "\n",
    "\n",
    "\"\"\"Importation des données de Customers dans la table Customers\"\"\"\n",
    "\n",
    "customers = pd.read_csv('olist_customers_dataset.csv')\n",
    "customers.to_sql('Customers', conn, if_exists='replace', index = False)\n",
    "\n",
    "\n",
    "\"\"\"Importation des données de Orders dans la table Orders\"\"\"\n",
    "\n",
    "orders = pd.read_csv('olist_orders_dataset.csv')\n",
    "orders.to_sql('Orders', conn, if_exists='replace', index = False)\n",
    "\n",
    "\n",
    "\"\"\"Importation des données de Order_payments dans la table Orders_payments\"\"\"\n",
    "\n",
    "order_payments = pd.read_csv('olist_order_payments_dataset.csv')\n",
    "order_payments.to_sql('Orders_payments', conn, if_exists='replace', index = False)\n",
    "\n",
    "\n",
    "\"\"\"Importation des données de Order_reviews dans la table Orders_reviews\"\"\"\n",
    "\n",
    "order_reviews = pd.read_csv('olist_order_reviews_dataset.csv')\n",
    "\n",
    "\"\"\" Suppression des doublons de la colonne review_id \"\"\"\n",
    "\n",
    "order_reviews_df = pd.DataFrame(order_reviews)\n",
    "keep_duplicates = order_reviews_df.drop_duplicates(subset=['review_id']).to_sql(name='Orders_reviews', con=conn, index = False, if_exists='replace')\n",
    "\n",
    "\n",
    "\"\"\"Importation des données de Order_items dans la table Orders_items\"\"\"\n",
    "\n",
    "order_items = pd.read_csv('olist_order_items_dataset.csv')\n",
    "order_items.to_sql('Orders_items', conn, if_exists='replace', index = False)\n"
   ]
  }
 ]
}