# Start from the official Node.js image
FROM node:latest

# Set the Current Working Directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the source code into the container
COPY . .

# Expose port 3000 to the outside world
EXPOSE 3000

# Build the Next.js app
RUN npm run build

# Command to run the executable
CMD ["npm", "start"]