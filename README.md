## Requirements
- The title on the poll is pulling through the description instead of title (BUG)
- Saving results to database is not working (BUG)
- Result percentage not correctly calculated (BUG)
- Users would like an option to skip the voting process and just see the results (FEATURE REQUEST)
- Add an image from the database to the top of poll (FEATURE REQUEST)

---

### Docker & Docker Compose Setup
Build Image
```
docker-compose build
```

Run Image
```
docker-compose up
open http://localhost:3000
```

_When adding new pip packages be sure to update your requirements.txt. These changes also requires rebuilding of the Docker image. Overview of using Flask with Docker https://medium.com/@terrillowalls/python3-flask-and-docker-in-production-the-easy-way-2ce8080d4f14_

---

### Database Structure with example data

**polls**

| uuid                  | title (VARCHAR) | description (LONGTEXT) | image (LONGTEXT)                   |
|-----------------------|-----------------|------------------------|------------------------------------|
| e3a444--81b4-2a2ae-e4 | A poll title    | A poll description     | https://example.com/image/poll.jpg |

**poll_options**

| poll_id               | name (VARCHAR)  | votes (INT)  |
|-----------------------|-----------------|--------------|
| e3a444--81b4-2a2ae-e4 | Option 1        | 1            |
| e3a444--81b4-2a2ae-e4 | Option 2        | 22           |
