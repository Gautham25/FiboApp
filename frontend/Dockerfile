FROM node:16-alpine

# Set the working directory in the container
WORKDIR /app/frontend

# Copy the package.json and package-lock.json files to the container
COPY ./package.json ./package-lock.json ./

# Install the dependencies for the frontend app
RUN npm install

# Copy the rest of the frontend app files to the container
COPY . ./

EXPOSE 3000

# Build the production-ready frontend app
# RUN npm run build
CMD ["npm", "start"]
