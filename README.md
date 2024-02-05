# VegLife

VegLife is a blog post website aimed at vegans. It's purpose is centred around various vegan topics such as lifestyle, food, fashion, and all things that may be interetsing to vegans. The goal of the project was to create a space that is interactive for the user so that they can better interact with their community.

# Design

In this section I will cover the overall design choices of this project.

## Design goals

The overall goal with the design of this project is to make it instantly recognisable what this project is about, create a space that is easy to understand and navigate where users can interact with the content posted as well as customise their own profiles.

## Tools

This project was made using Django, Python, HTML5, CSS3, Bootstrap, and a minimal amount of JavaScript.

Other technologies that I have used are Cloudinary API for storing images on the cloud, allauth for logins and creating secure user registraion, Summernote for forms used to create posts as they have options such as bold and other font modification, and Crispy forms to do some of the more basic forms such as the comment sections ones. I had also used coverage for testing purposes.

## Layout

This project has aimed to have a clear layout on both desktop and mobile, as well as medium sized screens. From the home page I wanted their to be an easy to understand nav bar at the top as well as a photo that makes it easy to understand the subject matter. It will then then go down into a search bar area for users to search by topic and have a page where up to 6 posts will be displayed. There will also be a create post and approve comment buttons, if you are logged in as a super user.

Depending on if the user is logged in or not this will change what the content of the nav bar are, if logged in they will have home, profile, and logout, where logged out users will have home, login, register. This style will also change to a burger icon on smaller screens.

Posts will be layed out in 2 columns showing the author, an image, title, excert, as well as the amount of likes. On samller screens, this will shrink down to 1 column. Wehn posts are clicked the display iamge will be on the top right hand side along with the title going down into the post where the details will be displayed. Under this you will have like button, comment counter, bookmark button, as well as edit and delete if you are the author.

Below is the comment section, which will display the comments on the left and have a block on the right for users to comment. The user will be able to click on the author or commentors name to be taken to their profile. On smaller screens the display will shift to have the comments on top of the comment box.

In the profile section you will see a round image containing a profile image, or a stovk image of a user if they have not set one up. Their is also various sections such as how long they have been vegan, bio, and favourite animal. If it is the logged in users profile, there will be an edit profile, bookmarks, and delete button. All delete buttons have a confirmation page.

I had decided to keep logo and nav bar at the top of each page and the footer at the bottom as I felt that this design choice is one that is very easy to understand for the user who is new to the website. The footer is links to social media platforms.

## Colour Scheme

The colour scheme that I have used for this project is #33cc33 a soft shade of green that I felt was very fitting for vegans as green is a commonly associated colour with vegetables, #595959 a grey colour which I opted for as I thought the black would look too harsh, but it also a dark enough grey to be clearly visible against the white background. I have also used some red in the home image as I felt this coloyr draws attention. Overall I feel this colour scheme is very readable and goes with the general aesthetic that vegans generally like.

<img src="static/images/colours_pp4.png" alt="Photo of colour scheme used through project">

# Features

In this section I will be covering the various features I have implemented, who I had in mind when creating them, and why they are useful. This project will be using the view / model / template functionality and have a high number of different html docs and python scripts.

These features will include a responsive design where the layout changes depending on screen size, like, comment, and bookmark functionality. A custom model that allows users to create their own profile. Ability to create posts for suoer users. And a pagination system that allows multiple pages to be made for every 6 posts.

# User Stories

- User Story 1: Setup Django
- As a Developer, I want to set up Django and install the libraries that I need to get the environment setup properly

- User Story 2: Early Deployment
- As a Developer, I want to deploy do an early deployment of the app to Heroku so that I can make sure that everything is working and that I can do continuous testing during the project

- User Story 3: Django Setup and Secret keys
- As the Developer, I want to setup my Django workspace and and hide my secret keys so that I do not expose secret files,

- User Story 4: Create HTML docs
- As a Developer, I want to get my html templates set up so I can use them throughput the development of the project

- User Story 5: Creating an account as a user
* As a User, I would like to be able to create an account, so that I can view posts and interact with the website.

- User Story 6: View own profile
- As a User, I would like to be able to view my own profile and also see what other users can see when they view my profile

- User Story 7: Insatll Bootstrap
- As a user, I want to set up my environment to include bootstrap so I can apply styling to various parts of the project.

- User Story 8: Login / Logout functionality
- As a User, I would like to be able to login or logout of my account

- User Story 9: View Posts
- As a user, I can view the posts on the website

- User Story 10: Create Posts
- As an admin user, I would like to be able to create posts for the community to review

- User Story 11: Commenting and Liking
- As a user, I want to be able to comment and like various posts and other peoples comments

- User Story 12: User can customise their own profile
- As a User, I would like to be able to edit my profile details such as my bio, so that I can make sure that I am showing relevant, up-to-date information

- User Story 13: Update Posts
- As an admin user, I can update a post that I have created, so that I can correct any mistakes I may have made or add new information

- User Story 14: Delete Posts
- As an admin user, I can delete a post that I made and remove it from the site entirely

- User Story 15: User has option to delete their account
- As a user, I can delete my account, so that I can remove my details and comments from the site

- User Story 16: Bookmarking posts
- As a User, I would like to be able to bookmark interesting posts, so that I can come back and view them again

- User Story 17: Post searching
- As a User, I would like to be able to search the post, so that I can find ones that match the topic I'm looking to explore

- User Story 18: Clear Post layout
- As a User, I would like clear layout of the posts I have clicked, so I can clearly see the information being presented

- User Story 19: Responsiveness
- As the owner of the site, I would like my site to be fully responsive, so that users accessing the site from different devices have an enjoyable experience

# Wireframes

Please see attached wireframes for the main pages of the project, being the home page, a post detail page, and the profiles page. These are the 3 main sections of the project and I will show the home page a post detail page wireframes from lareg and small screens, and the profile page is very similar no mater screen size so only has a asingle wireframe.

<img src="static/images/pp4_home_desktop.png" alt="Wireframe of home page on desktop">
<img src="static/images/pp4_home_mobile.png" alt="Wireframe of home page on mobile">
<img src="static/images/pp4_post_desktop.png" alt="Wireframe of post detail page on desktop">
<img src="static/images/pp4_post_mobile.png" alt="Wireframe of post detail page on mobile">
<img src="static/images/pp4_profile.png" alt="Wireframe of profile page on desktop, tablet and mobile">

# Navigation Bar

- The navigation bar and logo

* Featured on every page and part of the base.html.
* This was created to help the user flow of the website and allow the user to jump between each section at will without having to rely on back commands from the browser. The logo also acts as a home button if the user would like to use that.
* When on a page, the nav bar will have an underline to show the user which specific page they are on. When hovering over a new page the colour will also change to the green to contrast.
* DEpending on if user is logged in or out, the options will differ. Both having home as an option but login and sigup as option if your logged out, and profile and logout if you're logged in

<img src="static/images/navbar_desktop.png" alt="Photo of just the navigation bar on desktop">
<img src="static/images/navbar_mobile.png" alt="Photo of just the navigation bar on mobile">

# Hero Image and text

- Hero image and text

* The hero image was designed to make the introduction the website instantly recognisable.
* The image is fresh looking tomatoes paired with some green veg.
* the image has an overlay of some text to further show the user what the subject of the site is.

<img src="static/images/main_image.png" alt="Photo of just the landing image and overlay text">

# Welcome, Search bar, and Post Creation / Comment Approval

- VegLife introduction

* This is an introductory piece of info with a simple welcome message
* Underneath is a clear search bar with a magnify search button next to it so the user can search specific topics
* Below this is 2 buttons which are only visible for super users, these are buttons for creating new posts and apporving user comments.

<img src="static/images/searchbar.png" alt="Photo of welcome, search bar, and create post / approve comment buttons">

# Posts Section

- The Posts Section

* This section has two columns running down either side of the page, each column contains up to 3 posts.
* In these you will see a featured image, a title, the author, an excerpt, as well as the number of likes and the time and date of posting.
* The posts display in a chronological order and when clicked will bring you to the content of the posts
* This wil display as a single column on smaller screens
* If there are more than 6 posts, there will be a next button a the end of the screen to take the user to the next selection of posts.

<img src="static/images/posts_desktop.png" alt="Photo of posts on home page using desktop">
<img src="static/images/posts_mobile.png" alt="Photo of posts on home page using mobile">

# Footer

- Footer section

* The footer section will be appearing on all the pages. This has been designed with a minimal approach, using links that will take you to social media pages. I have not created social media pages for each of these so the link will guide to the home page of each website.

<img src="static/images/footer.png" alt="Photo of footer section">

# Post Details

- The contents of each post

* When going into a post you will see the image on the right and the title on the left
* On mobile the image will not appear
* Beneath you will see the content of the post
* Lastly is the buttons and like / comment counter. you will see 3 buttons usually unless you created the post, then there is 5
* Like, comment counter, bookmark button, edit, and delete
* These display horizontal on desktop and vertical on mobile

<img src="static/images/postdetail1_desktop.png" alt="Image of top of post detail page on dektop">
<img src="static/images/postdetail2_desktop.png" alt="Image of bottom of post detail page on dektop">
<img src="static/images/postdetail2_mobile.png" alt="Image of top of post detail page on mobile">
<img src="static/images/postdetail1_mobile.png" alt="Image of bottom of post detail page on mobile">

# Tricks Page Content

- Content for the Tricks page

* The page opens with a styled desription of the page. It is clear what this page is for based on decription.
* Following this are 3 seperate sections describing different trciks as well as having a video underneath them to act as a tutorial.
* None of these videos play automatically and also have a volume control slider.

<img src="assets/images/tricks-vids-demo.png" alt="Photo of content on tricks page">

# FAQ Page Photo

- Main Image on FAQ page

- Similar to the other images, I felt this image captured the energy of the website.
- This also has a zoom effect applied.

<img src="assets/images/faq-demo-image.png" alt="Photo of faq main image">

# FAQ Content

- FAQ section

- This section was designed to answer any questions the user may have when getting into skating.
- It includes plenty of basic information as well as a link to the contact page which keeps you in the same tab.

* In this section there are 3 column sections similar in design to the home page to break up the information in an easy digestible way for the user.

<img src="assets/images/faq-content.png" alt="Photo of faq content">

- Safety

- This section was designed to explain to users best safety practice, along with including a link that open in another page to buy safety gear.

<img src="assets/images/safety-content.png" alt="Photo of safety content">

- Equipment content

- This section goes over the various equipment needs of a new skater such as skates, wheels, and accessories.

<img src="assets/images/equipment-content.png" alt="Photo of equipment content">

# Contact Page

- Main image for page, this image has a smiling woman, I chose this as it is inviting and would suit a contact page. This also features the zoom effect.

<img src="assets/images/contact-demo-photo.png" alt="Photo of main contact image">

- The contact form was designed to take the users name, surname, and email.
- Styling this I decided to use a clear border and have the border be visible through a shadow effect, I chose this as I felt it was a more unique design.
- I then added a radio dial button for users to select their level of experience.
- I then made a submit button, this button was designed with rounded edges and to change colour when hovered over.
- It also gets a cursor when hovered over to let the user know it is able to be clicked.
- All parts of the form are required to be filled before you can submit.

* Once you complete the form and submit, you are redirected to a thank you site.

<img src="assets/images/contact-form.png" alt="Photo of submission form">

# Thank you page

- The thank you page is a redirect from the submission form, it is a simple page displaying a thank you message that will redirect you back tot he home page after 10 seconds.

<img src="assets/images/thank-you.png" alt="Photo of thank you page">

# 404 Error page

- A simple 404 page with basic styling to tells the user they have ended up on a page that doesn't exist. It has an explanation and reedirects back to the home page after 5 seconds.

<img src="assets/images/404-image.png" alt="Photo of 404 error page">

# Testing

- Ran html through W3C validator, have gotten back no errors but have gotten back 'warnings'. These warning are due to use of h1 elements in parts of the page that are not the very top. Due to time constraints, I am not able to change this right away as there is a lot of styling applied. If I were to re do the project, I would keep this in mind for future

* ran through Jigsaw css checker, no issues.

* I have checked screen compatibility for phone and tablet, I have checked tablet by using the inspect tool and shrinking down to size and have tested on my own personal mobile to assure it is responsive.

# Bugs

Throughout the project I had encountered several bugs which I will give details of in this section.

Resolved bugs:

- An issue I encountered was when developing my FAQ page. After designing it the footer was going up the page vertically and not horizontally at the bottom. I assumed it must be an issue with HTML and not CSS as it was unique to this page. After scanning through, I noticed I had left a tag unclosed, trying this brought most down to horizontal level, but not all. Then I noticed the entire thing was in one big section. When breaking it off into smaller one the issue had resolved.
- An issue I had encountered when making my page responsive was with my logo. I had it floated to the left and then pushed out with padding to the center. This looked good on desktop but not on other screen sizes. I had initially tried using a flex command to fix this but without much success. I ultimately decided to keep it floated to the left with a small amount of padding as this fixed the issue and made it look good on multiple screen sizes.
- Another bug I came across when when I was adding in my background images for the hero image. I was not able to get this to fit inside the the area I wanted to without looking distorted. After trying to alter the sizing, I used a larger image and a cover command which resolved the issue.
- I also encountered a bug when attaching the youtube videos to the tricks page. Initially were not loading correctling and I was unsure why. After having a look online, I realised I was using incorrect tags. When changed to iframe tags this then worked correctly.

Unresolved bugs:

- A bug I have left uncorrected is on the contact page. The styling shows shadowing on the desktop version but when I checked on the mobile this effect does not appear. I have tried to address this by increasing the shadow effect and this has not worked. Due to time constraints I was not able to find an alternative but I will update in future to something that is compatible with ios

- Another bug left uncorrected was the performance of the pages on mobile screens. I researched how to fix this and came across lazy loading. This solution looked like it would fix the issue how ever it would require JavaScript and I wanted to stick to html and css for this project.

# Lighthouse Testing

<img src="assets/images/home-desktop.png" alt="image of lighthouse for homepage on desktop">
<img src="assets/images/home-mobile.png" alt="image of lighthouse for homepage on mobile">
<img src="assets/images/tricks-desktop.png" alt="image of lighthouse for tricks page on desktop">
<img src="assets/images/tricks-mobile.png" alt="image of lighthouse for tricks page on mobile">
<img src="assets/images/faq-desktop.png" alt="image of lighthouse for faq page on desktop">
<img src="assets/images/faq-mobile.png" alt="image of lighthouse for faq page on mobile">
<img src="assets/images/contact-desktop.png" alt="image of lighthouse for contact page on desktop">
<img src="assets/images/contact-mobile.png" alt="image of lighthouse for contact page on mobile">

# Full Testing

The following devices were used during testing:

Desktop:

- Acer Aspire 5 17" screen

Tablet:

- iPad Air
- iPad Mini

Mobile Devices:

- iPhone 12
- iPhone 12 Pro
- Samsung Galaxy S8+

The following browsers were used during testing:

- Google Chrome
- Safari

All features that are on multiple pages (eg. Logo, Nav bar, Social media links) will only show up as tested in the first page they appear on, but have been tested on all pages.

## Home page testing

<table>
    <tr>
        <th>Feature</th>
        <th>Expected Outcome</th>
        <th>Test</th>
        <th>Result</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td>Logo</td>
        <td>When clicking logo takes back to home page</td>
        <td>Click logo</td>
        <td>Takes back to home page</td>
        <td>pass</td>
    </tr>
    <tr>
        <td>Nav bar highlight</td>
        <td>Hovered page on nav bar will change colour</td>
        <td>Hover over nav bar</td>
        <td>Changed colour</td>
        <td>pass</td>
    </tr>
    <tr>
        <td>Hero image animation</td>
        <td>Hero image will have a zoom effect on all screen sizes</td>
        <td>Reloaded page on different screen sizes</td>
        <td>Animation occured</td>
        <td>pass</td>
    </tr>
    <tr>
        <td>Social media links</td>
        <td>All social media links on footer take you to new tab of the indicated social media</td>
        <td>Click each link</td>
        <td>Social media opened in seperate tabs</td>
        <td>pass</td>
    </tr>
</table>

## Tricks Page Testing

<table>
    <tr>
        <th>Feature</th>
        <th>Expected Outcome</th>
        <th>Test</th>
        <th>Result</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td>Auto play</td>
        <td>Videos do not autoplay when page is loaded</td>
        <td>Reload page and check videos</td>
        <td>Does not autoplay</td>
        <td>pass</td>
    </tr>
    <tr>
        <td>Volume tab</td>
        <td>Videos will allow user to control volume once clicked</td>
        <td>Start video and mute volume with a click or control with cursor</td>
        <td>Volume mutes or goes up/down as intended</td>
        <td>pass</td>
    </tr>
    <tr>
        <td>Pause button</td>
        <td>Video will be able to be paused at anytime</td>
        <td>Click center of video and button in bottom left corner</td>
        <td>Video paused</td>
        <td>pass</td>
    </tr>
    <tr>
        <td>Full screen</td>
        <td>Videos will allow you to go full screen</td>
        <td>Click full screen icon in bottom right corner</td>
        <td>Video appeared full screen</td>
        <td>pass</td>
    </tr>
</table>

## FAQ Page

<table>
    <tr>
        <th>Feature</th>
        <th>Expected Outcome</th>
        <th>Test</th>
        <th>Result</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td>Link to contact page</td>
        <td>When click on the our Contact Page link will take you to contact form in same tab</td>
        <td>Click on our Contact Page link</td>
        <td>Opens contact page in same link</td>
        <td>pass</td>
    </tr>
    <tr>
        <td>Links to recommended products</td>
        <td>When clicking on any of the recommended products linked will take you to a new tab with products</td>
        <td>Click on all 4 of the different links</td>
        <td>Opens all links in new page with the correct product displayed</td>
        <td>pass</td>
    </tr>
</table>

## Contact Page

<table>
    <tr>
        <th>Feature</th>
        <th>Expected Outcome</th>
        <th>Test</th>
        <th>Result</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td>Form must be complete before submitting</td>
        <td>Form does not allow you to proceed unless every section complete</td>
        <td>Click submit with some area not complete</td>
        <td>Does not allow you to continue</td>
        <td>pass</td>
    </tr>
    <tr>
        <td>Email tab</td>
        <td>Email section will not proceed unless an email address is entered</td>
        <td>Click on submit with my full name in the email tab</td>
        <td>Email tab asks me to put in an email address before proceeding</td>
        <td>pass</td>
    </tr>
    <tr>
        <td>Radio button</td>
        <td>Only one radio button option can be selected at a time</td>
        <td>Click one radio button and then click each one after, tried this with every combonation of button</td>
        <td>Does not allow me to have more than one clicked</td>
        <td>pass</td>
    </tr>
    <tr>
        <td>Submit colour change</td>
        <td>Submit button changed colour when hovered over</td>
        <td>Hover over submit button</td>
        <td>Colour of button changes</td>
        <td>pass</td>
    </tr>
    <tr>
        <td>Submit button cursor</td>
        <td>Submit button changes cursor when hovered over</td>
        <td>Hover over submit button</td>
        <td>Cursor changes</td>
        <td>pass</td>
    </tr>
</table>

## Thank You Page

<table>
    <tr>
        <th>Feature</th>
        <th>Expected Outcome</th>
        <th>Test</th>
        <th>Result</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td>Redirect to home page</td>
        <td>When left on page for 10 seconds, you will be redirected to home page</td>
        <td>Load page and wait 10 seconds</td>
        <td>Redirected to home page</td>
        <td>pass</td>
    </tr>
</table>

## 404 Error Page

<table>
    <tr>
        <th>Feature</th>
        <th>Expected Outcome</th>
        <th>Test</th>
        <th>Result</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td>Redirect to home page</td>
        <td>When left on page for 5 seconds, you will be redirected to home page</td>
        <td>Load page and wait 5 seconds</td>
        <td>Redirected to home page</td>
        <td>pass</td>
    </tr>
</table>

# Deployment

- This was deployed in Github, I had done this by going to the seeting of the project, going down to pages in the sidebar, selecting the main branch, and deploying.
- the link to view this is here: https://sean-obrien95.github.io/skate-friendly/

# Forking and Cloning

## Forking the Repository

- Navigate to the main page of the "skate-friendly" repository on GitHub.
- Click on the Fork button in the upper-right corner of the page.
- This will create a copy of the repository under your GitHub account.

## Cloning the Repository

- On your forked repository page, click on the Code button.
- Select the HTTPS option to clone the repository using a secure connection.
- Copy the URL that is shown, which will be https://github.com/sean-obrien95/skate-friendly.git
- Open a terminal on your local machine.
- Navigate to the directory where you want to clone the repository.
- Run the following command: git clone https://github.com/sean-obrien95/skate-friendly.git
- This will create a local copy of the repository on your machine.

# Credit

- Picture credit 1 (hero image): Image by Katya Wolf: https://www.pexels.com/photo/a-roller-skater-tying-the-lace-8733401/
- Health benefits of roller skating taken from WebMD: https://www.webmd.com/fitness-exercise/what-to-know-about-roller-skating#:~:text=Ways%20that%20roller%20skating%20can%20benefit%20your%20body,Making%20you%20more%20flexible%207%20Increasing%20your%20agility
- Woods photo on home page: Photo by Fabian Wiktor: https://www.pexels.com/photo/selective-focus-photo-of-grass-in-forest-3466355/
- Dublin Convention Center Photo: Photo by Bhomick Attri: https://www.pexels.com/photo/an-illuminated-building-during-night-time-11827803/
- Coast line photo: Photo by Nati: https://www.pexels.com/photo/scenic-view-of-sea-and-boats-16015100/
- photo on tricks page: Photo by Laura Stanley: https://www.pexels.com/photo/white-and-red-roller-skates-2005992/
- photo on faq page: Photo by RDNE Stock project: https://www.pexels.com/photo/woman-in-pink-tank-top-and-white-shorts-sitting-on-gray-concrete-road-7335426/
- photo on contact page: Photo by RDNE Stock project: https://www.pexels.com/photo/woman-sitting-on-green-grass-wearing-roller-skates-7335209/
- Youtube videos from moxie roller skates https://www.youtube.com/watch?v=s56SKfk9608
  and queer girl straight skates https://www.youtube.com/watch?v=tKkdItBQM9U https://www.youtube.com/watch?v=nUm9hZ7Xbf8
- Favicon: fav icon: <a target="_blank" href="https://icons8.com/icon/BtCQacVxJCK1/skate">Skate</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>

### I had learned some commands from the following websites

- Flex commands: https://stackoverflow.com/questions/38948102/center-one-and-right-left-align-other-flexbox-element
- Using transition fade on submit button: https://www.w3schools.com/csS/css3_buttons.asp
- Applying shadow effect to contact form: https://blog.logrocket.com/how-to-style-forms-with-css-a-beginners-guide/

* Command for youtube videos: https://www.w3schools.com/html/html_youtube.asp







Veg stock photohome page: Photo by Rauf Allahverdiyev: <https://www.pexels.com/photo/tomatoes-1367242/>
Django using summernote

Defaukt veg photo creadit wfmynews2 <http://content.kens5.com/photo/2017/10/22/vegetables_1508727313637_11456014_ver1.0.jpg>

Default profile pic from researchgate: <https://www.researchgate.net/post/Why_is_RNA_contamination_effecting_my_PCR_product_size>

Files that cannot be shortened in settings.py: 
    151: E501 line too long (91 > 79 characters)
    154: E501 line too long (81 > 79 characters)
    157: E501 line too long (82 > 79 characters)
    160: E501 line too long (83 > 79 characters)
    183: E501 line too long (80 > 79 characters)
