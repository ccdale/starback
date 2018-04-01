# Starback #
Short-term, Role-based access credentials for AWS.

> **Note** There is no code here (yet) as I need to ask my employer whether this contravenes my employment contract or
> not as I wrote a similiar system for them.


Rather than managing multiple user credentials for AWS and giving users more access than they actually need the
Starback system allows you to create roles for users, with just enough access rights for what they need to do.

## Features ##
* Availability of 99.9% as core components are multi-az and (optionally) mult-region.
* Lambda and API Gateway based.
* Generates short term access and secret keys with a session token and (optionally) a federated console login url
  session.
* Role based access keys - just enough access to AWS services and no more.
* Consistent log trail of which key did what and to whom it was issued.
* Same key is used for CLI and console session, enables complete tracking of user actions.
* Logs into Cloudwatch with (optionally) Cloudtrail tracking.
* Simple user and access management:
  * Define roles using IAM policies
  * Create users with expiring access tokens to ensure that access is always current.
  * Assign users into groups
  * Assign roles to groups of users and/or individuals.
  * Cascading roles, where higher access levels automatically allow lower level roles to be requested.
* Automatic application access management. So long as the user running the application has the required levels of
  access then the application can be written to automatically manage it's own credentials.
