from concurrent import futures
import grpc
import recommendations_pb2
import recommendations_pb2_grpc

books_by_category = {
    "fantasy": [
        "The Lord of the Rings",
        "Harry Potter and the Philosopher's Stone",
        "The Hobbit",
    ],
    "scifi": [
        "Dune",
        "Foundation",
        "Ender's Game",
    ],
    "mystery": [
        "The Da Vinci Code",
        "Sherlock Holmes",
        "And Then There Were None",
    ],
}

class RecommendationsService(recommendations_pb2_grpc.RecommendationsServicer):
    def RecommendBook(self, request, context):
        category = request.category
        if category in books_by_category:
            recommendations = books_by_category[category]
        else:
            recommendations = []
        return recommendations_pb2.BookRecommendation(recommendations=recommendations)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(
        RecommendationsService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()



