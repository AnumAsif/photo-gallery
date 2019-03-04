# MyPhotoGallery
#### Online Photo Gallery where you can view my photos from different locations and different categories. You can share it with your friends by copying the image url, 01/03/2019.
#### By **ANUM ASIF**
## Description
This application is developed by me to share some of my favorite images with everyone. Users can view the details of the picture by clicking on it. Users can also copy the image link to share with their friends. Users can search for a particular category or users can also view the pictures according to the location of image. 
## Specifications
### Application:
1. displays a list of blogs for the user to select from
   - INPUT:"Website opened"
   - OUTPUT:"An area displaying all the existing blogs" 
2. displays a blog with it's comments on a new page when a link to a particular blog is selected
   - INPUT:"blog title clicked"
   - OUTPUT:"A page displaying a blog with all the comments on it"
3. adds a new blog
   - INPUT:"Add new blog button pressed"
   - OUTPUT:"New blog added with title and details"
4. registers user to the website
   - INPUT:"A form containing required info of user is submitted"
   - OUTPUT:"User is registered with a specific email and password"
5. login user to the website
   - INPUT:"User enter password and email address"
   - OUTPUT:"User loggedin to the system" 
6. adds a new comment to the selected blog 
   - INPUT:"Comment button pressed"
   - OUTPUT:"A new comment appear on the blog comments list"	
	
## Setup/Installation Requirements
- Python 3.6
- Django Framework
- HTML, CSS, JavaScript and Bootstrap
- PostgreSQL
## Running the Application
   * To run the application, in your terminal:

    1. Clone or download the Repository
    2. Create a virtual environment
    3. Read the requirements file and Install all the requirements. Or run pip3 install -r requirements.txt to automatically install all the requirements
    4. Prepare environment variables
    -export DATABASE_URL='postgresql+psycopg2://username:password@localhost/blog'
    -export SECRET_KEY='Your secret key'
    4. Run chmod a+x start.sh
    5. Run ./start.sh
    6. Access the application through `localhost:8000`
	
### Development
Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request 
## Known Bugs
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/AnumAsif/photo-gallery/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/AnumAsif/photo-gallery/issues/new). Please include sample queries and their corresponding results.
## Technologies Used
- This project was generated with [Python3.6](https://devdocs.io/python~3.6/) and using [Django](https://docs.djangoproject.com/en/2.1/) framework
## Support and contact details
Please feel free to contact me if you have any suggestion for me to improve this website.
- Email: anum@cockar.com
## Link to live website
- [MyPhotoGallery](https://photo-gallery.herokuapp.com/)
### License
*MIT*
Copyright (c) 2018 **ANUM ASIF**
