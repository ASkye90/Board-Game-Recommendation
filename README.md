<a id="readme-top"></a>

<!-- ABOUT THE PROJECT -->
## About The Project

The back-end portion of a board game recommendation engine. 

Using a combination of web scraping and API requests to gather data from boardgamegeek.com and analyze for user-tailored recommendations.


### Supported with

  [![Pycharm][Pycharm.js]][Pycharm-url] [![Python][Python.js]][Python-url] [![GitHub][GitHub.js]][GitHub-url] [![Postgresql][Postgresql.js]][Postgresql-url] [![Playwright][Playwright.js]][Playwright-url] [![BoardGameGeek][BoardGameGeek.js]][BoardGameGeek-url]

<!-- EXAMPLE -->
## Example
Running the script on BGG User: ASkye (https://boardgamegeek.com/collection/user/ASkye)

Results formatted as:

board game id : name - recommendation weight - [ids for board games in collection used while calculating weight]

![pycharm64_Za0jWknBh6](https://github.com/user-attachments/assets/effa54d2-08d9-4009-ac60-d1ab31a0b781)

Using a very simple formula for weights, based on user's ratings and BGG average ratings (producing weights from 1-100).

<!-- CONTACT -->
## Contact

Andrew Skye - andrew.d.skye@gmail.com

Project Link: [https://github.com/ASkye90/Board-Game-Recommendation](https://github.com/ASkye90/Board-Game-Recommendation)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[Pycharm.js]: https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white
[Pycharm-url]: https://www.jetbrains.com/pycharm/

[Python.js]:  https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://www.python.org/

[GitHub.js]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[GitHub-url]: https://github.com/

[Postgresql.js]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[Postgresql-url]: https://www.postgresql.org/

[Playwright.js]: https://img.shields.io/badge/-playwright-%232EAD33?style=for-the-badge&logo=playwright&logoColor=white"
[Playwright-url]: https://playwright.dev/

[BoardGameGeek.js]: https://img.shields.io/badge/BoardGameGeek-FF5100?style=for-the-badge&logo=BoardGameGeek&logoColor=FFFFFF
[BoardGameGeek-url]: https://boardgamegeek.com/
