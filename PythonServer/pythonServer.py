from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    "host": "sql6.freesqldatabase.com",
    "user": "sql6635701",
    "password": "hEF4kmDk5w",
    "database": "sql6635701",
}

# Endpoint to receive sensor data
@app.route('/api/temperature', methods=['POST'])
def save_sensor_data():
    try:
        data = request.get_json()
        SensorValue1 = data.get('SensorValue1')
        SensorValue2 = data.get('SensorValue2')

        # Connect to the MySQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert sensor data into the database
        query = "INSERT INTO temperature (SensorValue1, SensorValue2) VALUES (%s, %s)"
        values = (SensorValue1, SensorValue2)
        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({"message": "Sensor data saved successfully."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Specify the port number (e.g., 5000)
    port = 5000

    print(f"Server is running on http://localhost:{port}")
    print("Connected to the database.")

    # Run the Flask app
    app.run(debug=True, port=port)
