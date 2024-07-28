FROM node:18.18.2

# Set working directory inside the container
WORKDIR /backend

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install --omit=dev --no-fund --no-audit

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 3002

CMD [ "npm", "start" ]