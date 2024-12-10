import os
from app import create_app


port = int(os.getenv("PORT", 5000))

app = create_app()

if __name__ == "__main__":
    print(f"Server started in port {port}")
    app.run(host="0.0.0.0", port=port)
