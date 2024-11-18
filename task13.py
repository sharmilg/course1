# implement a Flask backend service that tells whether a number received as a parameter is a prime
# number or not. Use the prior prime number exercise as a starting point. For example, a GET
# request for number 31 is given as: http://127.0.0.1:5000/prime_number/31. The response must be
# in the format of {"Number":31, "isPrime":true}
''' ...................practice...........
from flask import Flask, request,jsonify
app = Flask(__name__)
@app.route('/sum')
def calculate_sum():
    args = request.args
    try:
        num1 = float(args.get('num1', 0)) #default to 0 if missing
        num2 = float(args.get('num2', 0)) #default to 0 if missing
        total_sum = num1 + num2
        response={
        "number1":num1,
        "number2":num2,
        "total_sum": total_sum
        }
        return jsonify(response)

    except(TypeError, ValueError):
        return jsonify({"error":"Invalid input:Please enter a valid numbers"}),400
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000,debug=True, use_reloader=False)
............................................................................................

# implement a Flask backend service that tells whether a number received as a parameter is a prime
# number or not. Use the prior prime number exercise as a starting point. For example, a GET
# request for number 31 is given as: http://127.0.0.1:5000/prime_number/31. The response must be
# in the format of {"Number":31, "isPrime":true}

import math
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/primeNumber")
def prime_number():
    args = request.args
    try:
        number = int(args.get('number', 0))
        if number <= 1:
            response = {
                'number': number,
                'isprime': False
            }
            return jsonify(response)

        is_prime = True
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                is_prime = False
                break

        response = {
            "Number": number,
            "isprime": is_prime
        }
        return jsonify(response)

    except ValueError:
        return jsonify({"error": "Invalid input, please provide an integer."}), 400


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)
'''
# Implement a backend service that gets the ICAO code of an airport and then returns the name and
# location of the airport in JSON format. The information is fetched from the airport database used
# on this course. For example, the GET request for EFHK would be: http://127.0.0.1:5000/airport/EFHK.
# The response must be in the format of:
# {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.
import mysql.connector
from flask import Flask, request, jsonify
app = Flask(__name__)

connection = mysql.connector.connect(
    user="sharmu",
    password="sharmilg",
    host="127.0.0.1",
    port="3306",
    database="flight_game",
    charset="utf8mb4",
    collation="utf8mb4_general_ci"

)
def fetch_airport_info(icao_code):
    cursor = connection.cursor()
    sql = "select name, municipality from airport where ident = %s"
    cursor.execute(sql,(icao_code,))
    result = cursor.fetchone()
    cursor.close()
    try:
        if result:
            return {
                "ICAO": icao_code,
                "Name": result[0],
                "Location": result[1]
            }
    except(TypeError, ValueError):
        return "Invalid Input: Please enter a valid ICAO code", 400

@app.route('/airport/<string:icao_code>', methods=['GET'])
def get_airport_info(icao_code):
    airport = fetch_airport_info(icao_code.upper())
    try:
        if airport:
            return jsonify(airport)
    except(TypeError, ValueError):
        return "Invalid Input: Please enter a valid ICAO code", 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port= 5000, debug=True, use_reloader=False)