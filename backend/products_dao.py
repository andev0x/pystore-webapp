import mysql.connector

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name FROM products LEFT JOIN uom ON products.uom_id = uom.uom_id")
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    cursor.close()
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products (name, uom_id, price_per_unit) VALUES (%s, %s, %s)")
    data = (product['product_name'], int(product['uom_id']), float(product['price_per_unit']))
    cursor.execute(query, data)
    product_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    return product_id

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products WHERE product_id = %s")
    data = (product_id, )
    cursor.execute(query, data)
    connection.commit()
    cursor.close()
    return product_id 