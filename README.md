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
