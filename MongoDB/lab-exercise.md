# MongoDB -- Create Vector Embeddings for Your Data | Lab Exercise 01

Welcome Nathan!

In this lab you will authenticate using a verification code from the terminal to associate your existing Atlas account to this lab session. After authenticating, you will return to this window to continue the lab. A short video shows the steps in the 📽️ Video Walkthrough section below.

Copy the verification code in the terminal tab by highlighting it and then clicking it. Then click the link https://account.mongodb.com/account/connect in the terminal output or here to open a browser to Atlas to authenticate.

A screenshot shows an example of a verification code in the terminal and link to open.

If you're already logged into your Atlas account, the lab will skip to the screen requesting the verification code.

A screenshot shows the login options.

Paste the verification code from the terminal output in the terminal tab. If necessary, return to this window to copy the verification code again. Note that the verification code times out after 10 minutes. If this happens, go to the 👨‍💻 Troubleshooting sections to get instructions for getting a new verification code.

A screenshot shows the page where you will paste the verification code.

To connect your lab session and your Atlas account, click the Confirm authorization button.

A screenshot shows the "Confirm authorization" button for MongoDB Atlas.

Once you have authenticated in the MongoDB Atlas webpage, return to this lab in your browser.

A screenshot shows the confirmation of authentication to MongoDB Atlas.

The atlas auth login command in the terminal tab will prompt for you to select a organization. If multiple organizations are provided, always select "MY_MDB_ORG".

Note
If you don't see the "MY_MDB_ORG" Atlas organization, select ANY organization as the check functionality will provision it for you. If you do not have any Atlas organizations, select No to the question "Do you want to enter the Organization ID manually?" Also select No to the question "Do you want to enter the Project ID manually?" The correct organization and project will be created for you when you click the Check button after authenticating successfully to Atlas.

The atlas auth login command displays one of the following messages in the console output when you have successfully authenticated.

If you have a single project associated with your Atlas account, you will see the following:

shell
Successfully logged in as {Your Email Address}.
If you have multiple projects associated with your Atlas account, you will see the following:

shell
Your profile is now configured. You can use [atlas config set] to change these settings at a later time.
Once you have completed the lab, select the Check button.

Do not skip this part of the lab, and ensure the Check button completes.
If it's not already present, this lab creates and deploys a new project with a free-tier cluster, loaded with sample data, configured as follows:

Organization name: "MY_MDB_ORG"
Project name: "MDB_EDU"
Cluster name: "myAtlasClusterEDU"
Database user: "myAtlasDBUser"
Password: "myatlas-001"
Permissions: "readWriteAnyDatabase"
This configuration is required to successfully complete the lab.

If you have an existing Atlas account that doesn't have the necessary permissions to create a new project or cluster in your organization, we recommend creating a separate Atlas account to use with MongoDB University.

Note that the lab platform and the Atlas account that you use on it are independent of your learn.mongodb.com account. For example, you can use a work email for our courses and a personal email for our labs.

---

The following video covers the steps in the Instructions. Note that the Atlas account used in this video has multiple projects associated with it. If you have only a single Atlas project, the steps will be slightly different. You can watch this video full screen in the video tab.

https://play.instruqt.com/embed/mongodb/tracks/create-embeddings/challenges/authenticate-against-atlas/assignment#tab-1

---

If the terminal does not show root@mongodb:~$ and is blank, refresh your web browser page to reload the lab.

If you need to re-authenticate or re-run the authentication command, copy and paste the following into the terminal tab in the terminal (root@mongodb:~$):

shell

copy

run
atlas auth login
If you encounter the "Session closed" error in the terminal tab, reload the window by clicking the reload button. This may require a few attempts. If this fails, restart your browser. If you are still encountering errors after restart, exit the lab and retry it from learn.mongodb.com.

A screenshot shows the reload button for the virtual lab environment.

If you need to scroll back in the terminal, use the Shift + Page Up keys. To scroll forward in the terminal, you can use the Shift + Page Down keys.

If you are still experiencing issues after several attempts, please post in our community forums at https://www.mongodb.com/community/forums/ or email us at learn@mongodb.com.
