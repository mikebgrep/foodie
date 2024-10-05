FROM nginx:latest

COPY ./foodie_be/nginx.conf /etc/nginx/nginx.conf
COPY ./foodie_be/foodie.nginx.conf /etc/nginx/sites-available/
RUN mkdir /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/foodie.nginx.conf /etc/nginx/sites-enabled/

CMD ["nginx", "-g", "daemon off;"]