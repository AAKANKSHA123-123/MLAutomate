# 1. Start from a lightweight Python image
FROM python:3.13-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy your app code into the container
COPY linear_regression_app.py /app/

# 4. Install dependencies
RUN pip install fastapi uvicorn scikit-learn numpy

# 5. Expose the port your app runs on
EXPOSE 8000

# 6. Command to run the app
CMD ["uvicorn", "linear_regression_app:app", "--host", "127.0.0.1", "--port", "8000"]
