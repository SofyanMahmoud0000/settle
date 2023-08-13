Read
----

Read project is a set of APIs for a library which contains the following feature

- Create book (Require authentication)
- Update book (Require authentication)
- List books with filteration and pagination
- Get book details 
- Create author (Require authentication)
- List authors
- Login
- Register

## DEMO

You can see a demo for the APIs from [here](https://drive.google.com/file/d/1-CuFNBWOOf5FIDn0xGqPCqG0ST4k0jsT/view?usp=sharing)


## DATA BASE
![schema](https://github.com/sofyanmahmoud0000/settle/blob/master/.gitmedia/schema.png)



If you want to access the database of the container, here they are the configuration 

- Host: `localhost:3307`
- username: `root`
- password: `password`
- database_name: settle

If you want to change the connection of the database, you can change those configuration from the file `.env`
## PREREQUISITES

- [Git](https://github.com/)
- [Docker](https://www.docker.com/)
- [Docker compose](https://docs.docker.com/compose/)

## STEPS TO RUN

- Clone the project 
  ```ssh
  git clone git@github.com:SofyanMahmoud0000/settle.git
  ```

- Navigate to the project root directory
  ```ssh
  cd settle
  ```

- Hit the command 
  ```ssh
  sudo docker compose --profile prod up
  ```
  The output of this command will be like that
  ![docker_compose_output](https://github.com/sofyanmahmoud0000/settle/blob/master/.gitmedia/docker_compose_output.png)

  > If you want to run this command in detached mode use the flag `-d`

- Navigate to the url `http://localhost:5002/apidocs/` to see the APIs documentation

## Build with 
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.3.x/)
* [MySQL](https://dev.mysql.com/doc/refman/8.0/en/what-is-mysql.html)
* [Docker](https://www.docker.com/) 

## Development and support 
If you have any questions on how to use this project, or have ideas for future development, 
please send me an e-mail to sofyan1020@gmail.com.


## Authors
* [Sofyan Mahmoud](https://github.com/sofyanmahmoud0000) - Software development engineer