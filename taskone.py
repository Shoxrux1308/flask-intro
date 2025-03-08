from flask import Flask, request

app = Flask(__name__)

@app.route('/api/get-sum', methods=['GET'])
def get_sum():
    """
    this function returns sum of two number from request data.

    Returns:
        json: sum of two number

    Note:
        request data will be like this:
            /api/get-sum/?a=1&b=2
            
        response data will be like this:
            {
                "sum": 3
            }
    """ 
    a = request.args.get('a')
    b = request.args.get('b')

    if a and b:
        sum = int(a) + int(b)
        response = {
            "sum": sum
        }
        return response
    else:
        return "Please provide two numbers in query string"
    

if __name__ == "__main__":
    app.run(debug = True)