# Straight Rate 2

Straight Rate 2 is a website that allows users to create profiles and rate movies and video games. Users can earn points by reviewing the media posted on the website. There are two thresholds that a user can reach with these points: **Proposer** and **Redactor**.

- **Proposers** can suggest movies and video games to be added to the website.
- **Redactors** can approve those suggestions, and the media will be added to the website.

## IMPORTANT!

In order to approve and suggest media, you will need to create the following groups:

- **Proposer:**  
  Give permissions:  
  - `('can_suggest_movies', 'Can suggest movies')`
  - `('can_suggest_games', 'Can suggest video games')`

- **Redactor:**  
  Give permissions:  
  - `('can_approve_movies', 'Can approve movies')`
  - `('can_approve_games', 'Can approve video games')`

---

## The App Uses:

- **Python 3.12**
- **Django 5.1.3**: Developed using Django.
- **Django REST**: For dynamically adding, viewing, liking, and editing reviews.
- **PostgreSQL Database**: Using PostgreSQL with psycopg2.
- **Pillow**: Image processing for saving posters of movies and video games.

---

## Website Flow

### Homepage

- **Displays the top 5 rated movies and video games:**  

### Movies

- **Movies:** Displays a list of movies available for rating.
- **Movies by Genre:** You can select a genre from the dropdown menu to view all movies in that genre.

### Video Games Dashboard

- **View Video Games:** Displays a list of video games available for rating.
- **Video Games by Genre:** You can select a genre from the dropdown menu to view all games in that genre.

### Search Bar

- **Expandable Search Bar:** The search bar expands when the magnifying glass is clicked or focused.
- **Search Button:** The circle at the end serves as a confirm search button.

### Search Results

- **Display Results:** Shows the movies, video games, directors, or developers matching the search query.  
  *(A query with only one letter will only show movies or video games that start with that letter.)*

### Create an Account

- **User Registration:** Sign up to start rating movies and video games.  
  *(The app uses the AbstractUser with an added points field and a unique constraint on the email field.)*

### Log in

- **User Authentication:** Log in to your account.

### Log out

- **Log Out:** Click the button in the nav bar that appears only when logged in.

### View Profile

- **Profile Page:** Displays or edits the user's profile.
- **Suggest or Approve Media:** Access the suggest and approve pages from here if you have enough points.
- **Edit Reviews:** Clicking on a movie/video game title under "My Reviews" takes you to that page to edit your review.

### Suggest Media

- **Suggest Media:** If you have the right permission, you will be able to access this page and fill out a form to suggest a movie or video game.  
  *(Otherwise, you will be redirected to the home page.)*

### Approve Media

- **Approve Media:** If you have the right permission, you will be able to access this page and approve movies or video games.  
  *(Otherwise, you will be redirected to the home page.)*

### View Media in Detail

- **See Movie or Video Game Details:**  
  Authenticated users can post or edit their reviews as well as like reviews posted by other users.  
  Unauthenticated users can only view the content.

---

## License

This project is licensed under the [MIT License](LICENSE) - feel free to modify and share!

---

