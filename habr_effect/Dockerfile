FROM python:3.9

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip

RUN apt update

RUN apt install dos2unix

WORKDIR /habr_effect

COPY . .

RUN dos2unix /habr_effect/manage.py

RUN useradd -rms /bin/bash admin && chmod 777 /opt /run

RUN mkdir /habr_effect/static && mkdir /habr_effect/media && chown -R admin:admin /habr_effect && chmod 755 /habr_effect

RUN chmod +x manage.py

RUN pip install -r requirements.txt

USER admin

CMD ["gunicorn", "-b", "0.0.0.0:8000", "habr_effect.wsgi:application"]
