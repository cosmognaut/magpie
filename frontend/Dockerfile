# First, we take the node base image and have this build stage where we build the application

FROM node:24-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
CMD ["npx", "vite", "--host", "--port", "90"]
