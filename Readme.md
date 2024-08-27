# How to Launch the Application

To launch the application follow these steps:

1. **Build and Start the Application**

   Run the following command to build and start the application in detached mode:

   ```bash
   docker-compose up -d --build
   ```
2. **Access the Web Container**

   Once the containers are up and running, access the web container by executing:

   ```bash
   docker compose exec -u root web bash
   ```

3. **Initialize the Database**

   **Inside the web container**, initialize the database by running:

   ```
   flask init-db
   ```

4. **Populate the Database with Data**

   After initializing, load the necessary data into the database:

   ```
   flask load-data out
   ```

5. Verify the Result

You can verify the final result by visiting the following link in your browser: 

emails: `udbbwscdnbegrmloghuf@london.com`, `tpxmuwr@somehost.ru`


[ТЫК](http://localhost:8080/)
