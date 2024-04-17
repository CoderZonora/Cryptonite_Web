# Cryptonite_CRUD
This is the project report for my CRUD Application:

<h3>Setup:</h3>
I have used the Spring Boot (version 3.2.4) to get stated and not have to bootstrap everything.The underlying database engine is Sqlite(version 3.42.0.0). 
The interaction with the database is done using the JPA library with Hibernate.

The first choice to make was what kind of spring boot application to generate and what dependencies to use.
Initially I used just the web dependency and later added JDBC,JPA and Sqlite manually.
https://docs.spring.io/spring-data/jpa/docs/2.1.0.RC2/reference/html/#dependencies

I used Java 21 as that is the language I am familiar with,Maven as that was better beginner language than Gradle as per my search and most projects I saw used Maven.
Used Sqlite 3.42.0.0 as that was the most recent stable build with highest number of projects build with it.
https://mvnrepository.com/artifact/org.xerial/sqlite-jdbc



I used JPA to provide a high level implementation without having to directly use complicated SQL queries. 
This was a choice I searched on fro some time to figure out if I use JPA or just JDBC directly.
Ultimately decided on JPA after reading forum posts and articles as I do not really know SQL much.https://medium.com/walmartglobaltech/a-cruncher-choice-jpa-or-jdbc-85c589f584a9

<h3>Development:</h3>
So to get started I searched and learnt basics about Spring Boot and CRUD applications through articles and Youtubes videos.
https://www.youtube.com/watch?v=EqJMYLTmqW4
https://www.youtube.com/watch?v=Pz1IcBjOxj8
https://www.youtube.com/watch?v=riSl59hLCnI
https://www.youtube.com/watch?v=LSEYdU8Dp9Y
https://www.youtube.com/watch?v=K43qyHJXmWI

Also searched about when using spring boot and sqlite is beneficial and how to use them:
https://www.reddit.com/r/webdev/comments/3eha79/so_what_is_the_point_of_sqlite/
https://www.reddit.com/r/learnprogramming/comments/14xuw90/use_cases_for_sqlite/
https://stackoverflow.com/questions/24232892/spring-boot-and-sqlite
https://www.baeldung.com/spring-boot-sqlite

Then I read guides on how to start writing the application:
https://spring.io/guides/gs/spring-boot
https://spring.io/guides/gs/spring-boot#scratch
https://spring.io/guides/gs/spring-boot/
https://github.com/apaspxp/SQLite.demo/tree/master
https://github.com/rkDeependra/Spring-JPA-Demo/tree/main/src/main/java/com/jpa/demo
https://spring.io/guides/gs/accessing-data-jpa
https://github.com/Java-Techie-jt/spring-boot-crud-example
Also got introduced to Lombok at this time but deciding against using it.


So the first problem I had when I started developing the application is how to use Spring Boot annotations as I had never used these earlier. 
Had to read up on the different annotations I saw on the guides and why they were present. 
https://freedium.cfd/https://medium.com/@AlexanderObregon/a-practical-approach-to-entity-and-table-annotations-in-spring-jpa-fbf10a8dc52d
@entiy and @table annnotations

@Override annotation:
https://www.geeksforgeeks.org/the-override-annotation-in-java/

Other annotations:
https://www.codecademy.com/learn/spring-apis-data-with-jpa/modules/spring-data-and-jpa/cheatsheet

@AutoWired
https://www.baeldung.com/spring-autowire

So I started with the Product.java class and writing the setter and getter methods which would be used to create and fetch each element of the database.
This is where I made a mistake which required quite a bit of time to figure out after I had set up the other classes and ran the project first time.
I set the method names as GetName() instead of getName() and so these methods were not actually being used by Spring and instead I was getting an empty database. 
First I tried to change the database to the root as it was initially not at the project root but at a higher directory but that did not work.
I tried to change the sql setting to update instead of create but that did not work. Also tried to find some other problem with the code but could not.
Finally had to use GPT on the code to figure out the reason.

Next was the Product_Repository which is used to implement the CRUDRepository and thus allow the use of its methods. This is also where I had to search a bit on the 
difference between CRUDepository and JPARepository.https://www.geeksforgeeks.org/spring-boot-difference-between-crudrepository-and-jparepository/?ref=lbp
Also learnt about the methods in CRUDRepository interface. https://docs.spring.io/spring-data/commons/docs/current/api/org/springframework/data/repository/CrudRepository.html

Another problem was that Hibernate does not directly support Sqlite. Got error Unable to resolve name org.hibernate.dialect.SQLiteDialect
Had to search a bit about Hibernate alternatives or ways to use Sqlite with Hibernate.
https://www.sqlite.org/lang.html
https://stackoverflow.com/questions/722121/what-should-i-learn-first-spring-or-hibernate
https://www.reddit.com/r/javahelp/comments/k9lcr2/should_i_really_learn_hibernate/
https://www.google.com/search?client=firefox-b-d&q=sqlite+in+spring+boot+without+hibernate#ip=1
https://github.com/eugenp/tutorials/issues/13235
https://elearningindustry.com/spring-boot-vs-hibernate-know-which-framework-fits-your-projects-needs

Finally found the community dependency in this post:
https://stackoverflow.com/questions/17587753/does-hibernate-fully-support-sqlite
	
I had to rely a lot on the guides for the MainController class and look up all the different things in it.

The first was the difference between @Controller and @RestController annotations. GPT explained it the best for me.
The first problem was handling the condition during reading or deleting a single entity but the ID does not exist.
Had to learn about Optional, its methods ad how to utilize them to prevent NullPointers.
There were many small errors here.Major problem was in readProduct() as I had to set up the toString() class for this due to the use of Optional.
Also in the getAllProducts() function as had to use Iterable<Product> to iterate over all the JSON objects.
I am still not very clear on its working and will have to look it up more.


Finally the index.html. I decided to create a static page using JS function instead of using template engine like Thymeleaf.
This was because looks were not a concern and I was familiar with html much better, just had to learn using Javascript with it and how to interact with the database.
The errors were mainly about handling the JSON objects and having to convert them to Strings using JSON.Stringify() as I was getting [object Object].
How to use dynamic URI for fetching particular objects,
using the wrong method like POST instead of PUT in the update method which would perform unexpected behaviour.
Also I made a mistake in deleteAllProducts() method of not specifying the DELETE method.So I was getting method not allowed in the alert box as the defalut method used is GET.

<h3>Local Setup</h3>


Method 1:
Clone the git repo.
Open in an IDE of your choice so that the necessary dependencies get installed.
Run the main class.
The application should be running at https://localhost:8080


Method 2:
If there is a .jar file available, download that.
Make sure java 21 is installed on the system.
Run ```java -jar <file_name>.jar```.
The application should be running at https://localhost:8080


Manual method:
For running this locally, jdk 21(java 21) needs to be installed on the computer.
Start by initializing a new spring boot project either by going to start.spring.io and generating a project or using spring initilizer in their IDE if it suppots it.
the project should have following specifications:
Project - Maven
Language : java
Spring Boot - 3.2.4
Package name:com.example.demo
Name:CRUD
Packaging : jar
Java: 21
Dependencies: Web

Extract and open the generated file in the IDE of choice.
Replace the application.properties and pom.xml files with the ones in the project.Build the maven project again so that the required dependencies get downloaded.
Add the four java files under the directory which contains CRUDApplication.java  and delete the original file.
Put the index.html in src/main/resources/static
Run the CrudBasicApplication.java. After few seconds go to 127.0.0.1/8080 on the browser and the portal should be accessible.
