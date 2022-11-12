FROM node:14.17.0-alpine as build-step

RUN mkdir -p /app
WORKDIR /app

COPY ../src/ui/package.json /app
RUN npm install
RUN npm install -g @angular/cli@14.2.9

COPY ./src/ui /app
CMD ng serve --host 0.0.0.0

# FROM nginx:alpine
# COPY --from=build-step /app/dist/to-do-ui /usr/share/nginx/html
