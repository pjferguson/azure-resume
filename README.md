# Azure-resume
This is my custom Azure resume, created as part of the [ACG project video.](https://www.youtube.com/watch?v=ieYrBWmkfno&t=837s)

## Project Overview

The Azure-resume project is a personal resume website hosted on Azure. It includes a visitor counter, which is implemented using Azure Functions. The backend and frontend code comes from: https://github.com/ACloudGuru-Resources/acg-project-azure-resume-starter

## Progress and Learnings

### Frontend
- Edited frontend folders' HTML with custom data, this file contains the website.
- Created main.js visitor counter code.

### Managing Keys and SSH
- Managed keys to clone my repo over SSH.

### Azure DB NoSQL
- Configured Azure DB NoSQL to hold the data regarding website count.

### Azure Functions
- Created an Azure function with Python.

### Azure Functions and Virtual Environments
- Created and triggered an Azure function that was run locally.
- Explored Azure functions and their triggers, input bindings, and output bindings.

### Cosmos DB
- Reviewed Microsoft Learn material regarding Cosmos DB.
- Connected Azure Cosmos DB accounts with code, a partition key is required to read specific items in a container.

### Deployment and Security
- Configured the backend properly, connected the DB values to the API via JavaScript.
- Ran into an error with cross-site origin resource origin sharing (CORS), researched more on this security policy.
- Deployed my local function to Azure, creating a secret in the Azure key vault for my connection string to the DB.
- Used Azure blob storage to host HTML files, and updated CORS to match the URL of my newly created static website.
- Configured CDN for my static website, which helps change content at the network edge, which improves network performance.

### CI/CD
- Explored CI/CD, version control, Continuous integration, Continuous Delivery, Continuous Deployment.

## GitHub Workflow for Frontend

I have set up a GitHub Actions workflow for the frontend of this project. This workflow is triggered on every push to the main branch. It automates the process of building, testing, and deploying the frontend code to Azure Blob Storage.

The workflow does the following:

1. Checks out the latest code.
2. Sets up Node.js environment.
3. Installs the necessary dependencies.
4. Builds and tests the project.
5. If the build and tests are successful, it deploys the code to Azure Blob Storage.

This workflow ensures that the deployed frontend is always in a working state and matches the latest version of the code in the main branch.

## Next Steps

- Implement unit tests for the code.
- Set up a similar CI/CD workflow for the backend.

## References
- [Python developer reference for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=asgi,application-level&pivots=python-mode-decorators)
