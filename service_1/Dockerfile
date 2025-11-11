FROM node:20-alpine

WORKDIR /service_1

COPY package*.json ./
RUN npm ci --omit=dev

COPY . .

EXPOSE 8080

CMD [ "node","server.js" ]