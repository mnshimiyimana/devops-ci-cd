# DevOps-Activity

**Building and Deploying a Django Application with DevOps Practices**

**Learning Objectives:**

* Gain practical experience with Docker containerization, including multi-service applications.
* Understand the principles of Continuous Integration (CI) and Continuous Deployment (CD).
* Learn to use GitHub Actions for automated build and testing workflows.
* Develop skills in Ansible for configuration management and application deployment.
* Implement a basic web application with a database backend and email functionality.

**Assignment Details:**

1. **Project Setup:**

   * Create a simple Django project (to-do API).
   * Include essential features: user authentication, data persistence (PostgreSQL), and email notifications (using any email server like MailHog, SendGrid, etc.).

2. **Dockerization:**

   * Create separate Dockerfiles for:
     * The Django application (including Gunicorn or uWSGI as the WSGI server).
     * The PostgreSQL database.
     * Nginx web server (as a reverse proxy).
     * The chosen email server.
   * Define a `docker-compose.yml` file to orchestrate these services.
   * Ensure proper networking between containers.

3. **GitHub Actions CI Pipeline:**

   * Create a GitHub Actions workflow file (`.github/workflows/main.yml`).
   * Define jobs to:
     * Assess Code Quality (linting)
     * Build the Docker images on each push to the repository.
     * Run unit tests and integration tests within the CI environment.
     * Push successful builds to Docker Hub.

4. **Ansible Deployment:**

   * Write an Ansible playbook to automate the deployment process.
   * Tasks should include:
     * Pulling the latest Docker images from Docker Hub.
     * Configuring the target server [104.248.241.153] (use my name for both username & password).
     * Running the application using `docker-compose up -d`.

5. **Port Management:**

   * Use a unique port for the docker services to avoid conflicts since you will all be using one server. Define your ports [here](https://docs.google.com/spreadsheets/d/1dkMxTwgAWF0DCrz3BElC5Y2D6mtFd1-dENlJY3SZ0yM/edit?usp=sharing).
   * Modify the `docker-compose.yml` and Ansible playbook to use these assigned ports for Nginx, the Django application, and any exposed services.

6. **Deployment Target:**

   * Provide students with access to a shared server (cloud VM or on-premise).
   * Communicate the server's IP address or domain name, and any necessary SSH credentials.

**Assessment:**

* Evaluate the functionality of the deployed Django application.
* Assess the correctness and efficiency of the Docker configuration.
* Review the CI pipeline for completeness and effectiveness.
* Examine the Ansible playbook for automation and best practices.
* Check for proper port assignment and conflict avoidance.

**Submission:**

* You should submit your project code (including the Dockerfiles, `docker-compose.yml`, GitHub Actions workflow, and Ansible playbook).
* Include a `README.md` file with clear instructions on how to run and deploy the application.

**Additional Notes:**

* Use environment variables for sensitive data (database credentials, API keys, etc.).
* Avoid conflicts when choosing your ports

**Optional challenge:**

* implementing HTTPS using Let's Encrypt.

**Resources**

* [Demo Repo](https://github.com/pelino250/gitpractice)

