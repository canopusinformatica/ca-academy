FROM node

WORKDIR /code/client

COPY ./app/package.json ./app/yarn.lock /code/client

RUN yarn

COPY ./app /code/client

CMD ["yarn", "start"]

EXPOSE 5000
