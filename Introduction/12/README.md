Certainly! Let's create an English README for your GitHub project. Below, I'll outline the necessary sections and provide a template for your subfolder.

## Video Media Management Software

Design software for managing video media. Implement features commonly found in a media store, such as menu design, add/edit/delete functionality, search capabilities, and more.

### Class: `Media`

- **Properties**:
    - `name`: The name of the media.
    - `director`: The director of the media.
    - `IMDB score`: The IMDB score of the media.
    - `url`: The URL related to the media.
    - `duration`: The duration of the media.
    - `casts`: A list of actors associated with the media.

- **Methods**:
    - `showInfo()`: Display information about the media.
    - `download()`: Download the media (using the provided URL).

### Subclasses (Inherited from `Media`):

1. **Film (Cinema Film)**:
    - Additional property: None (since cinema films don't have a specific "number of episodes" property).
    - Example: Hollywood blockbuster movies.

2. **Series (TV Series)**:
    - Additional property: `number_of_episodes`.
    - Example: Popular TV shows with multiple episodes.

3. **Documentary**:
    - Additional property: None.
    - Example: Informative documentaries.

4. **Clip (Short Video)**:
    - Additional property: None.
    - Example: Short video clips or promotional material.

### Actor Class:

- Create an `Actor` class to represent actors.
- The `casts` property in the `Media` class will be a list of `Actor` objects.

### File I/O:

- Read information from a file at the start of the program.
- Save any changes to the file when exiting the program.

### Separate Files:

- Implement each class in a separate file. Import them in `main.py`.

### Advanced Search Feature:

- Design an advanced search feature that takes two time values, `a` and `b` (in minutes), from the user.
- Display media whose duration falls between `a` and `b`.

### Downloading Videos:

- If a user calls the `download` method for a video, use the provided URL and the `pytube` library to download it. For guidance, refer to the Instagram account `pylearn@`.

Feel free to customize the properties and methods according to your project's specific requirements. Good luck with your video media management software! 🎥📺.

