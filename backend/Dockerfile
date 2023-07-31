FROM python:3.9

WORKDIR /app/backend

COPY ./requirements.txt /app/backend/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ /app/backend/

EXPOSE 5000

ENTRYPOINT [ "flask" ]
CMD ["run", "--host", "0.0.0.0"]