from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL connection
app.config['MYSQL_HOST'] = 'localhost'  # or your server IP if on a different host
app.config['MYSQL_USER'] = 'api_user'
app.config['MYSQL_PASSWORD'] = 'Aeden098@321'
app.config['MYSQL_DB'] = 'subash98'

mysql = MySQL(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM coffe_tbl")  # Replace with your table name
    data = cur.fetchall()
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def add_data():
    data = request.get_json()  # Expecting JSON data
    mid   = data.get('mid') 
    name = data.get('name')
    region = data.get('region')
    roast = data.get('roast') 

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO coffe_tbl (mid, name, region, roast) VALUES (%s, %s,%s, %s)", (mid, name, region, roast))
    mysql.connection.commit()

    return jsonify({'message': 'Data inserted successfully'}), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


exit()
