FROM postgres

# Set the environment variables
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=zaratustra

# Create a volume to store the database
VOLUME /var/lib/postgresql/data