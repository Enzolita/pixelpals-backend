# Pixelpals API
![amiresponsive](documentation/readme-image/PixelGif.gif)
<br>
<br>
Pixelpals is a Full-Stack web application that empowers users to share engaging content, drawing inspiration from popular social media platforms like Instagram. Leveraging Django Rest Framework for robust backend operations and React for a responsive frontend, Pixelpals delivers a smooth, intuitive experience for users to browse, create, and interact with captivating content.
<br>
<br>
The Pixelpals API serves as the backend service for the Pixelpals Application, [view live site here](https://pixelpals-pp5-ee2d5ecf265c.herokuapp.com/).

<hr>

## Table of Contents
- [Pixelpals API](#pixelpals-api)
  - [General Details](#general-details)
  - [Database and model](#database-and-model)
  - [Technologies](#technologies)
  - [Testing and Issues](#testing-and-issues)
  - [Deployment](#deployment)
  - [Credits](#Credits)

## General Details

This is the API for the Pixelpals backend application. Detailed information about strategy, structure, skeleton, surface plane, testing and open issues is found in the frontend repository README and TESTING information.

- The Pixelpals [frontend repository](https://github.com/Enzolita/pixelpals-pp5)
- The Pixelpals [backend repository](https://pixelpals-backend-49bb71efec81.herokuapp.com/)                                    

## Database and Model

In the development environment, Pixelpals uses SQLite, which is simple to set up and ideal for development and testing. For the production environment, PostgreSQL is used due to its robustness, scalability, and advanced features suitable for handling a live web application.

<details>
<summary>Models in Pixelpals</summary>
<br>

### Report model
- **Fields**: Manages user feedback and queries. 
- **Functionality**: Stores user queries, complaints, or suggestions. 
- **Impact**: Provides a direct channel for user feedback, helping to improve the platform based on user input and enhancing user satisfaction.
- **Example**: A user facing an issue with their account can easily send a message to the support team using the report form, ensuring their query is logged and addressed promptly.

### Comment Model
- **Fields**: `id`, `owner`, `post_`, `content`, `created_at`, `updated_at`
- **Functionality**: Stores comments made by users on posts.
- **Impact**: Facilitates engagement and community interaction by allowing users to comment on each other's posts.
- **Example**: Users comment on a friend's post to share their thoughts and reactions, fostering discussions.

### Post Model
- **Fields**: `id`, `owner`, `title`, `content`, `created_at`, `updated_at`
- **Functionality**: Stores posts created by users.
- **Impact**: Central to the content-sharing functionality, allowing users to create and share posts with their followers.
- **Example**: A user creates a new post with a photo from their new PC setup.

### Profile Model
- **Fields**: `id`, `owner`, `name`, `content`, `image`, `created_at`, `updated_at`
- **Functionality**: Stores user profile information.
- **Impact**: Enhances user profiles by allowing customization, making the platform more personalized and engaging.
- **Example**: A user uploads a profile picture and writes a short bio to let other users know more about them.

### Follower Model
- **Fields**: `id`, `owner`, `followed`, `created_at`, `updated_at`
- **Functionality**: Stores follower relationships between users.
- **Impact**: Enables users to follow each other, creating a personalized feed based on followed users' posts.
- **Example**: User A follows User B to see User B's posts in their feed, fostering engagement and community building.

### Like Model
- **Fields**: `id`, `owner`, `post`, `created_at`, `updated_at`
- **Functionality**: Stores likes on posts by users.
- **Impact**: Provides a way for users to express appreciation for content, increasing user interaction and engagement.
- **Example**: A user likes a friend's post, which may also increase the visibility of popular content through likes.

### User Model (from django.contrib.auth.models)
- **Fields**: `id`, `username`, `email`, `password`, `created_at`, `updated_at`
- **Functionality**: Manages user authentication and basic information.
- **Impact**: Provides essential authentication functionality, ensuring users can securely log in and access their accounts.
- **Example**: Users can register, log in, and have their authentication details securely stored.
</details>

### Data Modeling and Database Design

<details>
<summary>Entity-Relationship Diagram</summary>
<br>

The Entity-Relationship Diagram (ERD) provides a visual representation of the database's structure. It helps in planning and illustrating the SQL tables and the relationships between them. The ERD is an essential part of the database design that shows the entities, their attributes, and the types of relationships among the entities.

![erd](/documentation/readme-image/erd.webp)

**Relationships**


1. User
  - One-to-One: User.id → Profile.owner
  - One-to-Many: User.id → Post.owner
  - One-to-Many: User.id → Comment.owner
  - Many-to-Many (through Follower): User.id → Follower.owner
  - Many-to-Many (through Follower): User.id → Follower.followed
  - Many-to-Many (through Like): User.id → Like.owner
  - One-to-Many: User.id → Contact.owner
  - One-to-Many: User.id → Block.owner
  - One-to-Many: User.id → Block.target

2. Profile
  - One-to-One: Profile.owner → User.id

3. Post
  - Many-to-One: Post.owner → User.id
  - One-to-Many: Post.id → Comment.post
  - Many-to-Many (through Like): Post.id → Like.post
  - Many-to-Many: Post.id → Hashtag.post
  - Many-to-One: Post.category → Category.id

4. Comment
  - Many-to-One: Comment.owner → User.id
  - Many-to-One: Comment.post → Post.id

5. Like
  - Many-to-One: Like.owner → User.id
  - Many-to-One: Like.post → Post.id

6. Follower
  - Many-to-One: Follower.owner → User.id
  - Many-to-One: Follower.followed → User.id

8. Report
  - Many-to-One: Report.owner → User.id

</details>

### Database Schema

<details>

<summary>Data Flow</summary>
<br>

To follow best practice, a flowchart was created for the app's logic, and mapped out before coding began using a free version of Draw.io. Please note, that the flowchart provided is designed to offer a simplified visual overview of the application's core workflow. While it captures the essential operations and user interactions, some implementation details and error-handling mechanisms are abstracted for clarity. The actual application logic may involve additional steps and checks not depicted in the flowchart.

![Data Flow](/documentation/readme-image/flowchart.webp)

</details>
<br>

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*

## Technologies

<details>
<summary>Language</summary>
<br>

- [Python](https://www.python.org/) serves as the back-end programming language.

</details>
<br>

<details>
<summary>Frameworks, libraries and dependencies used in the backend part of the project.</summary>
<br>

- [asgiref==3.8.1](https://pypi.org/project/asgiref/) ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI.
- [cloudinary==1.41.0](https://pypi.org/project/cloudinary/) allows you to quickly and easily integrate your application with Cloudinary.
- [dj-database-url==0.5.0](https://pypi.org/project/dj-database-url/0.5.0/) This simple Django utility allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
- [dj-rest-auth==2.1.9](https://dj-rest-auth.readthedocs.io/en/2.1.9/) a set of REST API endpoints to handle User Registration and Authentication tasks.
- [Django==4.2](https://docs.djangoproject.com/en/4.2/) Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- [django-allauth==0.50.0](https://docs.allauth.org/en/latest/) Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
- [django-cloudinary-storage==0.3.0](https://pypi.org/project/django-cloudinary-storage/0.3.0/) Django Cloudinary Storage is a Django package that facilitates integration with Cloudinary by implementing Django Storage API.
- [django-cors-headers==4.4.0](https://pypi.org/project/django-cors-headers/) is a Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).
- [django-filter==2.4.3](https://pypi.org/project/django-filter/2.4.0/) django-filter is a reusable Django application for allowing users to filter querysets dynamically.
- [djangorestframework==3.15.2](https://pypi.org/project/djangorestframework/) is a powerful and flexible toolkit for building Web APIs.
- [djangorestframework-simplejwt==5.3.1](https://pypi.org/project/djangorestframework-simplejwt/) A minimal JSON Web Token authentication plugin for Django REST Framework.
- [gunicorn==23.0.0](https://pypi.org/project/gunicorn/) is a Python WSGI HTTP Server for UNIX.
- [oauthlib==3.2.2](https://pypi.org/project/oauthlib/3.2.2/) is a generic, spec-compliant, thorough implementation of the OAuth request-signing logic.
- [Pillow==10.4.0](https://pypi.org/project/pillow/10.4.0/) The Python Imaging Library enhances your Python interpreter with extensive file format support, efficient data representation, and powerful image processing capabilities.
- [psycopg2==2.9.9](https://pypi.org/project/psycopg2/) PostgreSQL database adapter for the Python programming language. The stand-alone binary package was chosen due to the normal psycopg2 throwing errors.
- [PyJWT==2.9.0](https://pypi.org/project/PyJWT/2.9.0/) JSON Web Token implementation in Python.
- [python3-openid==3.2.0](https://pypi.org/project/python3-openid/) OpenID support for modern servers and consumers.
- [pytz==2024.2](https://pypi.org/project/pytz/2024.2/) allows accurate and cross platform timezone calculations.
- [requests-oauthlib==2.0.0](https://pypi.org/project/requests-oauthlib/2.0.0/) provides first-class OAuth library support for Requests.
- [setuptools==68.0.0](https://pypi.org/project/setuptools/68.0.0/) is a Python library that helps developers package and distribute Python projects. It provides tools to package Python code so it can be easily installed and used by others, either by sharing the package on the Python Package Index (PyPI) or installing it locally.
- [sqlparse==0.5.1](https://pypi.org/project/sqlparse/0.5.1/) sqlparse is a non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.
</details>
<br>

<details>
<summary>Tools and Services</summary>
<br>

- [Code Institute Python Linter](https://pep8ci.herokuapp.com/) a tool to check Python code against some of the style conventions in PEP8.
- [Code Institute Template](https://github.com/Code-Institute-Org/ci-full-template) provided me with a familiar base from which to build my project.
- [Diffchecker](https://www.diffchecker.com/text-compare/) is used to check code snippets.
- [Draw.io](https://www.drawio.com/) is useful for planning the application's architecture and flowcharts, especially helpful in the design phase to visualize the application flow.
- [Git](https://git-scm.com/) is used for version control.
- [Gitpod](https://gitpod.io/) streamlines your development process by providing a pre-configured, cloud-based development environment that's instantly ready for coding.
- [Github](https://github.com/) is essential for version control, allowing you to track changes, collaborate with others (if applicable), and secure online code storage.
- [Google Dev Tools](https://developers.google.com/web/tools) is used during testing, debugging and styling.
- [Heroku](https://www.heroku.com/) is a platform for deploying and hosting web applications.
- [Lucidchart](https://www.lucidchart.com/) is used for ERD (entity relationship diagram)
- [PEP8](https://peps.python.org/pep-0008/) a style guide for Python code.
- [PostgreSQL](https://dbs.ci-dbs.net/) provided by the Code Institute, is employed as the database system for its robustness and compatibility with Django.

</details>
<br>

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*

## Testing and Issues

Information about how the project was tested & Issues encountered, please refer to the [pixelpals-frontend repository, TESTING.md](https://github.com/Enzolita/pixelpals-pp5/blob/main/TESTING.md)

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>*

## Deployment

<details>
<summary>Version Control</summary>
<br>
The site was created using the Gitpod editor and pushed to github to the remote repository ‘pixelpals-frontend’.
The following git commands were used throughout development to push code to the remote repo:

- `git add <file>` - This command was used to add the file(s) to the staging area before they are committed.
- `git commit -m “commit message”` - This command was used to commit changes to the local repository queue ready for the final step.
- `git push` - This command was used to push all committed code to the remote repository on github.
</details>
