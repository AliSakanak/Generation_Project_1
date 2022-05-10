FROM python:3.10
WORKDIR /application
COPY /couriers.dat .
COPY /orders.dat .
COPY /products.dat .
COPY /MiniProject.py .
CMD python /application/MiniProject.py