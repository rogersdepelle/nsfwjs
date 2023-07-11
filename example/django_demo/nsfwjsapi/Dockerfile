FROM node

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json ./
RUN npm install
RUN npm rebuild @tensorflow/tfjs-node --build-from-source
RUN if [ "$NODE_ENV" = "production" ]; then npm ci --omit=dev; fi

# Bundle app source
COPY . .

EXPOSE 8080
CMD [ "node", "server.js" ]
