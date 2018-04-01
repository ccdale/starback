# Starback #
Short-term, Role-based access credentials for AWS.

Rather than managing multiple user credentials for AWS and giving users more access than they actually need the
Starback system allows you to create roles for users, with just enough access rights for what they need to do.

## Features ##
* Generates short term access and secret keys with a session token and (optionally) a federated console login url
  session.
* Role based access keys - just enough access to AWS services and no more.
* Consistent log trail of which key did what and who it was issued to.
* Same key is used for CLI and console session, enables complete tracking of user actions.
* Simple user and access management:
  * Define roles using IAM policies
  * Create users with expiring access tokens to ensure that access is always current.
  * Assign users into groups
  * Assign roles to groups of users and/or individuals.
  * Cascading roles, where higher access levels automatically allow lower level roles to be requested.
