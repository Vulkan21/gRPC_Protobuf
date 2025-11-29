from flask import Flask, jsonify
import grpc
import os
import recommendations_pb2
import recommendations_pb2_grpc

app = Flask(__name__)

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
recommendations_client = recommendations_pb2_grpc.RecommendationsStub(recommendations_channel)

@app.route("/")
def index():
    return jsonify({"message": "Marketplace API"})

@app.route("/api/books/<category>")
def get_recommendations(category):
    request = recommendations_pb2.BookCategory(category=category)
    response = recommendations_client.RecommendBook(request)
    return jsonify({"recommendations": list(response.recommendations)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



