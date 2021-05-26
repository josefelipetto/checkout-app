FROM node:16

# Set workdir to /app
WORKDIR /app

# copy package*.json files to workdir
COPY package*.json ./

ENV NODE_ENV development

# install dependecies
RUN npm install

# exposes port 8080
EXPOSE 8080

# run serve command
CMD ["npm", "run", "serve"]