FROM node:17.4 as build-stage
WORKDIR /app
COPY ./app/node/ai-app .
RUN npm install
RUN npm run build

FROM nginx as production-stage
RUN mkdir /app
COPY --from=build-stage /app/dist /app
COPY ./docker/nginx/nginx.conf /etc/nginx/nginx.conf