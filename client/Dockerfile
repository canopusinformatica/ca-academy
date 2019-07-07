FROM node

WORKDIR /code/client

COPY package.json /code/client
COPY yarn.lock /code/client

RUN yarn

COPY . /code/client

EXPOSE 5000

CMD ["yarn", "start"]
